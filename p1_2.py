import math

'''
변수명 변경 
1. 더명확하게 바꿔보자
2. 매개변수 접두어로 type 명을 입력 - 뚜렷하지 않을 경우 an/an

* 컴퓨터가 이해하는 코드는 바보도 작성할 수 있다.
  사람이 이해하도록 작성하는 프로그래머가 전정한 실력자다. 
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


def amount_for(performance_a, play):
    result = 0
    # switch (play.type)
    if "tragedy" == play['type']:
        result = 40000
        if (performance_a['audience'] > 30):
            result += 1000 * (performance_a['audience'] - 30)

    elif "comedy" == play['type']:
        result = 30000
        if (performance_a['audience'] > 20):
            result += 10000 + 500 * (performance_a['audience'] - 20)
        result += 300 * performance_a['audience']
    else:
        try:
            pass
        except Exception:
            print(play['type'])
    return result



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

