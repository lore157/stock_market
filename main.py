from stock import get_price

n,price=get_price("AAPL")
print("Company {} has a stock value of {}$".format(price, n))
n,price=get_price("GOOGL")
print("Company {} has a stock value of {}$".format(price, n))


