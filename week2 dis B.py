
'''

Name : Dheeraj Mahanidhi Beerelly
Date: 07/06/2022
Course: ICT-4370-1
Displaying Dog names and weights also finding the heaviest dog, and calculating the expected weights after 1 and 2 years


'''

 

#function to calculate expected weight after 1 and 2 years
def weightgain(dogWeight,year1,year2):
    for i in range(len(dogName)):
        year1.append(dogWeight[i]+(dogWeight[i]*0.15))
        year2.append(year1[i] + (year1[i]*0.10))
    
#calling the function
weightgain(dogWeight,year1,year2)


#displaying the header and formating the output
print("-"*55)
print("Dogs and their weights in lbs: ")
print("-"*55)
print("Name\tCurrent Weight\tExpected 1 Year\tExpected 2 Years")

#printing all the dognames, their respective weights, and expected weights
for i in range(len(dogName)):
    print("-"*55)
    print(f"{dogName[i]} \t {dogWeight[i] : .2f} \t {year1[i] : .2f} \t {year2[i] : .2f}")
    

#displaying the heaviest dog
print("-"*55)
heaviest = dogName[dogWeight.index(max(dogWeight))]
print("\nThe heaviest dog of the bunch is ",heaviest)
