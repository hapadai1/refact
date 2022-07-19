import math

'''
1.6장 단계쪼개기
프로그램의 논리적인 요소를 파악하기 쉽도록 코드의 구조를 보강하는 리팩토링
1. 두 단계로 나누기 : 데이터 구조(연산), 출력 
2. 첫번째 : 중간 데이터 구조 생성

statement : 데이터 처리
출력 : text, html

renderPlainText : 함수추출 - 분리
'''

def statement(invoice, plays):
    return renderPlainText(invoice, plays)

# 함수 추출하기
def renderPlainText(invoice, plays):
    # inner function
    def play_for(perf):
        return plays[perf['playID']]

    # inner function
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

    # inner function
    def usd(number_a):
        return number_a / 100

    # inner function
    def volumeCredits_for(perf):
        result = 0
        result += max(perf['audience'] - 30, 0)
        if "comedy" == play_for(perf)['type']:
            result += math.floor(perf['audience'] / 5)
        return result

    # inner function
    def total_volume_credits():
        result = 0  # 변수 선언을 반복문 앞으로
        for perf in invoice['performances']:
            result += volumeCredits_for(perf)
        return result

    # inner function
    def total_amount():
        result = 0
        for perf in invoice['performances']:
            result += amount_for(perf)
        return result


    # 본문
    result = '청구내역 (고객명 : {})\n'.format(invoice['customer'])
    for perf in invoice['performances']:
        # 청구내역을 출력한다.
        result += '{} : ${} ({}석) \n'.format(play_for(perf)['name'], usd(amount_for(perf)), perf['audience'])
    result += '총액 : {} \n'.format(usd(total_amount()))
    result += '적립 포인트 : {} 점 \n'.format(total_volume_credits())
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

