import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt
from pykrx import stock
data = stock.get_market_ohlcv_by_date("20200101", "20230415", "005930")


# Get samsung Data from Yahoo
new_gs = data[data['거래량'] != 0]

# Moving average
ma5 = new_gs['종가'].rolling(window=5).mean()
ma20 = new_gs['종가'].rolling(window=20).mean()
ma60 = new_gs['종가'].rolling(window=60).mean()
ma120 = new_gs['종가'].rolling(window=120).mean()

# Insert columns
new_gs.insert(len(new_gs.columns), "MA5", ma5)
new_gs.insert(len(new_gs.columns), "MA20", ma20)
new_gs.insert(len(new_gs.columns), "MA60", ma60)
new_gs.insert(len(new_gs.columns), "MA120", ma120)

# Plot
plt.plot(new_gs.index, new_gs['종가'], label='종가')
plt.plot(new_gs.index, new_gs['MA5'], label='MA5')
plt.plot(new_gs.index, new_gs['MA20'], label='MA20')
plt.plot(new_gs.index, new_gs['MA60'], label='MA60')
plt.plot(new_gs.index, new_gs['MA120'], label='MA120')

plt.legend(loc="best")
plt.grid()
plt.show()