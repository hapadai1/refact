import math

'''
오리지널 예제 
'''
def statement(invoice, plays):
    totalAmount = 0
    volumeCredits = 0
    result = '청구내역 (고객명 : {})\n'.format(invoice['customer'])

    # format = new Intl.NumberFormat("en-US",
    #                   {
    #                       style: "currency", currency: "USD",
    #                       minimumFractionDigits: 2
    #                   }).format;

    for perf in invoice['performances']:
        play = plays[perf['playID']]
        thisAmount = 0

        # switch (play.type)
        if "tragedy" == play['type']:
            thisAmount = 40000
            if (perf['audience'] > 30) :
                thisAmount += 1000 * (perf['audience'] - 30)

        elif "comedy" == play['type']:
            thisAmount = 30000
            if (perf['audience'] > 20) :
                thisAmount += 10000 + 500 * (perf['audience'] - 20)
            thisAmount += 300 * perf['audience']
        else:
            try:
                pass
            except Exception :
                print(play['type'])

        volumeCredits += max(perf['audience'] - 30, 0)

        if "comedy" == play['type']:
            volumeCredits += math.floor(perf['audience'] / 5)

        # print line for this order
        result += '{} : ${} ({}석) \n'.format(play['name'], thisAmount / 100,  perf['audience'])
        totalAmount += thisAmount

    result += '총액 : {} \n'.format(totalAmount/100)
    result += '적립 포인트 : {} 점 \n'.format(volumeCredits)
    return result



if __name__ == '__main__':

    from data.plays import plays_json, invoice_json
    # print(plays_json)
    # print(invoice_json)

    result = statement(invoice_json, plays_json)
    print(result)
