## program 1 watermelon
#w=int(input())
#if w%2==0 and w!=2 :
#    print("Yes")
#else :
#    print("No")
#
#
##program 2 A+B
#a=int(input())
#b=int(input())
#sum=a+b
#print(a+b)
#
#
##program 3 for triangle 
#a=int(input())
#b=int(input())
#c=int(input())
#if a+b>c and a+c>b and b+c>a :
#    print("0")
#elif a+b<=c : 
#    print(c-(a+b)+1)
#elif b+c<=a : 
#    print(a-(b+c)+1)
#else : 
#    print(b-(a+c)+1)
#

#program 4 for Domino pilling 
#l=int(input())
#b=int(input())
#A=l*b 
#print(A//2)

n=int(input())
for i in range(n) : 
    a,b,c=map(int,input().split())
    if a==0 and b==0 and c==0 : 
        a0=1
        b0=1
        c0=1
        print(a0, b0, c0)
    elif a>max(b,c) : 
        a1=0
        b1=(a-b)+1
        c1=(a-c)+1
        print(a1, b1, c1)
    elif b>max(a,c) : 
        a2=(b-a)+1
        b2=0
        c2=(b-c)+1
        print(a2, b2, c2)
    else : 
        a3=(c-a)+1
        b3=(c-b)+1
        c3=0
        print(a3, b3, c3)





