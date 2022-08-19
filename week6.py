'''

Name : Dheeraj Mahanidhi Beerelly
Date: 07/21/2022
Course: ICT-4370-1
Week 6: PROGRAMMING ASSIGNMENT - STOCK PROBLEM WITH OBJECTS AND FILES


'''


#importing datetime library, csv, sys
from datetime import date, datetime
import csv
import sys






#creating a class for the stocks
class Stock:
    def __init__(self, stockName, noOfShare, purchasePrice, currentPrice, purchaseDate, stockId):
               
        self.stockName = stockName
        self.noOfShare = noOfShare
        self.purchasePrice = purchasePrice
        self.currentPrice = currentPrice
        self.purchaseDate = purchaseDate
        self.stockId = stockId
        
#function to get the number of years to calculate the yearly profit or loss
    def getDaysDifference (self):
        d1 = date.today ()
        d2 = self.purchaseDate 
        d2Format = date.fromisoformat (d2) 
        daysBetween = ((d1 - d2Format).days)/ 365.25
        return daysBetween

#function to calculate the total loss or profit
    def calcLossOrGain (self):
        earningLoss = round ((float (self.currentPrice) - float (self.purchasePrice)) *
                             float (self.noOfShare),2)
        return earningLoss

#function to calculate Earning per share
    def calcEarningPerShare (self):
        perShareEarning = round (float (Stock.findLossOrGain (self)) /
                                 float (self.noOfShare),2)
        return perShareEarning
    
#function to calculate the Yield
    def calcYield (self):
        yieldValue = round (((((float (self.currentPrice) -
        float (self.purchasePrice)) /float (self.purchasePrice)))) * 4)
        return yieldValue

#function to calculate the total yearly earning or loss till today
    def calcEarnLossRate (self):
        earningRate = round ((((((self.currentPrice) -
        float (self.purchasePrice)) /float (self.purchasePrice))
                        /(float (Stock.getDaysDifference(self))))* 100), 4)
        return earningRate

#function to print the bond information
    def printBondData (self):
        print ((str (self.stockName)), (str (self.noOfShare)), ("$" + str (self.purchasePrice)), ("$" + str (self.currentPrice)), (self.purchaseDate), (self.stockId),
         (str (self.coupon)), (str (self.yieldValue * 100) + "%"),sep='\t\t',end="\n")

#function to print the bond table header
    def printBondHeader ():
        print ("-" * 125)
        print ('\t\t\t\tBond Ownership for Bob Smith')
        print ("-" * 125)
        print ('Bond\t\tShare#\t\tPurchase Price\tCurrent Price\tPurchase Date\t\tStockId\t\tCoupon\t\tYield')
        print ("-" * 125)

#function to print the stock table header
    def stockTablesHeader():
        print("\n")
        print ("-" * 75)
        print ('\nStock \t\tShare# \t\tEarnings/Loss \tYearly Earning/Loss') 
        print ("-" * 75)
        

#function to print the stock table information
    def printStockValues (self):
        print('-' *70)
        print (f"{(str (self.stockName))}\t\t{(str (self.noOfShare))}\t\t{ (Stock.calcLossOrGain (self)) : .2f}\t\t {( (Stock.calcEarnLossRate (self))):.2f}") 
        print('-' *70)


#creating the Bond Class for the bonds
class Bonds (Stock):
    def __init__ (self, name, share, purchase, current, pDate, stockId, coupon, yieldValue):
        super ().__init__ (name, share, purchase, current, pDate, stockId)
        self.coupon = coupon
        self.yieldValue = yieldValue

#function to store coupon info
    def getCoupon ():
        return self.coupon

#function to store yeild info
    def getYeildRate():
        return self.yieldValue
        print ("-" * 125)


#creating the investor class
class Investor (): 
 
    def __init__ (self, investorID, address, contactNumber): 
        self.investorID = investorID 
        self.address = address
        self.contactNumber = contactNumber

    def printInvestorHeader():
        print ("-" * 50)
        print ('investorID  \taddress \tcontactNumber')
        print ("-" * 50)

    def printInvestorData (self):
        print (self.investorID,self.address,self.contactNumber,sep= '\t')


#inputing all the stock information into the stock class
stocks = {}
dum=100
try:
    with open('D:\Study\MS\Summer 22\Python\Lesson6_Data_Stocks.csv', mode ='r')as file:
        # reading the CSV file
        csvFile = csv.reader(file)
 
        # taking dog detials from csv file
        for lines in list(csvFile)[1:]:
            try:
                stocks[lines[0]] = (Stock(lines[0], int(lines[1]), float(lines[2]), float(lines[3]), lines[4], dum))
                dum=dum+1
            except:
                print("incompatable values")
                
    file.close()
except FileNotFoundError:
    print("file does not exist")





#inputting the bond information to the bond class


bonds = []
try:
    with open('D:\Study\MS\Summer 22\Python\Lesson6_Data_Bonds.csv', mode ='r')as file1:
        # reading the CSV file
        csvFile = csv.reader(file1)
 
        # taking dog detials from csv file
        for lines in list(csvFile)[1:]:
            try:
                bonds.append( (Bonds(lines[0], int(lines[1]), float(lines[2]), float(lines[3]), lines[4],dum,float(lines[5]),float(lines[6]))))
                dum=dum+1
            except:
                print("incompatable values")
    file1.close()      
except FileNotFoundError:
    print("file does not exist")


try:
    out = open('D:\Study\MS\Summer 22\Python\output.txt','w')
    sys.stdout = out
except:
    print("failed to create output file")




print('\nBond Table')
#calling the funtion to printthe bond table header
Bonds.printBondHeader()

#calling the function to print bonds information
for i in range(len(bonds)):
    bonds[i].printBondData()
print('\n\n')
print('*'*125)

#calling the funtion to printthe bond table header
Stock.stockTablesHeader()

#calling the function to print stocks information
for key in stocks:
    stocks.get(key).printStockValues()
print('\n\n')
print('*'*125)

#inputting the investor information to the investor class
investors = []
investors.append(Investor (1, "S Way St, Aurora, CO", "720-921-9999"))
print('\n\nInvestor Table')

#calling the funtion to printthe bond table header
Investor.printInvestorHeader()

#calling the function to print investor details
for i in range(len(investors)):
    investors[i].printInvestorData()

out.close()
