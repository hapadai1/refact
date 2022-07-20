'''
1.7
중간데이터 클래스
: 공연료, 적립 포인트 계산 함수를 담을 클래스 필요
'''


import math


class Performance_calculator:
    def __init__(self, performance_a, play_a):
        self.performance_a = performance_a
        self.play_a = play_a

def create_statement_data(invoice, plays):

    def enrich_performance(performances):
        for num, performance_a in enumerate(performances):
            print(num, performance_a)
            # cal class
            calculator = Performance_calculator(performance_a, play_for(performance_a))

            # performance_a['play'] = play_for(performance_a)
            performance_a['play'] = calculator.play_a
            # amount_for
            performance_a['amount'] = amount_for(performance_a)
            # volumeCredits_for
            performance_a['volumeCredits_for'] = volumeCredits_for(performance_a)

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

    statement_data = {}
    statement_data['customer'] = invoice['customer']
    statement_data['performances'] = invoice['performances']

    # statement_data = enrich_performance(statement_data['performances'])
    enrich_performance(statement_data['performances'])

    # 매개변수 전달 방식을 이용함
    statement_data['total_amount'] = total_amount(statement_data)
    statement_data['total_volume_credits'] = total_volume_credits(statement_data)
    print('statement_data : ', statement_data)

    return statement_data