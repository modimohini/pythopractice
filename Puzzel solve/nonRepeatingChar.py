# to repeat non-repeating char

a = "aaaaabcbd"

def firstNonRepeating():
    seen = []
    repeat = []

    for char in a:
        if char not in seen:                
            seen.append(char)     
           
        elif repeat.append(char):
            break
            

    x = seen.copy()
    y = repeat.copy()

    x1 = set(x)
    y1 = set(y)    

    z = x1.difference(y1)
    print(z)

        
firstNonRepeating()

