# w=input().split(" ")
# a=int(w[0])
# b=int(w[1])
# c=int(w[2])
# if a>=1 and a<=100 and b>=1 and b<=100 and c>=1 and c<=100 :
#     if a>b and a>c : 
#         p=a
#         q=b
#         r=c
#     elif b>a and b>c : 
#         p=b
#         q=a
#         r=c 
#     else : 
#         p=c
#         q=a
#         r=b
#     count=p-(q+r)
#     if count<0 :
#         print("0")
#     else :
#         print(count+1)




#**********Review Site****************

# t = int(input())
# for i in range (t): 
#     n =int(input())
#     a = list(map(int,input().split()))
#     count = 0
#     for i in a : 
#         if i == 1 or i==3 : 
#             count += 1  
#     print(count)

        
#************ The Rank **************

# t = int(input())
# m=[]
# m1=[]
# for i in range(t): 
#     l = list(map(int,input().split()))
#     m.append(sum(l))
#     m1.append(sum(l))
# m1.sort(reverse=True)
# rank=1
# for i in range(0,t,1): 
#     if m[0]==m1[i] : 
#         rank+=i 
#         break
# print(rank)


#********** Spy Detected ***************

# t = int(input())
# for i in range(t) : 
#     n = int(input())
#     a = list(map(int,input().split()))
#     k = sorted(a)[1]
#     for j in range(n) : 
#         if a[j] != k : 
#             print(j+1)
#             break
        
# t = int(input())
# for i in range(t) : 
#     n = int(input())
#     a = list(map(int,input().split()))
#     k = sorted(a)[1]
#     for j in range(n) : 
#         if a[j] != k : 
#             print(j+1)
#             break
        
        
#********** Lesha and array splitting ********
n = int(input())
a = list(map(int,input().split()))
if a.count(0)==n : 
    print("NO")
else :
    print("YES")
x = sum(a)
if x!=0 : 
    print(1)
    print(1,n)
else : 
    for i in range(n) : 
        x -= a[i] 
        if x != 0 : 
            print(2)
            print(1, i+1)
            print(i+2, n)
            break
