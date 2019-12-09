from my_package import stock  # Importing module 'stock' from my_package
import sys
import time
import argparse

# "main.py" will return us the value of the chosen company's stock price.

'''
This function requires two positional arguments to identify and compare the
companies and an optional argument that allow the user to get more explicit
information about the program.
'''

valid_firms = ["AAPL", "GOOGL"]


def parsing_input():
    parser = argparse.ArgumentParser()
    parser.add_argument("stock_code",
                        help="The ticker symbol of the company.",
                        choices=valid_firms)
    parser.add_argument("stock_code2",
                        help="The ticker symbol of the company.",
                        choices valid_firms)
    parser.add_argument("-v",
                        help="Increases verbosity of the program.",
                        action="store_true", default=False)
    args = parser.parse_args()
    return args

# The following code tries to retrieve the stock price of the input companies.
try:
    args = parsing_input()
    n, price = stock.get_price(args.stock_code)  # Calling get_price
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

# The next section helps the user recognize what did wrong when running main.py

except:
    # Check if there are sufficient arguments to allow for a comparison
    if len(sys.argv) > 2:
        print("Write correctly the arguments!")
        exit()
    # Most common error would be not writing all the arguments needed
    else:
        print("Write all the required arguments!")
        exit()

