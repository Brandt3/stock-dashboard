import requests

# API key EG940FYQTG22BKHV
# View different API functions https://www.alphavantage.co/documentation/

# Checks the API call (mainly the ticker sign if it's valid) 
# Then returns True and the data or Flase and None if invalid ticker sign or ran out of free API's
def fetchApiData(sign):
    func = 'TIME_SERIES_DAILY'
    symbol = sign
    API_key = 'EG940FYQTG22BKHV'
    OutPutSize = "compact" 

    api_url = f"https://www.alphavantage.co/query?function={func}&symbol={symbol}&outputsize={OutPutSize}&apikey={API_key}"

    r = requests.get(api_url)
    data = r.json()

    # This checks the status and also if certain words on in the data to verifiy 
    # that we haven't ran out of free API calls
    if r.status_code == 200 and 'Time Series (Daily)' in data:
        return True, data
    return False, None
