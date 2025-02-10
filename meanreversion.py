import backtrader as bt
from datetime import datetime

class MeanReversionStrategy(bt.Strategy):
   params = (('period', 30),)

   def __init__(self):
       self.sma = bt.indicators.SimpleMovingAverage(self.data.close, period=self.params.period)

   def next(self):
       if self.data.close[0] < self.sma[0]:
           self.buy(size=1)
       elif self.data.close[0] > self.sma[0]:
           self.sell(size=1)

if __name__ == '__main__':
   cerebro = bt.Cerebro()
   data = bt.feeds.YahooFinanceData(dataname='AAPL', fromdate=datetime(2010, 1, 1), todate=datetime(2020, 1, 1))
   cerebro.adddata(data)
   cerebro.addstrategy(MeanReversionStrategy)
   cerebro.run()
   cerebro.plot()
