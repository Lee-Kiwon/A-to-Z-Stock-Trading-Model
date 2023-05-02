import pandas as pd

from pykrx import stock
data = stock.get_market_ohlcv_by_date("20200101","20230415","005930")
print(data.tail())

ma5 = data['종가'].rolling(window=5).mean()

type(ma5)

ma5.tail(10)

data['거래량'] != 0

import matplotlib.pyplot as plt

new_data = data[data['거래량'] !=0]

ma20 = new_data['종가'].rolling(window=20).mean()

plt.plot(new_data['ma5'], label="ma5")