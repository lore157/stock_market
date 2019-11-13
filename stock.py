import requests
import json


fmp_URL = 'https://financialmodelingprep.com/api/v3/company/profile/%s'

def get_price(company="AAPL"):
    r = requests.get(fmp_URL % company)
    data = json.loads(r.text)
    price = data['profile']['price']
    name = data['profile']['companyName']
    return price, name
