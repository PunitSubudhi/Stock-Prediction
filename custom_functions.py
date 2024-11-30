import pandas as pd
import yfinance as yf
import prophet as prophet

def get_tickers(symbols):
    to_return = []
    for symbol in symbols:
        ticker = get_ticker(symbol)
        print(ticker)
        if ticker != None:
            to_return.append(ticker)
    print(to_return)
    return to_return
    
def get_ticker(symbol):
    ticker = yf.Ticker(symbol)
    if ticker.history(period='1d').__len__() == 0:
        print(ticker.info)
        return None
    return ticker

def get_history(tickers: list):
    return [ticker.history(period="max") for ticker in tickers]