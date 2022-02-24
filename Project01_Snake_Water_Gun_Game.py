import random
# Snake , Water or Scissors game or Rock Paper scissors Game 
def gameWin(comp, you) :
    # if two values are equal , declare a tie!
    if you == comp : 
        return None 
        # check for all possibilities when computer choose "s"
    elif comp == "s" : 
        if you == "w" : 
            return False
        elif you == 'g' : 
            return True  
            # check for all possibilities when computer choose "w"      
    elif comp=='w' : 
        if you == 'g' : 
            return False 
        elif you == 's' : 
            return True 
            # check for all possibiloties when computer choose "g"
    elif comp == 'g' : 
        if you == 's' : 
            return False
        elif you == 'w' : 
            return True
you = input("Your turn : Snake(s) Water(w) or Gun(g) \n" )

print("Computer turn : Snake(s) Water(w) or Gun(g)? \n")
randNo = random.randint(1, 3)
print(randNo)
if randNo == 1 : 
    comp = 's'
elif randNo == 2 : 
    comp = 'w'
else : 
    comp = 'g'


a = gameWin(comp, you)
gameWin(comp, you)
if a== None : 
    print("The game is a tie")
elif a==True : 
    print("You Won")
else : 
    print("You lost")


