mylist = ["paint", "red", "green", "Blur", "butter", "chips"]
print('\n my list: ' + format(mylist) + '\n')

print("the length of items: " + format(len(mylist)) + '\n') 

print("data type of the list " + format(type(mylist)) + '\n')

newlist = list(("pan", "knife", "butter", "chips"))
print("Using list as constructor () " + format(newlist))

print('\n' + "Using list as constructor () " + format((newlist[2], newlist[-1])))

print (mylist[-2], mylist[1], mylist[:3], mylist[3:])

if "chips" in mylist:
    print("I got 'chips' in snacks")

# change item value 
mylist[-1] = "jam"
print(mylist)

#changing the range of item 
mylist [:2] = ["jelly", "fish"]
print(mylist)

#insert
mylist.insert(2, "Veggi")
print(mylist)

#add item end of list append
mylist.append("pare")
print(mylist)

# to extend the list 
mylist.extend(newlist)
print(mylist)

# remove specificitem and pop(), del[] specific index
mylist.remove("fish")
mylist.pop(0)
del mylist[-2]
print (mylist)

#loop
for x in  range(len(newlist)):
    print(newlist[x])

# # loop for
[print(x) for x in mylist]

# all p in one list with for look
allPlist = []
for x in mylist:
    if 'p' in x:
        allPlist.append(x)
print(allPlist)

# similarly in one line 

allPlist = [x for x in mylist if 'i' in x]
print(allPlist)

# sort list
mylist.sort(key = str.lower)
print(mylist)

m = len(mylist)
print(m)

i = mylist.index("pan")
print(i)