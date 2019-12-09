import requests
import json

# Importing the libraries needed to build the function
fmp_URL = 'https://financialmodelingprep.com/api/v3/company/profile/%s'

# Function definition

# Retrieving the stock price of a chosen company


def get_price(company):
    r = requests.get(fmp_URL % company)  # Taking value of the stock from fmp
    data = json.loads(r.text)
    price = data['profile']['price']
    name = data['profile']['companyName']
    print("...", data, "...")
    return name, price

