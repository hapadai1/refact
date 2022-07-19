import math

'''
1.6장 중간 데이터 구조를 인수로 전달

'''

def statement(invoice, plays):
    ''' 1. 중간 데이터 구조를 인수로 전달
        2. invoice, plays - 이 인수 전달을 중간 데이터 구조를 이용하자
        3. invoice 삭제
    '''
    statement_data = {}
    statement_data['customer'] = invoice['customer']
    statement_data['performances'] = invoice['performances']

    # return render_plain_text(statement_data, invoice, plays)
    return render_plain_text(statement_data, plays)

def render_plain_text(data, plays):
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
        for perf in data['performances']:
            result += volumeCredits_for(perf)
        return result

    # inner function
    def total_amount():
        result = 0
        for perf in data['performances']:
            result += amount_for(perf)
        return result

    # 본문
    result = '청구내역 (고객명 : {})\n'.format(data['customer'])
    for perf in data['performances']:
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

