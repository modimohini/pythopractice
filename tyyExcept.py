try:
    print("hi")
except NameError:
    print("an excepton ocured")
except:
    print("var not define")
else:
    print("all good")

# to opan and read the file 'r'
f = open("readme.md", "r")
print(f.read())

# to append 'a' to append and 'w' to over write
f = open("test.txt","w")
f.write("some work stuff!")
f.close()
#open and read the file after the appending:
f = open("test.txt", "r")
print(f.read())

# to delete file os.remove() function 
import os
if os.path.exists("test.txt"):
    os.remove("test.txt")
else:
    print("file does not exist")

