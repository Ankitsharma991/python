#f = open("An.txt", "w")
#a=f.write("Ankit Bhai Axe hain\n")
#f.write("Ankit Bhai Axe hain\n")
#f.write("Ankit Bhai Axe hain\n")
#print(a)
#f.close()


            # HANDLE READ AND WRITE
#f = open("An.txt", "r+")
#f.write("Thank you")
#print(f.read())
#f.close()



                                        # EXERCISE 4 (ASTROLOGER STARS)
#Pattern printing
n = int(input())
b = bool(input()) 
if b==True:
    i = 0
    while i<n : 
        print(i*"*")
        i+=1
elif b == False:
    j = n-1
    while j > 0 : 
        print(j*"*")
        j = j-1
else : 
    print("invalid input")




