'''

Name : Dheeraj Mahanidhi Beerelly
Date: 06/21/2022
Course: ICT-4370-1
Week 2: PROGRAMMING ASSIGNMENT
STOCK EARNINGS SUMMARY FOR MULTIPLE STOCK SYMBOLS


'''


#creating four lists for taking input

stockList = ['GOOGLE','MSFT','RDS-A','AIG','FB']
noOfShares = [25,85,400,235,130]
purchasePrice = [772.88,56.60,49.58,54.21,124.31]
currentValue = [941.53,73.04,55.74,65.27,175.45]


#calculating the earnings/loss

earningLoss = []
profitLoss = []
for i in range(len(stockList)):
    profitLoss.append(round((currentValue[i] - purchasePrice[i]), 2))
    earningLoss.append( profitLoss[i] * noOfShares[i])

#Printing the Header
print("Stock ownership for Bob Smith\n")
print("Stock\tShare#\tEarning\Loss\n")


#printing the report with formating
for i in range(len(stockList)):
    print(f"{stockList[i]} \t{noOfShares[i]} \t{earningLoss[i] : .2f}")


#to check if any of the stocks are increasing
maxmin=[]
condition = False
for i in range(len(stockList)):
    if profitLoss[i] >0:
        condition = True

#to display the highest increase or decrease stock
if condition:
    print("\nThe stock with the highest increase in value in your portfolio on a per share basis is",stockList[profitLoss.index(max(profitLoss))])
else:
    print("\nThe stock with the least decrease in value in your portfolio on a per share basis is",stockList[profitLoss.index(max(profitLoss))])





