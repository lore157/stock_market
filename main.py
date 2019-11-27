from mypackage import stock as sck #we import the module stock from mypackage

'''
main.py works returning us the value of the company's stock price. Now we define the sentences that the program is going to return when called"
'''
#we import the function get_price from the module stock
n,price=sck.get_price("AAPL")
print("Company {} has a stock value of {}$".format(price, n))
n,price=sck.get_price("GOOGL")
print("Company {} has a stock value of {}$".format(price, n))


