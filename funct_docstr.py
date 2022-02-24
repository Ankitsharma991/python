#a = 12
#b = 13
#c = sum((a, b))
#print(c)



#def  function1(a,b) : 
#    print("Hello you are in function1", a+b)
#a , b = map(int, input().split())
#function1(a, b)



'''Creating your own functions'''

#def greet() : 
#    print("Hii There")
#    print("Welcome Abroad")
#    
#    
#greet()


'''Inserting the values in parameters of a function by user'''
#def greet(first_name, last_name) : 
#    print(f"Hi {first_name} {last_name}")
#    print("Welcome Abroad")
#    
#greet("Ankit", "Sharma")
#greet("Prashant", "Prasar")
#greet("Deepak", "prajapati")



''' Two types of function are there'''
# 1- Perform a task
#2- perform a value

#def get_greeting(name) : 
#    return f"Hi {name}"
#    
#message = get_greeting("Ankit")
#file = open("filename.exe_name", "abc")
#file.write(message)
    #"""[summary]
    #"""#print(message)


'''Defining a function to increment a number by certain value'''
#def increment(number, by) : 
#    return number + by
#result = increment(5, 6)
#print(result)



''' Defining a function to take variables number of arguments'''
#def multiply(a, b) : 
#    print(multiply, a*b)
#    return (a*b)
#multiply(4, 5)


#def multiply(*numbers) : 
#    total = 1
#    for number in numbers : 
#        total += number
#        return total 
#multiply(2, 3, 4, 5)



