# check for balance parentheses
# scan from left to right -->if first symbole is closing 'unbalance' elif opening symbol 'push' it into stack 's' 
# if closing symbol  & top of the stack is opening symbol of sametype then 'pop'
# should end with empty list 


#expr = "[())]" #IndexError: list index out of range
#expr = "[([]{})]"  #balance
expr = "[([]{})]["  # unbalance

var = ['(','[','{'] 
s = [] #list 
l = len(s)

def balanceEx():
    for char in expr:
        if char in ['[', '{', '(']:
            s.append(char)     
            print(s)   
        elif char in [')'] or var[0] == s[l]:
            s.pop(l-1)
            print(s)
        elif char in [']'] or var[1] == s[l]:
            s.pop(l-1)
            print(s)
        elif char in ['}'] or var[2] == s[l]:
            s.pop(l-1)
            print(s)
        elif not s:
            print("balance")
        else:
            return False
        
                       
balanceEx()



if not s:
    print("balance")
else:
    print("not balance")

## by Mohini Modi
## 3/6/2021