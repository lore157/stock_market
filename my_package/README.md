## Implementation of a stock price checker


In this repository you can find a file named ```stock.py``` that implements the ```get_price(company)``` function. It queries the FMP on-line service to receive the stock value of a company in U.S. Dollars. This function is used in the ```main.py``` file to obtain the last price of Apple and Google. If you run the program, executing the main file with: ```python main.py``` it will  give you results similar to the following: 

```
$ python main.py
Apple Inc. = 261.14$
Alphabet Inc. = 1297.13$

Including verbosity
Company 261.14 has a stock value of Apple Inc.
Company 1297.13 has a stock value of Alphabet Inc.
```
Now the code works for the allowed companies names restricted to those in the csv file called csv_stock.csv. 



Note that the project requires the ```json``` and ```requests``` module to run. [FMP](https://financialmodelingprep.com/) is an on-line resource that provides stock data. The APIs are documented in a [API documentation page](https://financialmodelingprep.com/developer/docs/). Note also that ```python2``` will give you a warning on a library, so you most likely want to run the program with: 

```$ python3 main.py```
