'''
                    ----------------------------------Snake---Water---Gun----------------------------------
'''

import random
from traceback import print_tb
print("choose \n1 for Snake\n 2 for Water \n 3 for Gun")
opt = [1, 2, 3]
computer = random.choice(opt)
ur_trn = int(input("Choose your Number "))
print("Computer Choosed",computer)
c = computer

# while (True):
if (c == 1 and ur_trn == 2):
    print("You Won")
elif (c == 1 and ur_trn ==3):
    print("You Won")
elif (c == 2 and ur_trn ==1): 
    print("You Lost")
elif (c == 2 and ur_trn ==3):
    print("You Lost")
elif (c==3 and ur_trn ==1):
    print("You Won")
elif (c==3 and ur_trn ==2):
    print("You Won")
else : 
    print("Game tie")
    
    # print("enter 1 to replay or press 2 to exit")
    # p = int(input("enter 1 to replay or press 2 to exit"))
    # if p == 1 :
    #     continue
    # else : 
    #     break 
