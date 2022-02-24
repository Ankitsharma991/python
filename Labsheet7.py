               #DIAGONAL WALKING
n = int(input())
s = input()
s1=s.upper()

p = 0
q = 0

while q<n-1 : 
  if s1[q] + s1[q+1] in 'RU' or s1[q]+s1[q+1] in 'UR' : 
    q = q + 2
    p = p + 1
  else : 
    q = q + 1

print(n-p)

     
  

               
               
               
                # REPEATING CIPHER
#n = int(input())
#s = input()
#l = len(s)
#p = ""
#m = 0
#n = 0
#if n == l : 
#  for i in range(l) : 
#    p = s[i]
#    m+=1
#    n=n+m
#print(p)

    

#n = int(input())
#s = input()
#s1 = ""
#i = 0
#c = 0
#while i+c < n : 
#  s1 += s[i]
#  c+=1 
#  i = i+c 
#print(s1)
          
                               # BOY OR GIRL

#s = input()
#t = set(s.lower())
#l = len(t)
#if l%2 == 0 : 
#  print("CHAT WITH HER!")
#else : 
#  print("IGNORE HIM!")
  
            
            # A WORD
#s = input()
#t = len(s)
#p = s.upper()
#q = s.lower()
#count = 0
#for i in range(t) : 
#  if s[i].islower() : 
#    count += 1
#if count >= t/2 : 
#  print(q)
#else : 
#  print(p)


              # LOVE A
#s = input()
#t = s.lower()
#l = len(t)
#p = t.count('a')
#if p > l//2 : 
#  print(l)
#else : 
#  print((2*p)-1)




