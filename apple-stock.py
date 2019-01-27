# code_base.py
# Demo program to show github branching
# This will be the Master code_base.py
# Retrieve stock data for 2018 for Apple Stock
# Change the stock ticker and make a new branch
# List the results in a dataframe dump
#

from datetime import datetime
import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like
import pandas_datareader.data as web

# Fetch and print 10 days worth of stock prices from the IEX exchange API

start = datetime(2018, 1, 1)
end = datetime(2018,12,31)

# The master just has AAPL Stock

ticker='AAPL'
df = web.DataReader(ticker,'iex',start,end)
print("\n\tA Sample of Apple Stock Prices During 2018\n")
print(df.head(10))
