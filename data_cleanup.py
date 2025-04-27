from class_structure import Stock, CompanyMetaData


# Data Clean up using JSON and setting it to proper data sctructure
def cleanApiData(sign, data):
    search_data = data['Time Series (Daily)']
    stock_data = []

    meta_data = data['Meta Data']
    symbol = sign
    company_data = []

    for k, v in search_data.items():
        print(f'({v['1. open']}), float({v['2. high']}), float({v['3. low']}), float({v['4. close']}), float({v['5. volume']}), symbol)')
        s1 = Stock(k, float(v['1. open']), float(v['2. high']), float(v['3. low']), float(v['4. close']), float(v['5. volume']), symbol)
        stock_data.append(s1)

    m1 = CompanyMetaData(symbol, (meta_data['3. Last Refreshed']), (meta_data['4. Output Size']), (meta_data['5. Time Zone']))
    company_data.append(m1)

    return stock_data, company_data