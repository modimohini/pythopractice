# tuple are order, unchangable, allows duplcate values and writtent in round brackets
mytuple = ("jam", "jelly", "bread and butter")

#changin tuple value
y = list(mytuple)
y[1] = "nutella"
mytuple = tuple(y)
print(mytuple)

# append in tuple
z = list(mytuple)
z.append("rose")
z.remove("jam")
mytuple = tuple(z)
print(mytuple)

#for loop
for x in mytuple:
    print (x)

# loop through indix numbers
for i in range(len(mytuple)):
    print(mytuple[i])

#while loop
a = 0
while a < len(mytuple):
    print(mytuple[a])
    a = a + 1

# count number of times it appers
x = mytuple.count("jelly")
print(x)

# index search for the occerance and returns its position 
x = mytuple.index("rose")
print(x)