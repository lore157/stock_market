# **Implementation of a PRICE STOCK CHECKER!**

In this repository, you can find a file called main.py that can help you to obtain in real time the stock value of companies in US dollars by querying an online FMP service. 

If you run the program, executing the main file with python main.py AAPL GOOGL  and you are not registered yet, it will give you results similar to the following:

```
$ python3 main.py AAPL GOOGL 

Guest user mode, demo started
Company: Apple Inc. 
Stock price: 272.71$
Company: Alphabet Inc. 
Stock price: 1342.98$
```
The user can ask for more verbosity 
```
$ python3 main.py AAPL GOOGL -v

Guest user mode, demo started. 
The program will retrieve only real-time stock prices.
Successfully fetched data.
Company Apple Inc. right now has a stock value of 274.16$
Successfully fetched data.
Company Alphabet Inc. right now has a stock value of 1346.18$
```
If you run the following program you are registering. Since, it is the first time you register, it will give you only the prices of the stocks.
```
$ python3 main.py AAPL GOOGL -a USERNAME -p PASSWORD 

User successfully registered!
The program will retrieve only real-time stock prices.
Company: Apple Inc.
Stock price: 274.16$
Company: Alphabet Inc.
Stock price: 1347.08$
```
If you run the following program, you are logging in into the database and you can receive also the values of beta of the selected companies.
```
$ python3 main.py AAPL GOOGL -c USERNAME -p PASSWORD 

Username and password are correct.
Company: Apple Inc.
Stock price: 274.16$
Beta: 1.139593
Company: Alphabet Inc.
Stock price: 1347.08$
Beta: 1.058184
```
The user can ask for more verbosity :
```
$ python3 main.py AAPL GOOGL -c USERNAME -p PASSWORD -v

Retrieving password...
Done!
Username and password are correct.
Successfully fetched data.
Company Apple Inc. right now has a stock value of 274.16$
Company Apple Inc. right now has a beta equal to 1.139593
Successfully fetched data.
Company Alphabet Inc. right now has a stock value of 1347.08$
Company Alphabet Inc. right now has a beta equal to 1.058184
```

The user can choose the ticker symbol of a company from those provided and allowed to check. Please remember to write two companies tickers so you can compare them better! Moreover, if the user is already registered can check also the beta value for the selected companies.
FMP is an on-line resource that provides stock data.

## **Documentation**

## **File with data**

Tickers symbols (such as AAPL, GOOGL) are stored in a .csv file called csv_stock in my_package/csv_stock. It’s necessary to write two tickers as input to compare them.
The code in file code_for_csv.py  is used only to create the csv and it is not called by our program. It takes the APIs from the website URL and stores them with json. Then, it converts the database in .csv with to_csv using the "pandas" library. So, in the .csv we are going to find the allowed companies' name that the user has to write as input to make the program work.

## **Command line parameters**

As positional arguments we have chosen the tickers symbol of the companies that can be found in my_package/csv_stock.  stock_code and stock_code2 are the positional arguments in parsing input function.
As optional arguments we used:
-a: it will add a new user
-p: add the password of the related username
-c: check for a username and a password, requires -p
-v: increase the verbosity of the program 
How to register in the database
```
$ python3 main.py AAPL GOOGL -a USERNAME -p PASSWORD
```
You must do a log in to get information about the beta of the companies.

How to log in into the database
```
$ python3 main.py AAPL GOOGL -c USERNAME -p PASSWORD
```

## **Testing**

The tests of the code are shown in the file: my_package/test
Here, you can find one python module called “test.py” that test of the function readCompaniesCsv from main.py and the function check_for_username from dbmanager.py
To run the tests: python3 -m unittest -v -b test/test_stock.py 
TESTS DO NOT WORK! 


## **Team software programmers**

Lorenzo Masarin - programmer name Lore157
Matteo Pettenà - programmer name M-PETT
Stefano Torresan – programmer name IvoryTower48

-------------------------
[FMP](https://financialmodelingprep.com/) is an on-line resource that provides stock data. The APIs are documented in a [API documentation page](https://financialmodelingprep.com/developer/docs/).
