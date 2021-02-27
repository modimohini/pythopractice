# set collection which is unordered, unindexed, unchangable 
myset = {"hulk", "butter", "chips", "CPU"}
workset = {"CPU", "laptop", "mouse"}
print (len(myset))
print(type(myset))
#to check if item exist in the set
print("banana" in myset)

# loop 
for x in myset:
    print(x)

# Add items
myset.add("lemon")
print(myset)

#Add sets
myset.update(workset)
print(myset)

# remove item , discard item, pop() --> will remove any random val
myset.remove("chips")
myset.discard("butter")
x = myset.pop()
print(myset)

""" # union and update excludes duplicate
y = myset.union(workset)
print(y)

myset.update(workset)
print(myset) """

# intersection_update() method will keep smame items in the set
myset.intersection_update(workset)
print(myset)

