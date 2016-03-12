#!/usr/bin/env python3

import json, requests, sys

def finance(symbol):
    '''
    Return current-ish stock price data for a given ticker symbol
    args:
    symbol - string representing a stock ticker
    returns:
    printed data
    '''

    r = requests.get('https://finance.yahoo.com/webservice/v1/symbols/'+symbol+'/quote?format=json')
    data = r.json()
    quote = data['list']['resources'][0]['resource']['fields']
    co = quote['name']
    price = quote['price']
    symbol = quote['symbol']
    print(co)
    print(symbol)
    print(price)

finance(sys.argv[1])
