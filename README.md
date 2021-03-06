# **Implementation of a PRICE STOCK CHECKER!**

In this repository, you can find a file called main.py that can help you to obtain in real time the stock value of companies in USD by querying an online FMP service. 

By running the main.py module, executing it with '''python main.py AAPL GOOGL ``` while not registered yet, will yield results similar to the following:

```
$ python3 main.py AAPL GOOGL 

Guest user mode, demo started

Company: Apple Inc. 
Stock price: 272.71$

Company: Alphabet Inc. 
Stock price: 1342.98$
```
The user can always ask for more verbosity. 
```
$ python3 main.py AAPL GOOGL -v

Guest user mode, demo started. 
The program will retrieve only real-time stock prices.

Successfully fetched data.
Company Apple Inc. right now has a stock value of 274.16$

Successfully fetched data.
Company Alphabet Inc. right now has a stock value of 1346.18$
```
If you run the following command, you'll register into the database.
```
$ python3 main.py AAPL GOOGL -a USERNAME -p PASSWORD 

User successfully registered!

Company: Apple Inc.
Stock price: 274.16$
Beta: 1.0247

Company: Alphabet Inc.
Stock price: 1347.08$
Beta: 1.1243
```
With this command instead, the user will log-in into the database, allowing him to retrieve also the values of beta of the selected companies.
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
The user, as always, can ask for more verbosity:
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

The user can choose the ticker symbol of a company from those provided and allowed to check. Please remember to write two companies tickers! Moreover, if the user is already registered, he can check also the beta value for the selected companies.
FMP is an on-line resource that provides stock data.

## **Documentation**

## **File with data**

Ticker symbols (such as AAPL, GOOGL) are stored in a .csv file called csv\_stock in my\_package. It’s necessary to write two tickers as input to compare them.
The code in file code\_for\_csv.py  is used only to create the .csv and it is not called by our program. It takes the APIs from the website URL and stores them with .json . Afterwards, it converts the database in .csv with the "pandas" library. So in the .csv there are only the allowed companies' name that the user can write as input to make the program work as intended.

## **Command line parameters**

As positional arguments we have chosen the ticker symbols of the companies that can be found in my\_package/csv\_stock. stock\_code and stock\_code2 are the positional arguments in parsing_input function.

As optional arguments we used:
-a: it will add a new user in the DB
-p: the password of the related username
-c: check for a username and a password in the DB, requires -p
-v: increase the verbosity of the program

## **How to register in the database**
```
$ python3 main.py AAPL GOOGL -a USERNAME -p PASSWORD
```
From this point onward, the user must perform a log-in to get information about the beta of the companies.

## **How to log in into the database**
```
$ python3 main.py AAPL GOOGL -c USERNAME -p PASSWORD
```

## **Testing**

The tests of the code can be found in the /tests directory.
Here, the user can find a module called “test_dbmodule.py” that tests the function open\_and\_create() from dbmanager.py.

To run the tests, from the directory where main.py is situated, run the following command: ```python3 -m unittest -v -b tests.test_dbmodule``` .

## **Team software programmers**

Stefano Torresan - programmer name IvoryTower48
Lorenzo Masarin - programmer name Lore157
Matteo Pettenà - programmer name M-PETT

-------------------------
[FMP](https://financialmodelingprep.com/) is an on-line resource that provides stock data. The APIs are documented in a [API documentation page](https://financialmodelingprep.com/developer/docs/).
