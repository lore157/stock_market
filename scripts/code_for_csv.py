
import json
import urllib.request as urllib2
import pandas as pd
''' Taking the data and converting them in .csv

This code takes the APIs from the website URL and stores them with json.
Then, it converts the database in .csv with to_csv using the "pandas" library.
So, in the .csv we are going to find the allowed companies' name that the user
has to write as input to make the program work.
'''


url = "https://financialmodelingprep.com/api/v3/stock/real-time-price"

data = json.load(urllib2.urlopen(url))
df = pd.DataFrame.from_dict(data['stockList'])
df.to_csv(r'Stocks.csv')
