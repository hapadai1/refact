'''
1.6장 파일분리
출력부분
'''

from create_statement_data_1 import create_statement_data

def statement(invoice, plays):
    return render_plain_text(create_statement_data(invoice, plays))

def render_plain_text(data):
    # 본문
    result = '청구내역 (고객명 : {})\n'.format(data['customer'])
    for perf in data['performances']:
        # 청구내역을 출력한다.
        result += '{} : ${} ({}석) \n'.format(perf['play']['name'], usd(perf['amount']), perf['audience'])
    result += '총액 : {} \n'.format(usd(data['total_amount']))
    result += '적립 포인트 : {} 점 \n'.format(data['total_volume_credits'])
    return result


def html_statement(invoice, plays):
    return render_html(create_statement_data(invoice, plays))

def render_html(data):
    result = '<h1>Statement for BigCo</h1>\n'
    result += '<table>\n'
    result += '<tr><th>연극</th><th>죄석수</th><th>금액</th></tr>'

    for perf in data['performances']:
        result += '<tr><td>{}</td>'.format(perf['play']['name'])
        result += '<td>{}석</td>'.format(perf['audience'])
        result += '<td>${}</td></tr>\n'.format(usd(perf['amount']))
        result += '<table>\n'

    result += '<p>Amount owed is <em>${}</em></p>\n'.format(data['total_amount'])
    result += '<p>You earned <em>{}</em> credits</p>\n'.format(data['total_volume_credits'])
    return result

def usd(number_a):
    return number_a / 100



if __name__ == '__main__':
    # data
    from data.plays import plays_json, invoice_json

    # run function
    run_result = statement(invoice_json, plays_json)
    print(run_result)
    html_result = html_statement(invoice_json, plays_json)
    print(html_result)

    # test
    from ch1.p1 import statement as origin_statement
    ori_result = origin_statement(invoice_json, plays_json)

    if run_result == ori_result:
        print('test result : OK!!')

