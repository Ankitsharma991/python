            # 01 (MIKE AND PALINDROME)
#a = input()
#b = a.lower()
#c = len(b)
#count = 0
#for i in range(0,c,1) : 
#    if b[i] != b[-i-1] : 
#        count = count + 1
#        #break
#        if count == 1 : 
#            result = "YES"
#        else : 
#            result = "NO"
#print(result)

 

#a = input()
#t = len(a)
#p = 0
#q = 0
#if t == 1 : 
#        print("YES") 
#        exit()
#while t-p-1 > p : 
#        if a[p] != a[t-p-1] : 
#                q += 1 
#        elif t%2 == 0 and t>=2 : 
#                if a==a[::-1] : 
#                        print("NO")
#                        exit()
#        elif t%2 != 0 : 
#                if a==a[::-1] : 
#                        print("YES")
#                        exit()
#                p += 1
#if q == 1 or t%2 == 0 and q==0 : 
#        print("YES")
#else : 
#        print("NO")







            # 02 (Football)
#a = input()
#b = a.count("0000000")
#c = a.count("1111111")
#if c>=1 or b>=1 : 
#    print("YES")
#else : 
#    print("NO")


        # OTHER METHOD OF PROBLEM FOOTBALL
#k = input()
#if "0000000" in k : 
#    print("YES")
#elif "1111111" in k : 
#    print("YES")
#else : 
#    print("NO")



            #04(MIKE AND PALINDROME)
#a = input()
#b = len(a)
#count = 0
#for i in range(b//2) :
#    if a[i] != a[b-i-1] : 
#        count += 1
#if count == 1 : 
#    print("YES")
#else : 
#    print("NO")


            # 03 (SUPERHERO TRANSFORMATION)) 
#s = input()
#t = input()
#c = len(s)
#if len(s) == len(t) : 
#    for i in range(c) : 
#        if t.find("a", "e", "i", "o", "u") == s.find("a", "e", "i", "o", "u") : 
#            print("YES")
#else : 
#    print("NO")




        #######################
#s = input()
#t = input()
#b = ("a", "e", "i", "o", "u", "n")
#if len(s) == len(t) : 
#    for i in range(len(s)) : 
#        if s[i] in b == t[i] in b : 
#            if s[i] not in b == t[i] not in b : 
#                print("YES")
#            else : 
#                print("NO")
#else :
#    print("NO")










            #04 (MINIMIZING THE STRING)

#a = input()
#for i in range(len(a)) : 
#    if a[i] > a[i+1] : 
#        result = 


a = int(input())
b = input()
for i in range(a) : 
        if b[1]>b[1|1] : 
                print(b[:1]|b[1|1:])
                exit()
print(b[:0, 1])




# ROMAjI

#s = input()
#a = len(s)
#vow = ('a', 'e', 'i', 'o', 'u')
#for i in range(0,a-1,2) : 
#    if s[i] == 'n' : 
#            result="YES"    
#    if s[i] not in vow: 
#        if s[i+1] in vow : 
#            result = "YES"
#    else : 
#        result = "NO"
#print(result)


#s = input()
#t = len(s)
#vow = ["a", 'e', 'i', 'o', 'u']
#p = 0
#for i in range(t-1) : 
#        if s[i] not in vow and s[i] != 'n' : 
#                if s[i+1] not in vow : 
#                        p = 1
#if s[t-1] not in vow and s[t-1] != 'n' : 
#        print("NO")
#elif p==1 : 
#        print("NO")
#else : 
#        print("YES")
#






#s = input()
#vow = ('a', 'e', 'i', 'o','u')
#for i in range(len(s)-1) : 
#        if (s[i] not in vow+'n') and (s[i+1] not in vow) : 
#                result = "No"
#        else : 
#                result = "Yes"
#print(result)


                       #SUPERHERO TRANSFORMATION
#s = input()
#t = input()
#p = len(s)
#q = len(t)
#if p != q : 
#        print("NO")
#        exit()
#for i in range(p) : 
#        if ((s[i]=='a' or s[i]=='e' or s[i]=='u' or s[i]=='i' or s[i]=='i') and (t[i]=='a' or t[i]=='e' or t[i]=='i' or t[i]=='o' or t[i]=='o' or t[i]=='u')) : 
#                continue
#        elif ((s[i]!='a' or s[i]!='e' or s[i]!='u' or s[i]!='i' or s[i]!='i') and (t[i]!='a' or t[i]!='e' or t[i]!='i' or t[i]!='o' or t[i]!='o' or t[i]!='u')) : 
#                continue
#        else : 
#                print("NO")
#                exit()
#print("YES")

s = input()
t = input()
p = len(s)
vow = ("a", "e", "i", "o", "u")
if p != len(t) :
        result = "NO" 
        #print("NO")
        #exit()
for i in range(p) : 
        if (s[i] in vow) : 
                if t[i] in vow : 
                        continue 
        elif (s[i] not in vow) : 
                if t[i] not in vow : 
                        continue
        else : 
                print("NO")
                exit()
print("YES")



#s = input()
#t = input()
#p = len(s)
#q = len(t)
#vow = ('a', 'e', 'i', 'o', 'u')
#if p==q : 
#        for i in range(p) : 
#                if (s[i] not in vow) and (t[i] not in vow) : 
#                                #continue 
#                                result = "YES"
#                elif (s[i] not in vow) and (t[i] not in vow) : 
#                                #continue 
#                                result = "NO"
#
#                else : 
#                        result = "NO"
#        print(result)
#        exit()
#else : 
#        result = "NO"
#print(result)


#s = input()
#t = input()
#p = len(s)
#t = len(t)
#if p == q : 
#        for i in range(p) : 
#                if s[i] in vow 




       


