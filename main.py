import yfinance as yf
from bs4 import BeautifulSoup
import re
import streamlit as st
import requests
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

today = datetime.today().strftime('%Y-%m-%d')
tickerSymbol = st.text_input('Enter the stock ticker(e.g: "GOOGL","APPL","TSLA")', 'GOOGL')
tickerSymbol = tickerSymbol.upper()
tickerData = yf.Ticker(tickerSymbol)

r = requests.get(f'https://finance.yahoo.com/quote/{tickerSymbol}?p={tickerSymbol}&.tsrc=fin-srch')
soup = BeautifulSoup(r.content,"html.parser")
title = soup.find_all('title')
company = re.findall(r'>(.*\))', str(title))

st.write(f'''
  # Stock Price Dashboard

  Below are the **closing price** and **volume** of {company[0]}.
  
  ''')

ticker_df = tickerData.history(period='1d', start='2010-5-31', end=today)

st.write('## The Closing Price')
st.write('(drag to move around. scroll to zoom, double click to reset)')
st.line_chart(ticker_df.Close)

st.write('## The Volume')
st.write('(drag to move around. scroll to zoom, double click to reset)')
st.line_chart(ticker_df.Volume)