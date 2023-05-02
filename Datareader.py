
from pykrx import stock
data = stock.get_market_ohlcv_by_date("20200101","20230415","005930")
print(data)

import matplotlib.pyplot as plt

plt.plot(data['종가'])
plt.show()