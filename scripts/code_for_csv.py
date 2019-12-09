#This code takes the APIs from the website URL and stores them with json. Then, it converts the database in csv with to_csv using the library pandas. So, in the csv we are going to find the allowed companies name that the user has to write as input to make the program working. 

import json
import urllib.request  as urllib2 
url = "https://financialmodelingprep.com/api/v3/stock/real-time-price"
data = json.load(urllib2.urlopen(url))

import pandas as pd

df = pd.DataFrame.from_dict(data['stockList'])

df.to_csv(r'Stocks.csv')
