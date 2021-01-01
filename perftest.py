from __future__ import print_function
import yfinance as yf
from datetime import datetime

start_time = datetime.now()
for ticker in ['MSFT', 'F', 'AAPL', 'NFLX']:
    t = yf.Ticker(ticker)
    info = t.short_info
    print(ticker, info['sector'], info['industry'])
time_elapsed = datetime.now() - start_time
print('Time elapsed {}'.format(time_elapsed))

print()
start_time = datetime.now()
for ticker in ['MSFT', 'F', 'AAPL', 'NFLX']:
    t = yf.Ticker(ticker)
    info = t.info
    print(ticker, info['sector'], info['industry'])
time_elapsed = datetime.now() - start_time
print('Time elapsed {}'.format(time_elapsed))
