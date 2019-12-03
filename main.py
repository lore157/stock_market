from my_package import stock as sck #Importing module 'stock' from my_package
import sys
import time

'''
main.py works by returning us the value of the company's stock price. Now we define the sentences that the program is going to return when called"
'''

#We import the function get_price from the module stock

#This will check if there are sufficient arguments to make a comparison 
#between companies

if len(sys.argv) > 2:
    n, price= sck.get_price(sys.argv[1])
    print("Company {} has a stock value of {}$".format(price, n))
    n, price= sck.get_price(sys.argv[2])
    print("Company {} has a stock value of {}$".format(price, n))
    time.sleep(5)
    exit()
else:
    print("Give two arguments in input!")
    exit()

