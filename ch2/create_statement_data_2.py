'''
1.7
함수 옮기기
: 클래스로 공연료 계산 코드 복사
'''


import math


class Performance_calculator:
    def __init__(self, performance_a, play_a):
        self.performance_a = performance_a
        self.play_a = play_a

    def amount(self):
        result = 0
        # switch (play.type)
        if "tragedy" == self.play_a['type']:
            result = 40000
            if (self.performance_a['audience'] > 30):
                result += 1000 * (self.performance_a['audience'] - 30)

        elif "comedy" == self.play_a['type']:
            result = 30000
            if (self.performance_a['audience'] > 20):
                result += 10000 + 500 * (self.performance_a['audience'] - 20)
            result += 300 * self.performance_a['audience']
        else:
            try:
                pass
            except Exception:
                print('Unknow type : ', self.performance_a['play']['type'])
        return result

    def volume_credits(self):
        result = 0
        result += max(self.performance_a['audience'] - 30, 0)
        if "comedy" == self.performance_a['play']['type']:
            result += math.floor(self.performance_a['audience'] / 5)
        return result


def create_statement_data(invoice, plays):
    def enrich_performance(performances):
        for num, performance_a in enumerate(performances):
            print(num, performance_a)
            # cal class
            calculator = Performance_calculator(performance_a, play_for(performance_a))

            # performance_a['play'] = play_for(performance_a)
            performance_a['play'] = calculator.play_a
            
            # 함수 인라인
            # performance_a['amount'] = amount_for(performance_a)
            performance_a['amount'] = calculator.amount()
            # volumeCredits_for
            # performance_a['volumeCredits_for'] = volumeCredits_for(performance_a)
            performance_a['volumeCredits_for'] = calculator.volumeCredits()

    def play_for(performance_a):
        return plays[performance_a['playID']]


    # class 로 이전하고 class 함수로 작업을 위임한다.
    # def amount_for(performance_a):
    #     return Performance_calculator(performance_a, play_for(performance_a)).amount()

    # def volumeCredits_for(performance_a):
    #     return Performance_calculator(performance_a, play_for(performance_a)).volumeCredits()

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