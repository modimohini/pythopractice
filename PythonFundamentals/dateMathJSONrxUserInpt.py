import datetime 
a = datetime.datetime.now()
print(a, a.year, a.strftime("%A"), a.strftime("%b"))

x = datetime.datetime(2021, 2 , 21)
print(x)

##
import json

# RegEX/regular expression to check strin containtsthe specific pattern 
import re
file = "it is 30 degree ceil, sunny day in here. how is the weather at your place? I hope it is not too cold"
x = re.search("^it.*here$",file)
if x:
    print("yes! we got match")
else:
    print("nope!")

y = re.search(r"\bs\w+", file) #Search for an lower case "s" character in the beginning of a word, and print the word
print(y.group())

y = re.findall("a|day", file)
z = re.findall("[l-s]",file) #Find all lower case characters alphabetically between l-s
x = re.findall("\d", file) #Find all digit characters:
print(y)
print(z)
print(x)

x = re.split("\s", file, 2) # split the string at first two while-stpace
z = re.split("\s", file) # to split the string at whitespace char
print(x)
print(z)

# to replace whilespace with the digit 
x = re.sub("\s", "1", file, 3)
print(x)