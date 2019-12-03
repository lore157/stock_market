import requests
import json
# Importing the libraries needed to build the function

fmp_URL = 'https://financialmodelingprep.com/api/v3/company/profile/%s'

# Function definition
def get_price(company):  
    r = requests.get(fmp_URL % company)  #We take the value of the stock from fmp
    data = json.loads(r.text)
    price = data['profile']['price']
    name = data['profile']['companyName']
    return price, name
