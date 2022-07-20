import math

'''
- 임의 변수를 질의 함수로 바꾸기
1. 임시 변수들 때문에 로컬 범위에 존재하는 이름이 늘어나서 추출작업이 복잡해지기 때문이다. 
    --> 지역변수 제거 : 추출작업이 쉬워진다.
2. 긴 함수를 쪼개때마다 play 같은 함수는 최대한 제거하다.
3. play 변수는 개별 pefr에서 얻기 때문에 매개변수 전달이 필요없다. amount_for 에서 계산하면 된다.
4. 중첩함수 변수 인라인
 
- 변수 인라인하기

'''

def statement(invoice, plays):
    totalAmount = 0
    volumeCredits = 0
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


    for perf in invoice['performances']:
        # 인라인 함수로 변경
        # play = play_for(perf)
        thisAmount = amount_for(perf)

        volumeCredits += max(perf['audience'] - 30, 0)

        if "comedy" == play_for(perf)['type']:
            volumeCredits += math.floor(perf['audience'] / 5)

        # print line for this order
        result += '{} : ${} ({}석) \n'.format(play_for(perf)['name'], thisAmount / 100,  perf['audience'])
        totalAmount += thisAmount

    result += '총액 : {} \n'.format(totalAmount/100)
    result += '적립 포인트 : {} 점 \n'.format(volumeCredits)
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

