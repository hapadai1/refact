import math

'''
함수 추출하기
1. switch 문은 공연에 대한 요금을 계산한다 --> 코드분석을 통해서 얻는 정보
2. 함수 추출하기 : 코드가 하는 일을 설명하는 이름을 지어준다.
'''

def statement(invoice, plays):
    totalAmount = 0
    volumeCredits = 0
    result = '청구내역 (고객명 : {})\n'.format(invoice['customer'])

    for perf in invoice['performances']:
        play = plays[perf['playID']]
        thisAmount = amount_for(perf, play)

        volumeCredits += max(perf['audience'] - 30, 0)

        if "comedy" == play['type']:
            volumeCredits += math.floor(perf['audience'] / 5)

        # print line for this order
        result += '{} : ${} ({}석) \n'.format(play['name'], thisAmount / 100,  perf['audience'])
        totalAmount += thisAmount

    result += '총액 : {} \n'.format(totalAmount/100)
    result += '적립 포인트 : {} 점 \n'.format(volumeCredits)
    return result


def amount_for(perf, play):
    thisAmount = 0
    # switch (play.type)
    if "tragedy" == play['type']:
        thisAmount = 40000
        if (perf['audience'] > 30):
            thisAmount += 1000 * (perf['audience'] - 30)

    elif "comedy" == play['type']:
        thisAmount = 30000
        if (perf['audience'] > 20):
            thisAmount += 10000 + 500 * (perf['audience'] - 20)
        thisAmount += 300 * perf['audience']
    else:
        try:
            pass
        except Exception:
            print(play['type'])
    return thisAmount



if __name__ == '__main__':
    # data
    from data.plays import plays_json, invoice_json

    # run function
    run_result = statement(invoice_json, plays_json)
    print(run_result)

    # test
    from p1 import statement as origin_statement
    ori_result = origin_statement(invoice_json, plays_json)

    if run_result == ori_result:
        print('test result : OK!!')

