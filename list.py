lista = ['1','2','3']
listb =  ['12','22','23']

listb = lista
print(lista,listb)


""" print("hello how are you")
name = input("what is ur name?")
print(id(name))
age = input("what is ur age?")
print ("ur name is", name, "and age is", age, sep=" : ", end = " .") 
print(id(name))

a = name.lower()
print(a)
b = name.upper()
print(b)
c = name.capitalize() 
print(c)
d = len(name)
print(d) """

my_list = ['1', 'hello', '3', 4, 6]
my_list.insert(0, 'new')
print(my_list)

e = list(reversed(my_list))
print(e)

num_list = [5,7,3,5]
f = sorted(num_list)
print(f)

# Nested List
matrix_list = [[1 , 2, 3], [6, 4, 9]]
row_count = len(matrix_list)
column_count = len(matrix_list[0])
print(row_count)
print(column_count)
print(matrix_list[1][2])

# Dictionaries {key : value} 
dic0 = {'hum': 30, 'jum': 'gum'}
dict1 = dict(Jim=20, jon =89, lill = "billi")
dic2  = dict([('hum', 30), ('jum', 'gum')])
print(dict1)
print(dic0)
print(dic0.keys())
print(dic0.values())
g = dic0.items()
print(g, dic0.values())