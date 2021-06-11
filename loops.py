# Simple > < = logic of greater than less than, and equal too
def my_simplefunction():
    a = int(input("a = "))
    b = int(input("b = "))

    if b > a: 
        print("b > a")
    elif a == b:
        print("==")
    else:
        print("a > b") 
# my_simplefunction()

# to print numbers from in asdending order  
def my_whileLoop():
    i = 1
    a = int(input("how many number you want, your val? "))
    while i <= a:
        print(i)
        i += 1 
        
# my_whileLoop()

# Print the pattern
def pattern():
    n = 5
    for i in range(0, n):
        for i in range(0, i+1):
            print('*', end = ' ')
        print('\r')
    
    for i in range(n,0,-1):
        for i in range(0,i-1):
            print('*', end=" ")
        print('\r')
# pattern()

# using while loop to print 10 number
def while_loop():
    num = 0
    while num <= 10:
        print(num)
        num += 1
# print pattern
def numberPattern():
    n = 6
    for i in range(1,n):
        for i in range(1, i+1):
            print(i, end= " ")
        print('\r')
#  sum of all number from 1 to a given number
""" num = input("Please provide given number: ")
num = 5
for x <= num:
    num + """


data = [[A,B], [E,B], [F,B], [B,D]]
"""        D
           |
           B
         /  | 
     #   A   E  F  """

def manager():
    for i in range(0,data):
        
        print(i)
   
manager()




