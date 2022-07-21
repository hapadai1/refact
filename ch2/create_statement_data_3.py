'''
1.7
다형성 지원 :
1. 타입코드를 서버클래스로 바꾸기

Performance_calculator 의 서브 클래스들을 준비하고
create_statement_data 에서 적합한 서브클래스를 사용하게 만들어야한다.

2. 생성자를 팩터리 함수로 바꾸기
딱 맞는 서브클래스를 사용하려면 생성자 대신 함수를 호출하도록 바꿔야한다.(JS 문제)
'''


import math



class Performance_calculator:
    def __init__(self, performance_a, play_a):
        self.performance_a = performance_a
        self.play_a = play_a

    def amount(self):
        # 자식 함수 사용 유도
        try:
            pass
        except Exception:
            print('서브 클래스에서 처리하도록 설계되었습니다.')
        # result = 0
        # # switch (play.type)
        # if "tragedy" == self.play_a['type']:
        #     # print('Unknow type : ', self.performance_a['play']['type'])
        #     # result = 40000
        #     # if (self.performance_a['audience'] > 30):
        #     #     result += 1000 * (self.performance_a['audience'] - 30)
        #
        # elif "comedy" == self.play_a['type']:
        #     # result = 30000
        #     # if (self.performance_a['audience'] > 20):
        #     #     result += 10000 + 500 * (self.performance_a['audience'] - 20)
        #     # result += 300 * self.performance_a['audience']
        # else:
        #     try:
        #         pass
        #     except Exception:
        #         print('Unknow type : ', self.performance_a['play']['type'])
        # return result

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
            
            # 생성자 대신 팩터리 함수 이용
            # Performance_calculator 의 서브 클래스 중에서 어느것을 생성해서 반환할지 선택할 수 있다.
            # calculator = Performance_calculator(performance_a, play_for(performance_a))
            calculator = create_performance_calculator(performance_a, play_for(performance_a))

            # 함수 인라인
            performance_a['play'] = calculator.play_a
            performance_a['amount'] = calculator.amount()
            performance_a['volumeCredits_for'] = calculator.volume_credits()

    def play_for(performance_a):
        return plays[performance_a['playID']]

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

    enrich_performance(statement_data['performances'])

    # 매개변수 전달 방식을 이용함
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
    # return Performance_calculator(performance_a, play_a)

class tragedy_calculator(Performance_calculator):
    def amount(self):
        result = 40000
        if (self.performance_a['audience'] > 30):
            result += 1000 * (self.performance_a['audience'] - 30)
        return result


class comedy_calculator(Performance_calculator):
    def amount(self):
        result = 30000
        if (self.performance_a['audience'] > 20):
            result += 10000 + 500 * (self.performance_a['audience'] - 20)
        result += 300 * self.performance_a['audience']
        return result


