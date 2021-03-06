#!/usr/bin/env python3

import requests
import sys

def finance(symbol):
    '''
    Return current-ish stock price data for a given ticker symbol
    args:
    symbol - string representing a stock ticker
    returns:
    printed data
    '''
    headers = {'user-agent' : 'Mozilla/5.0'}
    r = requests.get('https://finance.yahoo.com/webservice/v1/symbols/'+symbol+'/quote?format=json', headers=headers)
    try:
        data = r.json()
        quote = data['list']['resources'][0]['resource']['fields']
        co = quote['name']
        price = quote['price']
        symbol = quote['symbol']

        print(co)
        print(symbol)
        print(price)
    except:
        print("No data found for symbol " + symbol.upper())

if len(sys.argv) == 1:
    print("Usage: ./midas tckr1 tckr2")
else:
    for i in range(1, len(sys.argv)):
        finance(sys.argv[i])
