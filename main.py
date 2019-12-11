from my_package import stock   # Importing module 'stock' from my_package
from scripts import dbmanager  # Importing module 'dbmanager' from scripts
import sys
import time
import argparse
import csv
import json

'''
"main.py" main objective is to return the value of a company's stock price from
an online database with real-time data
'''

# To read the .csv file containing all the allowed companies names.
def readCompaniesCsv():
    reader = csv.reader(open('csv_stock.csv', 'r'))
    companies = []
    next(reader)
    for row in reader:
        companies.append(row[2])
    return companies

'''
The next function requires two positional arguments to identify the companies
and an optional argument that allows the user to get more information about the
status of the program and a more complete output.
'''


def parsing_input():
    parser = argparse.ArgumentParser()
    parser.add_argument("stock_code",
                        help="The ticker symbol of the company.",
                        choices=valid_firms)
    parser.add_argument("stock_code2",
                        help="The ticker symbol of the company.",
                        choices=valid_firms)
    parser.add_argument('-a',
                        help="Add a username (requires -p)",
                        type=str, required=False)
    parser.add_argument('-p',
                        help="The password of the related username.",
                        type=str, required=True)
    parser.add_argument('-c',
                        help="Check for a username and password (requires -p)",
                        type=str,  required=False)
    parser.add_argument("-v",
                        help="Increases verbosity of the program.",
                        action="store_true", default=False)
    args = parser.parse_args()
    return args

# The following code gives the value of the stock price of chosen companies
try:
    valid_firms = readCompaniesCsv()
    args = parsing_input()
    
    dbmanager.open_and_create()
    print("OK 2!")
    if args.a and args.p: 
        dbmanager.save_new_username(args.a, args.p)
        print("OK 2A!")
    elif args.c and args.p:
        print("OK temp!")
        dbmanager.check_for_username(args.c, args.p)
        print("OK 2B!")
    else:
         print ("Insert -a and -p or -c and -p.")
         exit()
    print("OK 3!")

    n, price = stock.get_price(args.stock_code)  # Calling get_price from stock
    if args.v:
        print("Successfully fetched data")
        print("Company {} has a stock value of {}$".format(price, n))
    else:
        print("{} = {}$".format(price, n))

    n, price = stock.get_price(args.stock_code2)

    if args.v:
        print("Successfully fetched data")
        print("Company {} has a stock value of {}$".format(price, n))
    else:
        print("{} = {}$".format(price, n))

# Troubleshooting for mosto common user errors
except:
    # Check if there are sufficient arguments to allow for a company comparison
    if len(sys.argv) > 2:
        print("Write correctly the arguments!")
        exit()
    else:
        print("Write all the required arguments!")
        exit()

