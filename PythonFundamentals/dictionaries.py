# Dictionary items are ordered,changable, not allow duplicates,items are presented in key:valuepairs
mydict = {
  "brand": "Ninja",
  "device type": "Ice-Mixer",
  "year": 1964,
  "year": 2021,  # dictionary cannot have two items with same key
  "year of make": 2021,
  "colors": ["red", "white", "blue"],
   "electric": False
}
print(mydict)
print(mydict["brand"]) 

print(len(mydict))
print(type(mydict))

# removing items pop, del, clear
mydict.pop("year")
del mydict["colors"]
print(mydict)
""" mydict.clear()
print(mydict) """

#loop 
for x in mydict:
  print(mydict[x])

# loop to give all values 
for x in mydict.values():
  print(x)

# loop to giveout all keys
for x in mydict.keys():
  print(x)

# loop out both key and values
for x, y in mydict.items():
  print(x,y)

# copy 
newdic = mydict.copy()
print(newdic)

# using buildin function to copy dictonary  'dict()' function
new2 = dict(mydict)
print(new2)

# nested dictionary 
parentdic = { 
  "ch1" : mydict,
  "ch2" : new2,
  "ch3" : newdic
}


