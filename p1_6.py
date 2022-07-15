import math

'''
함수 추출
1. 반복문 쪼개기 : 변수값 누적 부분
2. 문장 슬라이드 : 초기화 문장을 누적코드 바로 앞으로
3. 함수 추출하기 : 적립 포인트 계산 부분을 함수로 추출
4. 변수 인라인하기 : 로컬 변수 제거 volumeCredits

* 성능 문제
1. 똑똑한 컴파일러
2. 특별한 경우가 아니라면 일단 무시하자
3. 리팩토링 후에 성능을 개선하자. 그게 더 쉽다.
'''

def statement(invoice, plays):
    totalAmount = 0
    # volumeCredits = 0
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

    #
    def total_volume_credits():
        volumeCredits = 0  # 변수 선언을 반복문 앞으로
        for perf in invoice['performances']:
            volumeCredits += volumeCredits_for(perf)
        return volumeCredits

    for perf in invoice['performances']:
        # 청구내역을 출력한다.
        result += '{} : ${} ({}석) \n'.format(play_for(perf)['name'], usd(amount_for(perf)),  perf['audience'])
        totalAmount += amount_for(perf)
    
    # 값 계산 로직을 함수로 추출
    # volumeCredits = total_volume_credits()

    result += '총액 : {} \n'.format(usd(totalAmount)) # 변수 인라인
    result += '적립 포인트 : {} 점 \n'.format(total_volume_credits())  # 변수 인라인
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

