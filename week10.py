'''

Name : Dheeraj Mahanidhi Beerelly
Date: 08/03/2022
Course: ICT-4370-1
Week 10: PORTFOLIO PROGRAMMING ASSIGNMENT
IMPROVING THE STOCK PROBLEM WITH ADDITIONAL FUNCTIONALITY


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
import tkinter as tk

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 600, height = 400,  relief = 'raised')
canvas1.pack()

label1 = tk.Label(root, text='Get the Graph by uploading the csv file path')
label1.config(font=('helvetica', 14))
canvas1.create_window(300, 25, window=label1)

label2 = tk.Label(root, text='Enter the Path:')
label2.config(font=('helvetica', 10))
canvas1.create_window(300, 100, window=label2)

entry1 = tk.Entry (root) 
canvas1.create_window(300, 140, window=entry1)

def getGraph():
        x1 = entry1.get()


        try:
                data = pd.read_csv (x1)   
                df = pd.DataFrame(data, columns= ['SYMBOL','NO_SHARES'])

        except:
                print("Unable to read file")

	
        # reading json file 
        file_path= 'D:\Study\MS\Summer 22\Python\AllStocks.json'
        try:
                with open(file_path) as x:
                        y = json.load(x)
        except:
                print("file not read")
                label3 = tk.Label(root, text= 'Upload Correct File Path',font=('helvetica', 10))
                canvas1.create_window(300, 210, window=label3)
    
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
        try:
                
                
                for stock in Dictionary:
                    stock.add_newstock(stock.calclosingprice(df.loc[df['SYMBOL'] == stock.Symbol, 'NO_SHARES'].iloc[0]))
                    if stock.Symbol.upper() not in plot:
                        plot[stock.Symbol.upper()]=[]
                    plot[stock.Symbol.upper()].append([datetime.strptime(stock.Date, '%d-%b-%y').strftime('%d-%m-%y'),stock.closingprice])
        except:
                print("Wrong File")
                label3 = tk.Label(root, text= 'Upload Correct File Path',font=('helvetica', 10))
                canvas1.create_window(300, 210, window=label3)
                

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
    
            #label4 = tk.Label(root, text= float(x1)**0.5,font=('helvetica', 10, 'bold'))
            #canvas1.create_window(200, 230, window=label4)
    
button1 = tk.Button(text='Submit', command=getGraph, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(300, 180, window=button1)


root.mainloop()
