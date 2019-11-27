from mypackage import stock as sck

n,price=sck.get_price("AAPL")
print("Company {} has a stock value of {}$".format(price, n))
n,price=sck.get_price("GOOGL")
print("Company {} has a stock value of {}$".format(price, n))


