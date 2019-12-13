import requests
import json

# Importing the libraries needed to build the function
fmp_URL = 'https://financialmodelingprep.com/api/v3/company/profile/%s'

# Function definition

# Retrieving only stock price of the chosen company for program demo
def get_price_demo(company):
    r = requests.get(fmp_URL % company)  # Taking data of chosen stock from fmp
    data = json.loads(r.text)
    price = data['profile']['price']
    name = data['profile']['companyName']
    return price, name


# Retrieving all data for registered and logged in users
def get_data_registered(company):
    r = requests.get(fmp_URL % company)  # Taking data of chosen stock from fmp
    data = json.loads(r.text)
    price = data['profile']['price']
    beta = data['profile']['beta']
    name = data['profile']['companyName']
    return price, beta, name
