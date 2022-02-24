#n=int(input())
#for i in range(n) :
#    a,b=map(int,input().split())
#    p=((n*a)-((n-1)*b))
#print(p)


# program to check out whether entered number is palindrome or not 
n = input()
p = len(n)
for i in range(0,p,1) : 
    if (n[i] !=  n[-i-1]) : 
        result = False 
    else : 
        result = True 
print(result)







