"""Python Counter takes in input a list, tuple, dictionary, string, which are all iterable objects, and it will give you output that will have the count of each element."""


from collections import Counter
list1 = ['x','y','z','x','x','x','y', 'z']   # list 
print(Counter(list1))


my_str = "count this string!"  # string
print(Counter(my_str))

print(Counter(['x','y','z','x','x','x','y', 'z'])) #using list
print(Counter({'x': 4, 'y': 2, 'z': 2})) #using dictionary
print(Counter(('x','y','z','x','x','x','y', 'z'))) #using tuple


words_list = ['Cat', 'Dog', 'Horse', 'Dog']
counter = Counter(words_list)
print(counter) > out.txt

print(Counter(words_list))