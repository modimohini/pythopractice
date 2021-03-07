# this version of rps check for invlid input 
import random
select = ['r' , 'p' , 's']
comp = random.choice(select)

player1 = input("You type one from the list (r, p, s), tell me? " )


        def rpsfun():
   
            if player1 in select: 
                if comp == player1:
                    print (" it is draw and play again, play again")
                elif comp == 'p' and player1 == 's' :
                    print("player scissor win")
                elif comp == 's' and player1 == 'r' :
                    print("player rock win")
                elif comp == 'r' and player1 == 'p' :
                    print("player paper win")
                else:
                    print("comp win with " + comp)
            else:
                print("invalid input :( ")

    

            rpsfun()

print ("player1 input:  " + player1 + " and comp input: " + comp)
