# Simple > < = logic
def my_simplefunction():
    a = int(input("a = "))
    b = int(input("b = "))

    if b > a: 
        print("b > a")
    elif a == b:
        print("==")
    else:
        print("a > b") 

 # to print

 
def my_whileLoop():
    i = 1
    a = int(input("how many number you want, your val? "))
    while i <= a:
        print(i)
        i += 1 
        
my_whileLoop()


