import yfinance as yf
import csv
msft = yf.Ticker("MSFT")

# get all stock info
print(msft.info)

# get historical market data
hist = msft.history(period="1mo",interval = "15m")
hist.to_csv('test.csv', index=True)
print(hist)