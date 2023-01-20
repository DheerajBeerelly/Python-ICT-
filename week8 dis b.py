'''

Name : Dheeraj Mahanidhi Beerelly
Date: 08/3/2022
Course: ICT-4370-1
Week 8: DISCUSSION B - PYGAL EXPLORATION


'''




import json
import pygal


#loading the json object to python object
with open("D:\Study\MS\Summer 22\Python\dogWeights.json", "r") as read_it:
     data = json.load(read_it)


dogsweight={}
dogIDS=[]
max=0

#getting the data from the json and storing the weights for different years
for dog in data:
    #print(dog['DogID'])
    if dog['DogID'] not in dogIDS:
        dogIDS.append(dog['DogID'])
        dogsweight[dog['Dog']] = [dog['Weight']]
    else:
        dogsweight[dog['Dog']].append(dog['Weight'])

    if max < len(dogsweight[dog['Dog']]):
        max = len(dogsweight[dog['Dog']])
    

#making the empty values to null
for i in dogsweight.values():
    while len(i)<max:
        i.insert(0, None)

years = range(2007,2017)

#creating the line graph
graph = pygal.Line()
graph.title = 'Dogs Weight'

graph.x_labels = map(str,years)

#adding each dog to the line graph
for i in dogsweight:
    graph.add(i,dogsweight[i])

#saving the graph
graph.render_to_file('dog.svg')
