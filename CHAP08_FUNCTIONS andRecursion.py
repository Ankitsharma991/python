#8.1 (program to print average of 5 marks uding fumctions)
#def percent(marks) : 
#    p = ((marks[0]+marks[1]+marks[2]+marks[3]+marks[4])/500)*100
#    return(p)
#
#marks = [45, 65, 85, 15, 75]
#percentage1 = percent(marks)
#
#marks2 = [25, 65, 89, 25, 26]
#percentage2 = percent(marks2)
#
#print(percentage1, percentage2)

#8.2 (program to greet someone usimg functions)
#N = input("enter your name \n") 
#G = input("enter the greeting\n")
#a = int(input())
#b = int(input())
#def greet(name) : 
#    print(G+ ", " + name)
#def mysum(num1, num2) : 
#    return num1 + num2
#greet(N)
#s = mysum(a, b)
#print(s)

#8.3 (program to take default parameter values)
#def greet(name="Stranger") : 
#    print("Good Day, " + name)
#greet("Ankit")         # name will be "Ankit" in function body (passed)
#greet()                # name will be "Stranger" in the function body (default)



                #   RECURSION (a self call function)
# program to print factorial using for loop
#n = int(input())
#product = 1
#for i in range(n) : 
#    product = product * (i+1)
#print(product)

# program to print factorial by defining a function
#t = int(input())
#def factorial_iter(n) : 
#    product = 1
#    for i in range(n) : 
#        product = product * (i+1)
#    return product 
#
#print(factorial_iter(t))

# n! = n* (n-1)!
#t = int(input())
#def fac(n) : 
#    if n==1 or n==0 : 
#        return 1
#    return n*fac(n-1)
#f = fac(t)
#print(f)





