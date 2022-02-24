#Faulty calculator 
a, b = map(int, input().split())
op = input()
if (a == 45 and b==3) or (b==45 and a==3) : 
    if op == '*' : 
        print("45*3 = 555")
elif (a==56 and b==9) or (a==56 and a==9) : 
    if op=='+' : 
        print("56+9 = 77")
elif (a==56 and b==6) or (a==6 and b==56) : 
    if op=='/' : 
        print((a/b), "= 4")
else : 
    print(a(op)b)
    
    