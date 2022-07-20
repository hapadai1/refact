import math

'''
- 처리해야할 변수 2개
1. volumeCredits 메소드 추출 , 변수 정리
'''

def statement(invoice, plays):
    totalAmount = 0
    volumeCredits = 0
    result = '청구내역 (고객명 : {})\n'.format(invoice['customer'])

    # 중첩함수
    def play_for(perf):
        return plays[perf['playID']]

    # 중첩함수
    def amount_for(performance_a):
        result = 0
        # switch (play.type)
        if "tragedy" == play_for(performance_a)['type']:
            result = 40000
            if (performance_a['audience'] > 30):
                result += 1000 * (performance_a['audience'] - 30)

        elif "comedy" == play_for(performance_a)['type']:
            result = 30000
            if (performance_a['audience'] > 20):
                result += 10000 + 500 * (performance_a['audience'] - 20)
            result += 300 * performance_a['audience']
        else:
            try:
                pass
            except Exception:
                print(play_for(performance_a)['type'])
        return result
    
    # 중첩함수 : 내부 변수 정리
    def volumeCredits_for(perf):
        result = 0
        result += max(perf['audience'] - 30, 0)
        if "comedy" == play_for(perf)['type']:
            result += math.floor(perf['audience'] / 5)
        return result

    for perf in invoice['performances']:
        # 인라인 함수로 변경
        # play = play_for(perf)
        thisAmount = amount_for(perf)

        # volumeCredits = volumeCredits_for(perf, play_for, volumeCredits)
        volumeCredits = volumeCredits_for(perf)

        # print line for this order
        result += '{} : ${} ({}석) \n'.format(play_for(perf)['name'], thisAmount / 100,  perf['audience'])
        totalAmount += thisAmount

    result += '총액 : {} \n'.format(totalAmount/100)
    result += '적립 포인트 : {} 점 \n'.format(volumeCredits)
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

