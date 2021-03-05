x = 11
def myadd(a):
    for x in range(1:5:1):
        a =+ 1
        if a >= 10:
            print(a, x)
        else:
            print("not yet " + format(a) + " " + format(x)) 
        return True

print(myadd(12))