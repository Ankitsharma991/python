import random
p = int(input("The number of password\n"))
length = int(input("The length of password\n"))
for i in range(p) :
    l = "abcdefghijklmnopqrstuvwxyz"
    u = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    n = "0123456789"
    s = "!@#$%^&*()_+=/"
    all = l + u + n + s
    password = "".join(random.sample(all,length))
    print(password)



#n = int(input())
#l = list(map(int, input().split()))
#x=0
#y=0
#for i in l : 
#  x+=i
#  if x<0 : 
#    y+=1
#    x=0
#print(y)



#n,k = map(int, input().split())
#l = []
#l1=[]
#c=0
#for i in range(n) : 
#    a = input()
#    l.append(a)
#for i in range(k+1) : 
#    l1.append(str(i))
#for i in l : 
#    m=0
#    for j in range(len(l1)) : 
#        if l1[j] not in i : 
#            m = 1
#    if m!=1 : 
#        c+=1
#print(c)

    
