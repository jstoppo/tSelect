import os
import sys
import zipfile
import time
from com import mysqldb
#from time import time, strftime
import pandas as pd

import yfinance as yf

msft = yf.Ticker("MSFT")


# # get stock info
print(msft.recommendations)


# ric = "RELIANCE.NS"

#ric = "BEL.NS"

# data = msft.recommendations
# #data = yf.download(ric, start="2020-09-01", end="2020-09-21")
# print(data)