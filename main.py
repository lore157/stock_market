from my_package import stock   # Importing module 'stock' from my_package
from scripts import dbmanager  # Importing module 'dbmanager' from scripts
import sys
import time
import argparse
import csv
import json

'''
"main.py" main objective is to return the value of a company's stock price from
an online database with real-time data.
'''

# To read the .csv file containing all the allowed company names.


def readCompaniesCsv():
    reader = csv.reader(open('csv_stock.csv', 'r'))
    companies = []
    next(reader)
    for row in reader:
        companies.append(row[2])
    return companies

# To display data according to verbosity and user status


def output_check(verbosity, reg_status):
    if verbosity and reg_status:
        print("--------------------------------------------------------------")
        print("Successfully fetched data.")
        print("Company {} right now has a stock value of {}$".format(n, price))
        print("Company {} right now has a beta equal to {}".format(n, beta))
    elif verbosity == False and reg_status == True:
        print("--------------------------------------------------------------")
        print("Company: {}".format(n))
        print("Stock price: {}$".format(price))
        print("Beta: {}".format(beta))
    elif verbosity and reg_status == False:
        print("--------------------------------------------------------------")
        print("Successfully fetched data.")
        print("Company {} right now has a stock value of {}$".format(n, price))
    elif verbosity == False and reg_status == False:
        print("--------------------------------------------------------------")
        print("Company: {}".format(n))
        print("Stock price: {}$".format(price))
    return


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
                        help="To add a username (requires -p)",
                        type=str, required=False)
    parser.add_argument('-p',
                        help="The password of the related username.",
                        type=str, required=False)
    parser.add_argument('-c',
                        help="To check for a username and password \
                             (requires -p)", type=str, required=False)
    parser.add_argument("-v",
                        help="Increases verbosity of the program.",
                        action="store_true", default=False)
    args = parser.parse_args()
    return args


# Main function, return the value of the stock price of chosen companies.
if __name__ == "__main__":
    try:
        # Retrieve allowed ticker symbols and user input
        valid_firms = readCompaniesCsv()
        args = parsing_input()

        # Access to DB and register or login user
        reg_status = False
        dbmanager.open_and_create()

        if args.a and args.p:
            dbmanager.save_new_username(args.a, args.p, args.v)
            reg_status = True
        elif args.c and args.p:
            reg_status = dbmanager.check_for_username(args.c, args.p, args.v)

        if not reg_status:
            print("\nGuest user mode, demo started.")
            print("The program will retrieve only real-time stock prices.")

        # Change in the behaviour of the program according to user status
        if reg_status:
            price, beta, n = stock.get_data_registered(args.stock_code)
            output_check(args.v, reg_status)
            price, beta, n = stock.get_data_registered(args.stock_code2)
            output_check(args.v, reg_status)
        else:
            price, n = stock.get_price_demo(args.stock_code)
            output_check(args.v, reg_status)
            price, n = stock.get_price_demo(args.stock_code2)
            output_check(args.v, reg_status)
        print("--------------------------------------------------------------")

    # Troubleshooting for most common user errors
    except SystemExit:
        print("\nQuitting the program now.")
        sys.exit()
    except NameError:
        print("\nWrite both ticker symbols!")
        sys.exit()
    else:
        # Check for sufficient arguments to allow for a company comparison
        if args.stock_code and args.stock_code2:
            print("\nWrite correctly the ticker symbols!")
            sys.exit()
