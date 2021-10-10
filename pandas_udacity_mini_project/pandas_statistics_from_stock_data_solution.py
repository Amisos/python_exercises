# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 12:49:08 2021

@author: MCanA
"""

# We import pandas into Python
import pandas as pd
import os

# We read in a stock data data file into a data frame and see what it looks like
google=pd.read_csv(os.path.dirname(__file__)+"\GOOG.csv");
apple=pd.read_csv(os.path.dirname(__file__)+"\AAPL.csv");
amazon=pd.read_csv(os.path.dirname(__file__)+"\AMZN.csv");
    

# We display the first 5 rows of the DataFrame
print(google.head())

#%%


# We load the Google stock data into a DataFrame
google_stock = google[["Date","Adj Close"]]
google_stock['Date']=pd.to_datetime(google_stock['Date'],format="%Y-%m-%d")
google_stock = google_stock.set_index(["Date"])

# We load the Apple stock data into a DataFrame
apple_stock = apple[["Date","Adj Close"]]
apple_stock['Date']=pd.to_datetime(apple_stock['Date'],format="%Y-%m-%d")
apple_stock = apple_stock.set_index(["Date"])
                       
# We load the Amazon stock data into a DataFrame
amazon_stock = amazon[["Date","Adj Close"]]
amazon_stock['Date']=pd.to_datetime(amazon_stock['Date'],format="%Y-%m-%d")
amazon_stock = amazon_stock.set_index(["Date"])

#%%

# We create calendar dates between '2000-01-01' and  '2016-12-31'
dates = pd.date_range('2000-01-01', '2016-12-31')

# We create and empty DataFrame that uses the above dates as indices
all_stocks = pd.DataFrame(index = dates)


# Change the Adj Close column label to Google
google_stock = google_stock.rename(columns={"Adj Close":"Google"})

# Change the Adj Close column label to Apple
apple_stock = apple_stock.rename(columns={"Adj Close":"Apple"})

# Change the Adj Close column label to Amazon
amazon_stock = amazon_stock.rename(columns={"Adj Close":"Amazon"})




print(google_stock)
print("------------------------------------")
print(apple_stock)

print(amazon_stock)

#%%


# We join the Google stock to all_stocks
all_stocks = all_stocks.join(google_stock)

# We join the Apple stock to all_stocks
all_stocks = all_stocks.join(apple_stock)

# We join the Amazon stock to all_stocks
all_stocks = all_stocks.join(amazon_stock)

print(all_stocks)

#%%


# Check if there are any NaN values in the all_stocks dataframe and delete these rows
all_stocks=all_stocks[all_stocks["Google"].notna() & all_stocks["Apple"].notna() &all_stocks["Amazon"].notna()]


print("------------------------------------")
print(all_stocks)

#%%

#after 150 row mean calculations done for every row
rollingMeanOfGoogle=all_stocks['Google'].rolling(150).mean()

#%%


# We import matplotlib into Python
import matplotlib.pyplot as plt

# We plot the Google stock data
plt.plot(all_stocks['Google'])

# We plot the rolling mean ontop of our Google stock data
plt.plot(rollingMeanOfGoogle)
plt.legend(['Google Stock Price', 'Rolling Mean'])
plt.show()















