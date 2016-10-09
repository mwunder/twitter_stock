import pandas.io.data as web
from datetime import *
from sentiment.models import *
from sentiment_refs import * 

start = datetime(2016,1,1) # datetime.now() - timedelta(minutes=1440)
end = datetime.now() #(2016,10,7)


toupper = lambda s: s.upper()

stockDataYear = web.DataReader(map(toupper,symbols), 'yahoo', start, end).to_frame()

for i,row in stockDataYear.iterrows():
    day,symbol = row.name
    stock = Stock.objects.filter(symbol=symbol)
    if not stock: continue
    stock = stock[0]
    if Stock_price.objects.filter(stock=stock,trading_day=day): continue
    stock_p = Stock_price(stock=stock,trading_day=day,
        high_price = row.High,
        low_price = row.Low,
        open_price = row.Open,
        close_price = row.Close,
        volume = row.Volume)
    stock_p.save()





