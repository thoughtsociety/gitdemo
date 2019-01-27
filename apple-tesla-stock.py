# code_branch.py
# Demo program to show github branching
# This will be a branch of the Master code_base.py
# Retrieve stock data for 2018 for Apple Stock
# Change the stock ticker and make a new branch
# List the results in a dataframe dump
#

from datetime import datetime
import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like
import pandas_datareader.data as web 

# Set the date range fot all of 2018

start = datetime(2018, 1, 1)
end = datetime(2018,12,31)

# Fetch and print 10 days worth of stock prices from the IEX exchange API

ticker='AAPL'

# Read from IEX Public API for Apple stock

df = web.DataReader(ticker,'iex',start,end)
print("\n\tA Sample of Apple Stock Prices During 2018\n")
print(df.head(10))

# The branch includes Tesla stock as well

ticker='TSLA'
df = web.DataReader(ticker,'iex',start,end)
print("\n\tA Sample of Tesla Stock Prices During 2018\n")
print(df.head(10))
