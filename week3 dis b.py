'''

Name : Dheeraj Mahanidhi Beerelly
Date: 06/27/2022
Course: ICT-4370-1
Week 3
STOCK EARNINGS SUMMARY FOR MULTIPLE STOCK SYMBOLS USING DICTIONARIES


'''


#creating dictionaries for taking input

stockdata = {"stockList" : ['GOOGLE','MSFT','RDS-A','AIG','FB'],
             "noOfShares" : [25,85,400,235,130],
             "purchasePrice": [772.88,56.60,49.58,54.21,124.31],
             "currentValue" : [941.53,73.04,55.74,65.27,175.45] }




#calculating the earnings/loss

earningLoss = []
profitLoss = []
for i in range(len(stockdata["stockList"])):
    profitLoss.append(round((stockdata["currentValue"][i] - stockdata["purchasePrice"][i]), 2))
    earningLoss.append( profitLoss[i] * stockdata["noOfShares"][i])

#Printing the Header
print("Stock ownership for Bob Smith\n")
print("Stock\tShare#\tEarning\Loss\n")


#printing the report with formating

for i in range(len(stockdata["stockList"])):
    stockstr = stockdata["stockList"][i]
    noofsharesstr = stockdata["noOfShares"][i]
    print(f"{stockstr} \t{noofsharesstr} \t{earningLoss[i] : .2f}")


#to check if any of the stocks are increasing
maxmin=[]
condition = False
for i in range(len(stockdata["stockList"])):
    if profitLoss[i] >0:
        condition = True

#to display the highest increase or decrease stock
if condition:
    print("\nThe stock with the highest increase in value in your portfolio on a per share basis is",stockdata["stockList"][profitLoss.index(max(profitLoss))])
else:
    print("\nThe stock with the least decrease in value in your portfolio on a per share basis is",stockdata["stockList"][profitLoss.index(max(profitLoss))])





