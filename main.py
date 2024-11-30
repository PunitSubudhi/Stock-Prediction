import streamlit as st
import pandas as pd
import yfinance as yf
import prophet as prophet
import streamlit_tags
from custom_functions import *

# st.page_config(layout="wide", initial_sidebar_state="expanded")



with st.sidebar:
    st.title("Stock Prediction")
    st.write("Enter the stock symbol and the number of days you want to predict")
    stock_symbol = streamlit_tags.st_tags()
    tickers = get_tickers(stock_symbol)
    view = st.segmented_control("View", ['view','graph'],label_visibility='collapsed')
    if len(tickers) < len(stock_symbol):
        st.write("Some of the stock symbols you entered are invalid")
        
if 'view' in view:   
    for df,symbol in zip(get_history(get_tickers(stock_symbol)), get_tickers(stock_symbol)):
        with st.expander(symbol.info['longName'], expanded=False):
            st.dataframe(df)

if 'graph' in view:
    for df,symbol in zip(get_history(get_tickers(stock_symbol)), get_tickers(stock_symbol)):
        with st.expander(symbol.info['longName'], expanded=False):
            st.line_chart(df['Close'])
            st.line_chart(df['Volume'])

