import math

'''
반복문 쪼개기
- volumeCredits 변수 제거하기
1. 반복문 돌때마다 누적하기 때문에 리팩토링하기 더 까다롭다.
2. 반복문 쪼개기로 누적되는 부분을 따로 빼낸다.
3. volumeCredits 관련 문장을 한데 모으면 함수 추출하기 쉬워진다.
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

    # for perf in invoice['performances']:
    #     thisAmount = amount_for(perf)
    #
    #     volumeCredits = volumeCredits_for(perf)
    #
    #     # 청구내역을 출력한다.
    #     result += '{} : ${} ({}석) \n'.format(play_for(perf)['name'], thisAmount / 100,  perf['audience'])
    #     totalAmount += thisAmount

    for perf in invoice['performances']:
        # 청구내역을 출력한다.
        result += '{} : ${} ({}석) \n'.format(play_for(perf)['name'], usd(amount_for(perf)),  perf['audience'])
        totalAmount += amount_for(perf)

    volumeCredits = 0  # 변수 선언을 반복문 앞으로
    for perf in invoice['performances']:
        volumeCredits += volumeCredits_for(perf)

    result += '총액 : {} \n'.format(totalAmount/100)
    result += '적립 포인트 : {} 점 \n'.format(volumeCredits)
    return result


def usd(number_a):
    return number_a /100


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

