#6.1(to print the table of entered number)
#num = int(input())
#for i in range(1,11) : 
#    print(str(num)+ "X" + str(i)+"="+str(i*num))

#6.2 (program to greet all the persons names stored in a list)
#t = input("enter the greeting\n")
#l1=list(map(str,input().split()))
#l = len(l1)
#for i in range(l) : 
#    print(t +" "+ "To You"+" "+" "+l1[i])

#6.3 (program to greet persons whose name startswith as wish of user in a list)
#l = list(map(str,input().split()))
#c = input()
#for name in l : 
#    if name.startswith(c) : 
#        print("Hello" +" "+ name)

#6.4(program to print out table of a number using while loop)
#n = int(input())
#j=1
#i=10
#while j <= i : 
#    print(n*j)
#    j = j+1


#6.4(program to find whether a given number is prime or not)
n = int(input())
for i in range(2,n) : 
    if n%i != 0 : 
        p = "The given number is a prime number"
    else : 
        p = "The given number is not a prime number"
print(p)












