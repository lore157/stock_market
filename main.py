from my_package import stock #Importing module 'stock' from my_package
import sys
import time
import argparse
import csv
import json

'''
main.py works by returning us the value of the company's stock price. Now we define the sentences that the program is going to return when called"
'''


#With this function we can read the csv file containing all the allowed valid companies names

def readCompaniesCsv():
    reader = csv.reader(open('csv_stock.csv', 'r'))
    companies = []
    next(reader)
    for row in reader:
        companies.append(row[2])
    return companies

valid_firms = readCompaniesCsv()

#This function requires two positional arguments to identify the companies and an optional argument that allow the user to get more explicit information about the program"

def parsing_input():
    parser = argparse.ArgumentParser()
    parser.add_argument("stock_code",
                        help= "The ticker symbol of the company.",
                        choices= valid_firms)
    parser.add_argument("stock_code2",
                        help= "The ticker symbol of the company.",
                        choices= valid_firms)
    parser.add_argument("-v", 
                        help= "Increases verbosity of the program.",
                        action= "store_true", default= False)
    args = parser.parse_args()
    return args

#The following code gives the value of the stock price of the input companies
try:
    args= parsing_input()
    n, price= stock.get_price(args.stock_code) #import the function get_price from the module stock
    if args.v:
        print("Successfully fetched data")
        print("Company {} has a stock value of {}$".format(price, n))
    else:
        print("{} = {}$".format(price, n))

    n, price= stock.get_price(args.stock_code2)

    if args.v:
        print("Successfully fetched data")
        print("Company {} has a stock value of {}$".format(price, n))
    else:
        print("{} = {}$".format(price, n))

#This code helps the user to check if he wrote correctly the inputs
except:
#This will check if there are sufficient arguments to make a comparison between companies
    if len(sys.argv)>2:
        print("Write correctly the arguments!")
        exit()
    else:
        print("Write all the required arguments!")
        exit()


    

	

