import backtrader as bt
from datetime import datetime


class firstStrategy(bt.Strategy):

    def __init__(self):
        self.rsi = bt.indicators.RSI_SMA(self.data.close, period=21)

    def next(self):
        if not self.position:
            if self.rsi < 30:
                self.buy(size=100)
        else:
            if self.rsi > 70:
                self.sell(size=100)

import matplotlib.pyplot as plt
from pykrx import stock
import pandas as pd
import openpyxl
import backtrader

data = stock.get_market_ohlcv_by_date("20160101", "20230415", "005930")

print(data)


plt.plot(data.index, data['종가'])
from datetime import datetime
import backtrader as bt

data.rename(columns={'시가':'Open','고가':'High','저가':'Low','종가':'Close','거래량':'Volume','거래대금':'money','등락률':'percentage'} , inplace=True)
print(data)

data.to_csv('Samsung.csv')

data = pd.read_csv('Samsung.csv', index_col='날짜', parse_dates=True)


# Create a data feed
data = bt.feeds.PandasData(dataname=data)

# Variable for our starting cash
startcash = 10000

# Create an instance of cerebro
cerebro = bt.Cerebro()

# Add our strategy
cerebro.addstrategy(firstStrategy)


# Add the data to Cerebro
cerebro.adddata(data)

# Set our desired cash start
cerebro.broker.setcash(startcash)

# Run over everything
cerebro.run()

# Get final portfolio Value
portvalue = cerebro.broker.getvalue()
pnl = portvalue - startcash

# Print out the final result
print('Final Portfolio Value: ${}'.format(portvalue))
print('P/L: ${}'.format(pnl))

# Finally plot the end results
cerebro.plot(style='candlestick')