'''

Name : Dheeraj Mahanidhi Beerelly
Date: 08/10/2022
Course: ICT-4370-1
Week 9: DISCUSSION B - DATA ANALYTICS APPLIED TO THE STOCK PROBLEM


'''


import pandas as pd
import glob
import os
import matplotlib.pyplot as plt
import seaborn as sns


# Importing Stock data to DF

try:
    globbed_files = glob.glob("D:\Study\MS\Summer 22\Python\Data\*.csv") #creates a list of all csv files
    
    data = [] 
    
    for csv in globbed_files:
        frame = pd.read_csv(csv)
        frame['Symbol'] = os.path.basename(csv)
        data.append(frame)
        
        
    df = pd.concat(data, ignore_index=True) 
    
    #strip .,csv from stock name
    df['Symbol'] = df['Symbol'].str.rstrip('.csv')

except Exception as e:
            print("Error. Exception found: "+str(e))


#calculating the required data
try:
    
    df_mean_std = df.groupby(['Symbol']).agg({'Close':['mean','std']})
    print(df_mean_std)
    
    
    df_spy = df[df['Symbol'].str.contains("SPY")]
    
    
    df_corr_merged = pd.merge(df, df_spy, how='left', on=['Date'])
    
    
    df_corr_calculated = df_corr_merged.groupby(['Symbol_x']).Close_x.corr(df_corr_merged.Close_y)
    
    print(df_corr_calculated)


except Exception as e:
    print(e)

#ploting the line graph
figure ,ax= plt.subplots(figsize=(10,6))

for value,date in df.groupby(["Symbol"]):
    axis = date.plot(ax = ax, kind = 'line', x='Date', y= 'Close', label= value)
plt.legend(loc='upper left')
plt.xlabel("Date")
plt.ylabel("Closing Price")
plt.show()
