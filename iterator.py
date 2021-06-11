# obj containing countable no of val, to traverse thrugh all the valuse, __iter__() and  __next__()

mydict = {
  "brand": "Ninja",
  "device type": "Ice-Mixer",
  "year": 1964,
  "year": 2021,  # dictionary cannot have two items with same key
  "year of make": 1964,
  "colors": ["red", "white", "blue"],
   "electric": False
}

myit = iter(mydict)
for x in myit:
    print(x)

# creating an iterator
class mynub: 
    def __iter__(self):
        self.a =1
        return self

    def __next__(self):
        if self.a <= 10:
            x = self.a
            self.a += 1
            return x
        else: 
            raise StopIteration
myclass =mynub()
newit = iter(myclass)

for x in myclass:
    print(x)

