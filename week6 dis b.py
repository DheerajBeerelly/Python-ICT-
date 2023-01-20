'''

Name : Dheeraj Mahanidhi Beerelly
Date: 07/20/2022
Course: ICT-4370-1
DISCUSSION B - POPULATE THE DATA STRUCTURE
Getting the input from csv file

'''
import csv


#creating dog class
class Dog:

    def __init__(self, dogName, dogWeight):
        self.dogName = dogName
        self.dogWeight = dogWeight

    #function to calculate expected weight after 1 and 2 years
    def weightgain(self):
        year1 = (self.dogWeight+(self.dogWeight*0.15))
        year2 = (year1 + (year1*0.10))
        return year1,year2
            
    

        
DogObj=[]

try:
    with open('D:\Study\MS\Summer 22\Python\Dogs_Week6.csv', mode ='r')as file:
        # reading the CSV file
        csvFile = csv.reader(file)
 
        # taking dog detials from csv file
        for lines in list(csvFile)[1:]:
            DogObj.append(Dog(lines[0],float(lines[1])))
            
except FileNotFoundError:
    print("file does not exist")
    


#displaying the header and formating the output
print("-"*55)
print("Dogs and their weights in lbs: ")
print("-"*55)
print("Name\tCurrent Weight\tExpected 1 Year\tExpected 2 Years")



heaviest=0
#calling the function to calculate the expected weights and printing all the dognames, their respective weights, and expected weights
for i in DogObj:
    
    year1,year2 = i.weightgain()
    print("-"*55)
    print(f"{i.dogName} \t {i.dogWeight : .2f} \t {year1 : .2f} \t {year2 : .2f}")

    #calculating the heaviest dog
    if heaviest < i.dogWeight:
        heaviest = i.dogWeight
        name = i.dogName

#displaing the heaviest dog
print("\nThe heaviest dog of the bunch is ",name)


    



















