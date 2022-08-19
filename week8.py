'''

Name : Dheeraj Mahanidhi Beerelly
Date: 08/03/2022
Course: ICT-4370-1
Week 8: PROGRAMMING ASSIGNMENT
STOCKS WITH DATABASES AND DATA VISUALIZATION


'''



#importing all required libraries
import json
import pandas as pd
from datetime import datetime
import time
from matplotlib.dates import DateFormatter
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import datetime as dt

# used pandas to read csv file
data = pd.read_csv (r'D:\Study\MS\Summer 22\Python\Lesson6_Data_Stocks.csv')   
df = pd.DataFrame(data, columns= ['SYMBOL','NO_SHARES'])


# reading json file 
file_path= 'D:\Study\MS\Summer 22\Python\AllStocks.json'
with open(file_path) as x:
    y = json.load(x)
    
#creating shares class
class shares:
    def __int__(self,noshares, stockName):
        self.noshares=noshares
        self.stockName = stockName

#creating stock class
class stock:
    def __init__(self,Symbol,Date,Open,High,Low,Close,Volume):
        self.Symbol=Symbol
        self.Date=Date
        self.open=Open
        self.high=High
        self.Low=Low
        self.Close=Close
        self.Volume=Volume
        
    def add_newstock(self,closingprice):
        self.closingprice=closingprice

    def calclosingprice(self, noshares):
        closep = round ((int (self.Close)) * int (noshares),2)
        return closep


#dictionary to get the json data
Dictionary=[]
for s in y:
        if s['Symbol'].upper() not in Dictionary: 
            Dictionary.append(stock(s['Symbol'], s['Date'],s['Open'], s['High'], s['Low'], s['Close'], s['Volume']))            

#PLOTTING THE GRAPH
plot = {}
for stock in Dictionary:
    stock.add_newstock(stock.calclosingprice(df.loc[df['SYMBOL'] == stock.Symbol, 'NO_SHARES'].iloc[0]))
    if stock.Symbol.upper() not in plot:
        plot[stock.Symbol.upper()]=[]
    plot[stock.Symbol.upper()].append([datetime.strptime(stock.Date, '%d-%b-%y').strftime('%d-%m-%y'),stock.closingprice])
#print(plot)
count=0
fig, ax = plt.subplots()

ax.xaxis.set_major_locator(mdates.WeekdayLocator(interval=11))
ax.xaxis.set_tick_params(rotation = 80) 
left = dt.date(2015, 11, 9)
right = dt.date(2018,11,10)
plt.gca().set_xbound(left,right)
for index, row in df.iterrows():
    xAxis = [value[0] for value in plot[row[0]]]
    yAxis = [value[1] for value in plot[row[0]]]
    ax.plot(xAxis,yAxis,)
    count=count+1
 
plt.xlabel('date')# PRINTS x-LABEL ATTRIBUTE NAME
plt.gca().invert_xaxis()
plt.ylabel('volume')# PRINTS Y-LABEL ATTRIBUTE NAME
ax.legend(list(df.SYMBOL))# PRINTS SYMBOL NAMES ON GRAPH
plt.show()
plt.savefig('D:\Study\MS\Summer 22\Python\simplePlot.png')

