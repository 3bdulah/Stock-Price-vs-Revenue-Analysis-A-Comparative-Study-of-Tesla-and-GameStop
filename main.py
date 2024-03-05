import yfinance as yf
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import pandas as pd

tesla_data = yf.download("TSLA")
tesla_data.reset_index(inplace=True)
tesla_data.to_csv('tesla_stock_data.csv', index=False)
print(tesla_data.head())

gme_data = yf.download("GME")
gme_data.reset_index(inplace=True)
gme_data.to_csv('gme_stock_data.csv', index=False)
print(gme_data.head())

def make_graph(data, title):
    plt.figure(figsize=(10, 5))
    plt.plot(data['Date'], data['Close'], label='Tesla Stock Price', color='blue')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title(title)
    plt.legend()
    plt.show()

make_graph(tesla_data, 'Tesla Stock Price')
