import requests
import json

# Importing the libraries needed to build the function
fmp_URL = 'https://financialmodelingprep.com/api/v3/company/profile/%s'


def get_price_demo(company):
    """Retrieving only stock price of the chosen company for program demo

    We are implementing this function when the user is not registered. As
    output it will have the company's stock real time value.

    :param company: the ticker of the company required by the user
    :return: the real time value and the company's complete name
    :rtype: int, str
    """

    r = requests.get(fmp_URL % company)  # Taking data of chosen stock from fmp
    data = json.loads(r.text)
    price = data['profile']['price']
    name = data['profile']['companyName']
    return price, name


def get_data_registered(company):
    """Retrieving stock price and beta of the chosen company

    We are implementing this function when the user is registered. As
    output it will have the company's stock real time value and the beta

    :param company: the ticker of the company required by the user
    :return: the real time value of the stock, the beta and the complete name
    :rtype: int, str, str
    """
    r = requests.get(fmp_URL % company)  # Taking data of chosen stock from fmp
    data = json.loads(r.text)
    price = data['profile']['price']
    beta = data['profile']['beta']
    name = data['profile']['companyName']
    return price, beta, name
