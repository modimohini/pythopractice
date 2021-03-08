""" # insert sort
A[] --> set of numbers unsorted 
n[] =  len(A)-1 --> lenth of the array
i = 1 --> first index 
value = A[i]
hole = i

while (hole > 0 && A[hole-1] > ) 
and a[i-1] > value:                   
            a[hole] = a[hole-1]
            #print(a[hole])
            hole = hole - 1
            #print(hole)
    a[hole] = value   
    print(a[hole])   
    print(a)      """

a = ['9','1', '3','7']

def insertsort():
    for index in range(1,len(a)):
        value = a[index]    # value = a[1] --> value = 1
        i = index - 1       # i = 1 - 1 --> i = 0        
        while i >= 0:
            if value < a[i]:    # value < a[i] --> 1 < a[0] --> 1 < 9 
                a[i+1] = a[i]   # a[1] = a[0]    --> a[1] = 9  --> shift number in slot 'i' right to slot 'i+1'
                print(a)        # [9,9] 
                a[i] = value    # a[0] = 1                     --> shift value left into slot i
                print(a)        # [1,9]
                i = i - 1
                print(i)
            else:
                break 
    
insertsort()
 



