'''
1.7
다형성 지원 :
1. volume_credits

'''


import math



class Performance_calculator():
    def __init__(self, performance_a, play_a):
        self.performance_a = performance_a
        self.play_a = play_a

    def amount(self):
        # 자식 함수 사용 유도
        try:
            pass
        except Exception:
            print('서브 클래스에서 처리하도록 설계되었습니다.')

    def volume_credits(self):
        # 대다수 연극 처리와 장르별 처리를 분리한다.
        # 관객수가 30을 넘는지 검사
        return max(self.performance_a['audience'] - 30, 0)
        # result = 0
        # result += max(self.performance_a['audience'] - 30, 0)
        # if "comedy" == self.performance_a['play']['type']:
        #     result += math.floor(self.performance_a['audience'] / 5)
        # return result


def create_statement_data(invoice, plays):
    def enrich_performance(performances):
        for num, performance_a in enumerate(performances):
            print(num, performance_a)
            
            calculator = create_performance_calculator(performance_a, play_for(performance_a))

            performance_a['play'] = calculator.play_a
            performance_a['amount'] = calculator.amount()
            performance_a['volumeCredits_for'] = calculator.volume_credits()

    def play_for(performance_a):
        return plays[performance_a['playID']]

    def total_volume_credits(data):
        result = 0
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

    enrich_performance(statement_data['performances'])

    statement_data['total_amount'] = total_amount(statement_data)
    statement_data['total_volume_credits'] = total_volume_credits(statement_data)
    print('statement_data : ', statement_data)

    return statement_data


# 다형성
def create_performance_calculator(performance_a, play_a):
    # switch (play.type)
    if "tragedy" == play_a['type']:
        return tragedy_calculator(performance_a, play_a)
    elif "comedy" == play_a['type']:
        return comedy_calculator(performance_a, play_a)
    else:
        print('Unknow type : ', performance_a['play']['type'])

class tragedy_calculator(Performance_calculator):
    def __init__(self, performance_a, play_a):
        super().__init__(performance_a, play_a)

    def amount(self):
        result = 40000
        if (self.performance_a['audience'] > 30):
            result += 1000 * (self.performance_a['audience'] - 30)
        return result


class comedy_calculator(Performance_calculator):
    def __init__(self, performance_a, play_a):
        super().__init__(performance_a, play_a)

    def amount(self):
        result = 30000
        if (self.performance_a['audience'] > 20):
            result += 10000 + 500 * (self.performance_a['audience'] - 20)
        result += 300 * self.performance_a['audience']
        return result

    def volume_credits(self):
        return super().volume_credits() + math.floor(self.performance_a['audience'] / 5)
