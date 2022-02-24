#2.1 (WATERMELON)
#t = int(input())
#if t%2 == 0 : 
#    print("YES")
#else : 
#    print("NO")


#2.2 (A+B--PROBLEM)
#n = int(input())
#for i in range(n) : 
#    a,b = map(int, input().split())
#    print(a+b)

#2.3 (MAKE A TRIANGLE)
#a,b,c = map(int, input().split())
#if 1<=a<=100 and 1<=b<=100 and 1<=c<=100 : 
#    if a>b and a>c : 
#        p=a
#        q=b
#        r=c
#    elif b>a and b>c : 
#        p=b
#        q=c
#        r=a
#    else : 
#        p=c
#        q=a
#        r=b
#    count = p-(q+r)
#if count<0 : 
#    print("0")
#else : 
#    print(count+1)


#2.4 (DOMINO PILLING)   
#m,n = map(int, input().split())
#print((m*n)//2)



#3.1 (FROG JUMPING)
#n = int(input())
#for i in range(n) :  
#    a,b,k = map(int, input().split())
#    p=(k//2) 
#    if k%2 != 0 : 
#        print((a*(p+1))-(p*b))
#    else : 
#        print((p*a)-(p*b))


#3.2 (THE RANK)
#n = int(input())
#l = []
#for i in range(n) : 
#    a,b,c,d = map(int, (input().split()))
#    p = (a+b+c+d)
#    l.append(p)
#k = l[0]
#l.sort()
#l.reverse()
#r = l.index(k)
#print(r+1)

#3.3 (GOLDEN PLATE)
#sum = 0
#w,h,k = map(int, input().split()) 
#for i in range(k) : 
#    sum = sum + (2*(w+h-2))
#    w = w-4
#    h = h-4
#print(sum)

# BEAR AND BIG BROTHER
#a,b = map(int, input().split())   
#p = 0
#if 1<=a<=b<=10 : 
#    while a<=b : 
#        a=a*3
#        b=b*2
#        p+=1
#print(p)



#LABSHEET-4


#4.1 (CANDIES AND TWO SISTER)
#t = int(input())
#for i in range(t) : 
#    n = int(input())
#    a = ((n-1)//2)
#    print(a)

    
#4.2 (TEAM)
#n= int(input())
#r=0
#for i in range(n) : 
#    a,b,c = map(int, input().split())
#    if (a+b+c)>=2 : 
#        r+=1
#print(r)


#4.3 (DICE ROLLING)
#t = int(input())
#for i in range(t) : 
#    x = int(input())
#    print((x//7)+1)

#4.4 (ELEPHANT)
#n = int(input())
#if n%5 == 0 : 
#    print(n//5) 
#else : 
#    print((n//5)+1)

#4.5 (FAFA AND HIS COMPANY)
#n = int(input())
#r = 0
#for i in range(1,n,1) : 
#    if (n%i == 0) : 
#        r+=1
#print(r)

#4.6   (ELECTIONS)
#t = int(input())
#for i in range(t) : 
#    a,b,c = map(int, input().split())
#    if a>b and a>c : 
#        p=0
#        q=a-b+1
#        r=a-c+1
#    elif b>a and b>c : 
#        p=b-a+1
#        q=0
#        r=b-c+1
#    elif c>a and c>b : 
#       p=c-a+1
#       q=c-b+1
#       r=0
#    elif a==b and a!=c : 
#        p=a-b+1
#        q=0
#        r=a-c+1
#    elif a==c and a!=b: 
#        p=a-c+1
#        q=a-b+1
#        r=0
#    elif b==c and b!=a : 
#        p=b-a+1
#        q=b-c+1
#        r=0
#    else : 
#        p=1
#        q=1
#        r=1
#    print(p,q,r)


       
#LABSHEET-5 

#minimizing the string
l = int(input())
text = input()
f=0
p=""
for i in range(l-1) : 
    if text[i] > text[i+1] : 
        p = text[:i] + text[i+1]
        f=1
        break
if f==0 : 
    p = text[:l-1]
print(p)







