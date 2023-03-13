#A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
s={
    "brand":"ford",
    "model":"mustang",
    "year":1954
}
print(s)
#accessing item
print(s["brand"])
#Duplicate values will overwrite existing values
s={
    "brand":"ford",
    "model":"mustang",
    "year":1964,
    "year":2020
}
print(s)
#Dictionary Length
print(len(s))
#Get Keys
x=s.keys()
print(x)
#Get Values
x=s.values()
print(x)
#add a new item to the original dictionary, and see that the values list gets updated as well
s={
    "brand":"ford",
    "model":"mustang",
    "year":1964,
    "year":2020
}
x=s.values()
print(x)
s["color"]="red"
print(x)
#Get Itmes
x=s.items()
print(x)
#Check if Key Exists
s = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in s:
    print("YES")
#Update the "year" of the car by using the update() method
s = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
s.update({"year": 2020})
print(s)
#Add a color item to the dictionary by using the update() method
s = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
s.update({"color": "red"})
print(s)
#The pop() method removes the item with the specified key name
s = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
s.pop("model")
print(s)
"""The popitem() method removes the last inserted item if no key name specified"""
#The del keyword removes the item with the specified key name
s = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del s["model"] # if we call del s then it delete the dict completely
print(s)
#The clear() method empties the dictionary
s = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
s.clear()
print(s)
#Make a copy of a dictionary with the copy() method
s = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = s.copy()#x = dict(s) using dict function for copying
print(x)
#Nested Dictionaries
"""Create a dictionary that contain three dictionaries"""
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily)
#Create three dictionaries, then create one dictionary that will contain the other three dictionaries
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
print(myfamily)
#Print the name of child 2
print(myfamily["child2"]["name"])
