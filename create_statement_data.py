'''
1.6장 파일분리

연산부분 - 중간 데이터 생성

1. 조건부 로직을 다형성으로 바꾸기
2. 상속 계층부터 정의
   : 공연료, 적립 포인트 계산 함수를 담을 클래스 필요
'''


import math

def create_statement_data(invoice, plays):

    def enrich_performance(performances):
        result = {}
        for num, performance_a in enumerate(performances):
            print(num, performance_a)

            performance_a['play'] = play_for(performance_a)

            # amount_for
            performance_a['amount'] = amount_for(performance_a)

            # volumeCredits_for
            performance_a['volumeCredits_for'] = volumeCredits_for(performance_a)

        return result

    # inner function
    def play_for(performance_a):
        return plays[performance_a['playID']]


    # 조건문 수정 필요함 - 연극 장르에따라 계산 방식이 달라진다. 구조적인 요소로 보완
    # 다형성 적용
    def amount_for(performance_a):
        result = 0
        # switch (play.type)
        if "tragedy" == performance_a['play']['type']:
            result = 40000
            if (performance_a['audience'] > 30):
                result += 1000 * (performance_a['audience'] - 30)

        elif "comedy" == performance_a['play']['type']:
            result = 30000
            if (performance_a['audience'] > 20):
                result += 10000 + 500 * (performance_a['audience'] - 20)
            result += 300 * performance_a['audience']
        else:
            try:
                pass
            except Exception:
                print('Unknow type : ', performance_a['play']['type'])
        return result

    # inner function
    def volumeCredits_for(perf):
        result = 0
        result += max(perf['audience'] - 30, 0)
        if "comedy" == perf['play']['type']:
            result += math.floor(perf['audience'] / 5)
        return result

    # inner function
    def total_volume_credits(data):
        result = 0  # 변수 선언을 반복문 앞으로
        for perf in data['performances']:
            result += perf['volumeCredits_for']
        return result

    # inner function
    def total_amount(data):
        result = 0
        for perf in data['performances']:
            result += perf['amount']
        return result

    result = {}
    result['customer'] = invoice['customer']
    result['performances'] = invoice['performances']
    result = enrich_performance(result['performances'])
    # 매개변수 전달 방식을 이용함
    result['total_amount'] = total_amount(result)
    result['total_volume_credits'] = total_volume_credits(result)
    print('result : ', result)

    return result