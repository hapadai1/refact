import math

'''
1.6장 중간 데이터 구조를 인수로 전달

'''

def statement(invoice, plays):

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


    # inner function
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

    result = enrich_performance(statement_data['performances'])


    # 매개변수 전달 방식을 이용함
    statement_data['total_amount'] = total_amount(statement_data)
    statement_data['total_volume_credits'] = total_volume_credits(statement_data)

    print('result : ', result)
    return render_plain_text(statement_data, plays)


def render_plain_text(data, plays):
    print(data)

    # inner function
    def usd(number_a):
        return number_a / 100

    # 본문
    result = '청구내역 (고객명 : {})\n'.format(data['customer'])
    for perf in data['performances']:
        # 청구내역을 출력한다.
        result += '{} : ${} ({}석) \n'.format(perf['play']['name'], usd(perf['amount']), perf['audience'])
    result += '총액 : {} \n'.format(usd(data['total_amount']))
    result += '적립 포인트 : {} 점 \n'.format(data['total_volume_credits'])
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

