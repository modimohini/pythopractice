""" # comp = computer randomly selecting r | p | s
# player = player input r1 | p1 | s1
case 1 : r == r1 | p == p1 | s == s1 --> result --> draw and play again 

case 2 :    r and p1    --> p1 player win
            p and s1    --> s1 player win
            s and r1    --> r1 player win --> result --> you are awesome! you win

case 3 :    s and p1    --> s  comp win
            r and s1    --> r  comp win
            p and r1    --> p  comp win --> result --> computer wins  """




# -random letter generator-
import random
select = ['r' , 'p' , 's']
comp = random.choice(select)

player1 = input("You type one from the list (r, p, s), tell me? " )


def rpsfun():
    if player1 in select: 
        if comp == player1:
            print (" it is draw and play again, play again")
        elif comp == ['p'] and player1 == ['s'] or player1 == ['s'] and comp == ['p'] :
            print("player scissor win")
        elif comp == ['s'] and player1 == ['r'] or player1 == ['r'] and comp == ['s'] :
            print("player rock win")
        elif comp == ['r'] and player1 == ['p'] or player1 == ['p'] and comp == ['r'] :
            print("player paper win")
        else:
            print("comp win with " + comp)
    else:
        print("invalid")

rpsfun()

print ("player1 input:  " + player1)
print ("comp input: " + comp)


