#WHCH TRIANGEL
#n = int(input())
#for i in range(n) : 
#    a,b = map(int, input().split())
#    c = 180-(a+b)
#    if a==b==c : 
#        print('equilateral')
#    elif a==b or a==c or b==c : 
#        print('isosceles')
#    else : 
#        print('scalene')

 #REMOVAL VOWEL
#s = input()
#p=""
#vow = ['a','e','i','o','u']
#for i in range(len(s)) : 
#    if s[i] not in vow : 
#        p=p+s[i]
#print(p)

#EVEN ODD SORT
#s = list(map(int, input().split()))
#o = []
#e = []
#for i in s : 
#    if i%2 == 0 : 
#        e.append(i)
#    else : 
#        o.append(i)
#r = e+o
#for j in r : 
#    print(j, end=" ")



#FRUITS IN BASKET
#n = int(input())
#f = list(input().split())
#b = 0
#g = 0
#a = 0
#for i in f : 
#    if i == 'yellow' : 
#        b += 1
#    elif i == 'green' : 
#        g += 1
#    elif i=='red' : 
#        a += 1
#if b>g and b>a : 
#    print('banana')
#elif g>b and g>a : 
#    print('guava')
#elif a>b and a>g : 
#    print('apple')
#else : 
#    print('none')



# SCORE MISMATCH
#n = int(input())
#a = list(map(int,input().split()))
#b = list(map(int,input().split()))
#for i in range(n) : 
#    if b[i] - a[i] != 10 : 
#        print(a[i],b[i])
#        break


#REVERSE THE WORD
#l = list(map(str,input().split()))
#for i in l : 
#    print(i[::-1],end=' ')


a=[]
for i in range(10) : 
    a.append(i* ++i)
for a[i] in a : 
    print(a[i])






#FRUITS IN BASKET



