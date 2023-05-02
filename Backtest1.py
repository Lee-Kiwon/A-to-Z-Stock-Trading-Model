import matplotlib.pyplot as plt
from pykrx import stock
import pandas as pd
import FinanceDataReader as fdr
import openpyxl
import backtrader
import backtrader as bt
import backtrader.feeds as btfeeds


#data = stock.get_market_ohlcv_by_date("20160101", "20230415", "005930")

data=fdr.DataReader('005930','2016-01-01','2023-04-21')
data.to_csv('005930.csv')

print(data)


plt.plot(data.index, data['Close'])
from datetime import datetime
#data.rename(columns={'시가':'Open','고가':'High','저가':'Low','종가':'Close','거래량':'Volume','거래대금':'money','등락률':'percentage'} , inplace=True)
#print(data)

#data.to_csv('Samsung.csv')

class customCSV(btfeeds.GenericCSVData):
    params =(
        ('format', '%Y-%m-%d'),
        ('datetime',0),
        ('time', 1),
        ('open',1),
        ('high',2),
        ('low',3),
        ('close',4),
        ('volume',5),
        ('openinterest', -1),
    )


# Create a subclass of Strategy to define the indicators and logic

class SmaCross(bt.Strategy):
        # list of parameters which are configurable for the strategy
        params = dict(
            pfast=10,  # period for the fast moving average
            pslow=30   # period for the slow moving average
        )

        def __init__(self):
            sma1 = bt.ind.SMA(period=self.p.pfast)  # fast moving average
            sma2 = bt.ind.SMA(period=self.p.pslow)  # slow moving average
            self.crossover = bt.ind.CrossOver(sma1, sma2)  # crossover signal

        def next(self):
            if not self.position:  # not in the market
                if self.crossover > 0:  # if fast crosses slow to the upside
                    self.buy()  # enter long

            elif self.crossover < 0:  # in the market & cross to the downside
                self.close()  # close long position

data = customCSV(dataname='005930.csv')

cerebro = bt.Cerebro()  # create a "Cerebro" engine instance


#data = pd.read_csv('Samsung.csv', index_col='날짜', parse_dates=True)


# Create a data feed
#data = bt.feeds.PandasData(dataname=data)
cerebro.adddata(data)  # Add the data feed
cerebro.broker.setcash(3000000)
cerebro.addstrategy(SmaCross)  # Add the trading strategy
back_init=cerebro.broker.getvalue()
cerebro.run()  # run it all
result = cerebro.broker.getvalue()