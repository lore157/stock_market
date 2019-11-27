import requests
import json
# we import the libraries that we need to build the function

fmp_URL = 'https://financialmodelingprep.com/api/v3/company/profile/%s'
#function definition
def get_price(company="AAPL"):  #we try the function with Apple
    r = requests.get(fmp_URL % company)#we take the value of teh stock from fmp
    data = json.loads(r.text)
    price = data['profile']['price']
    name = data['profile']['companyName']
    return price, name
