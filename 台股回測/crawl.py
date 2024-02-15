
import twstock
import pandas
from twstock import analytics
import matplotlib.pyplot as plt



STOCK_CODE = '00757'
stock = twstock.Stock(STOCK_CODE)
print(stock.sid)
data = stock.fetch_from(2015, 5)
print(data)

close_price = [i.close for i in data]
avg20 = [0 for i in range(140)] + stock.moving_average(close_price, 140)
avg5 = [0 for i in range(35)] + stock.moving_average(close_price, 35)

plt.plot(avg20)
plt.plot(avg5)
plt.show()


