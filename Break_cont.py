#i = 0
#while True :  
#    if i+1 < 5 : 
#        i+=1
#        print(i)
#        continue
#    print(i)
#    i += 1
#    if i==45 :
#        break


#while True : 
#    n = int(input())
#    if n > 100 : 
#        print("Congrants")
#        break
#    else : 
#        print("Try again!!")
#        continue
    
    

                #EXERCISE 3
#GUESS THE NUMBER
n = 18
c = 0
for i in range(5) : 
    a = int(input())
    while 5-i-1 == 0 : 
        print("Game Over!!\n",0, "chances left" )
        break
    if a>18 : 
        print("Think Lower")
        print(5-i-1,"chances left")
        c += 1
        continue
    elif a<18 : 
        print("Think Greater")
        print(5-i-1,"chances left")
        c += 1
        continue
    else : 
        print("Congrants!! \n you got it in", c+1, "times")
        break



        