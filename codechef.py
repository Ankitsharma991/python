#t = int(input())
#for i in range(t) : 
#  n,k = map(int,input().split())
#  if n%k == 0 : 
#    print(n//k)
#  else : 
#    print((n//k)+1)




#t = int(input())
#for i in range(t) : 
#  a = ''
#  n = int(input())
#  for l in range(n) : 
#    p = int(input())
#    a = a + p 
#print(a)   


#t = int(input())
#for i in range(t) : 
#  t1 = int(input())
#  a = input()
#  b = input()
#  p = 0
#  for l in range(len(a)) : 
#    if a[i] != b[i] : 
#      p += 1
#print(p)



#a,b = int(input()),bool(input())
#print(a-b)

  
#t = int(input()) 
#for i in range(t) : 
#    p = 0
#    n = input()
#    for j in range(len(n)) : 
#        p = p + (int(n[j]))
#
#    print(p)
    
    
#t = int(input())
#for i in range(t) : 
#    a,b = map(int,input().split())
#    print(a%b)


#t = int(input())
#for i in range(t) : 
#    n = input()
#    print((int(n[0]))+(int(n[-1])))


#t = int(input())
#for i in range(t) : 
#    c = 0
#    n = input()
#    for j in range(len(n)) : 
#        if n[j] == '4' : 
#            c += 1
#    print(c)


#t = int(input())
#for i in range(t) : 
#    f = 1
#    n = int(input())
#    j=1
#    while j<=n : 
#        f = f*j 
#        j=j+1
#    print(f)
   
#t = int(input())
#for i in range(t) : 
#    a = ""
#    n = input()
#    l = len(n)
#    j = -1
#    while j<=(-l) : 
#        a += n[j]
#        j = j - 1
#    print(a)
     
#t = int(input())
#for i in range(t) : 
#    n = input()
#    p = len(n)
#    r = ""
#    for j in range(-1,-p-1,-1):
#        r += n[j]
#    print(int(r))

 #TSORT
#t = int(input()) 
#p = []
#for i in range(t) : 
#    a = list(input())
#    p = p + a
#p.sort()
#for j in range(t) : 
#    print(int(p[j]))

#SQUARE ROOT
#import math 
#n = int(input())
#for i in range(n) : 
#    a = int(input())
#    p=math.sqrt(a)
#    print(round(p))


#SECOND HIGHEST NUMBER
#n = int(input())
#for i in range(n) :
#    A,B,C = map(int, input().split())
#    if (A>B and A<C) or (A<B and A>C): 
#        result = A
#    elif (B>A and B<C) or (B<A and B>C) : 
#        result = B
#    else : 
#        result = C
#    print(result)



#n=int(input())
#a1=[]
#a2=[]
#a3=0
#a4=0
#b1=[]
#b2=[]
#b3=0
#b4=0
#for i in range(n) : 
#    A,B = map(int, input().split())
#    a1.append(A)
#    b1.append(B)
#    a3+=A
#    b3+=B
#    if A>B : 
#        a4+=1
#        a2.append(A-B)
#    if B>A : 
#        b4+=1
#        b2.append(B-A)
#if max(a2) > max(b2) : 
#    print("1",max(a2))
#else : 
#    print("2",max(b2))

    




#n=int(input())
#p = []
#q = []
#r = []
#s = []
#for i in range(n) : 
#    A,B = map(int, input().split())
#    p.append(A)
#    q.append(B)

#print(sum(p))
#print(sum(q))
#print(sum(p)-sum(q))

#if sum(p) > sum(q) : 
#    for j in range(n) :
#        if p[i] > q[i] : 
#            r.append(p)
#            break
#        #break
#        elif q[i] > p[i] : 
#            s.append(q[i])
#            break
        #break





            
    





#l = list(map(int,input().split())) 
#l.sort()
#print(l[-2])



#police recuit
#n = int(input())
#l = list(map(int, input().split()))
#r = 0
#for i in range(len(l)) : 
    
#good number



#coins
#n,s = map(int, input().split())
#if s%n == 0 :
#    print(s/n)
#else : 
#    print((s//n)+1)
    
# in search of an easy problem
#n = int(input())
#l = list(map(int, input().split()))
#c = 0
#for i in range(len(l)) : 
#    if l[i] == 1 : 
#        c += 1
#if c>=1 : 
#    print("HARD")
#else : 
#    print("EASY")

#GOOD NUMBERS
#n, k = map(int, input().split())
#c = 0
#d = []
#for j in range(k+1) : 
#    d.append(j)
#for i in range(n) : 
#    a = int(input()) 
#    for i in range(len(str(a))) : 
#        if int(a[i]) in d : 
#            c += 0
#print(c)
    





