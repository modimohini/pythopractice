""" [1,2,1,2,3,3]
[2,1,3,5,3,2]
[1,2,3,4,5,6]
to find first duplicate in the array """




def firstDup(a):
    seen = []

    for num in a: 
        if num in seen:
            print(num)  
            break
        else: 
            seen.append(num)
            print('-1')
            

a = [1,2,3,4,5,6]
firstDup(a)


    

