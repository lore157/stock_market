from my_package import stock   # Importing module 'stock' from my_package
from scripts import dbmanager  # Importing module 'dbmanager' from scripts
import sys
import time
import argparse
import csv
import json


def readCompaniesCsv():
    """ Function used to take the company's stock value from the .csv file.

        :return: a list with the stock's value"""

    reader = csv.reader(open('csv_stock.csv', 'r'))
    companies = []
    next(reader)
    for row in reader:
        companies.append(row[2])
    return companies


def output_check(verbosity, reg_status):
    """Tailoring the output according to registration status.

    This function defines the type of output according to user's registration;
    If the user is logging-in it will get the beta value for the company
    required, otherwise it will get just the stock's value. The output changes
    even if the user has required -v in the command line.

    :param verbosity: the level of verbosity required by the user
    :param reg_status: wheter the user is registered or not"""

    # The user is registered and asks for verbosity.
    if verbosity and reg_status:
        print("--------------------------------------------------------------")
        print("Successfully fetched data.")
        print("Company {} right now has a stock value of {}$".format(n, price))
        print("Company {} right now has a beta equal to {}".format(n, beta))
    # The user is registered but doesn't ask for verbosity.
    elif verbosity == False and reg_status == True:
        print("--------------------------------------------------------------")
        print("Company: {}".format(n))
        print("Stock price: {}$".format(price))
        print("Beta: {}".format(beta))
    # The user is not registered but asks for verbosity.
    elif verbosity and reg_status == False:
        print("--------------------------------------------------------------")
        print("Successfully fetched data.")
        print("Company {} right now has a stock value of {}$".format(n, price))
    # The user is  not registered and doesn't ask for verbosity.
    elif verbosity == False and reg_status == False:
        print("--------------------------------------------------------------")
        print("Company: {}".format(n))
        print("Stock price: {}$".format(price))
    return


def parsing_input():
    """Parsing the input for our program.

    This function requires two positional arguments to identify the companies
    that the user is interested in and four optional arguments that are used to
    register the user (-a), to insert the password (-p), to perform a log-in
    (-c) and to get more info about the status of the program (-v). """

    parser = argparse.ArgumentParser()
    # Positional arguments
    parser.add_argument("stock_code",
                        help="The ticker symbol of the company.",
                        choices=valid_firms)
    parser.add_argument("stock_code2",
                        help="The ticker symbol of the company.",
                        choices=valid_firms)
    # Optional arguments
    parser.add_argument('-a',
                        help="To add a username (requires -p)",
                        type=str, required=False)
    parser.add_argument('-p',
                        help="The password of the related username.",
                        type=str, required=False)
    parser.add_argument('-c',
                        help="Check for username and password (requires -p)",
                        type=str, required=False)
    parser.add_argument("-v",
                        help="Increases verbosity of the program.",
                        action="store_true", default=False)
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    """"main.py" main objective is to return the value of a company's stock
    price from an online database with real-time data."""

    try:
        # Retrieve allowed ticker symbols and user input
        valid_firms = readCompaniesCsv()
        args = parsing_input()

        # Access to DB and register or login user
        reg_status = False
        db_name = None
        dbmanager.open_and_create(db_name)

        # Process of user registration
        if args.a and args.p:
            dbmanager.save_new_username(args.a, args.p, args.v)
            reg_status = True
        # The user is already registered
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
        sys.exit(0)
    except NameError:
        print("\nWrite both ticker symbols!")
        sys.exit(2)
    except:
        # Check for sufficient arguments to allow for a company comparison
        if args.stock_code and args.stock_code2:
            print("\nWrite correctly the ticker symbols!")
            sys.exit(3)

