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

