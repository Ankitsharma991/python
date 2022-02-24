        # ELECTIONS
#t = int(input())
#for i in range(t) : 
#    a,b,c = map(int,input().split())
#    if a==b==c== 0 : 
#        a1=1
#        b1=1
#        c1=1
#    elif (a==b==c) : 
#        a1=a+1
#        b1=b+1
#        c1=c+1
#    elif a>b and a>c : 
#        b1 = (a-b)+1
#        c1 = (a-c)+1
#        a1 = 0
#    elif b>a and b>c : 
#        a1 = (b-a)+1
#        c1 = (b-c)+1
#        b1=0
#    elif c>a and c>b : 
#        a1 = (c-a)+1
#        b1 = (c-b)+1
#        c1 = 0
#    elif a==b and a!=c : 
#        c1=()
#    print(a, b, c)


#n = int(input())
#a1 = 0
#b1 = 0
#c1 = 0
#for i in range(n):
#    a, b, c = map(int, input().split())
#    if a>b and a>c :
#        a1=0
#        b1=(a-b)+1
#        c1=(a-c)+1
#        if a==b and a!=c : 
#                a1=(a-b)+1
#                b1=a1
#                c1=(a-c)+1
#    elif b>a and b>c :
#        a1=(b-a)+1
#        b1=0
#        c1=(b-c)+1
#        if a==c and a!=b : 
#                a1=(a-c)+1
#                b1=(a-b)+1
#                c1=a1
#    elif c>a and c>b :
#        a1=(c-a)+1
#        b1=(c-b)+1
#        c1=0
#        if b==c and b!=a : 
#                a1=(b-a)+1
#                b1=(b-c)+1
#                c1=b1
#    else:
#        a1, b1, c1 = 1, 1, 1
#    print(a1, b1, c1)











       
             #TEAMS
#n = int(input())
#for i in range(n) : 
#    p,v,t = map(int,input().split())
#    c=0
#    if (p==1)and(v==1) or (v==1)and(t==1) or (p==1)and(t==1): 
#        sum = p+v+t
#    if (sum>=2) : 
#         c = c+1
#    print(c)
#


#n = int(input())
#c = 0
#for x in range(n) : 
#    p,v,t = map(int,input().split()) 
#    s = p+v+t 
#    if s.count('1') >= 2 : 
#        c = c + 1
#print(c)





















   
                  # CANDIES AND TWO SISTERS
#n=int(input())
#for i in range(n) : 
#    y=int(input())
#    w=((y-1)//2)
#    print(w)







                    # FAFA AND HIS COMPANY
#n=int(input())
#t=0
#for i in range(1,n) : 
#    if (n%i == 0 ) : 
#        t = t + 1 
#print(t)


                    # ELEPHANT 
#x=int(input())
#if (x/5 == 0) : 
#    t = x//5 
#else : 
#    t = (x//5)+1
#print(t)

                    # DICE ROLLING
t=int(input())
for i in range(t) : 
    d=int(input())
    p = (d//7)+1
    print(p)



    
