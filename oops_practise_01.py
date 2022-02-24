# # ******************create a class programmer for storing informaion of few programmers working at mivrosoft  *********************

# class programmer():
#     company = 'Microsoft'
#     def __init__(self, name, product): 
#         self.name = name   
#         self.product = product
#     def getInfo(self):  
#         print(f"The name of the programmer is {self.name} and the product is {self.product}")
        
# harry = programmer("Harry", "Skype")
# Ankit = programmer("Ankit", "GitHub")  
# harry.getInfo()
# Ankit.getInfo()
        
        
        
        
        
        

#************ Write a class calculate capable of finding square, cube and square-root of a number **************** 

# class calculator : 
    
#     def __init__(self, num): 
#         self.number = num    
        
#     def square(self): 
#         print(f"The value of {self.num} square is {self.num **2}")
    
#     def cube(self): 
#         print(f"The value of {self.num} square is {self.num **3}")
    
#     def squareRoot(self): 
#         print(f"The value of {self.num} square is {self.num *0.5}")
    
# a = calculator(5)

# a.square()

# a.cube()

# a.squareRoot()







#********* create a class with a class attribute a ; create an object from it and set a directly using object.a = 0 , does this change the class attribute ??********

# class sample :     
#     a = 'Ankit'

# obj = sample()
# # obj a : str le()
# obj.a = 'Vikky' 
# print(sample.a)
# print(obj.a)





#******Add a static method in problem 2 to greet the user ********

# class Calculator:   
#     def __init__(self, num): 
#         self.number = num

#     def square(self): 
#         print(f"The value of {self.number} square is {self.number **2}")
        
#     def squareRoot(self): 
#         print(f"The value of {self.number} square root is {self.number **0.5}")
        
#     def cube(self): 
#         print(f"The value of {self.number} cube is {self.number **3}")
        
#     @staticmethod   
#     def greet(): 
#         print("Hello three welcome to the best calculator of the world")
        
# n = int(input())
# a = Calculator(n)
# a.greet()
# a.square()
# a.squareRoot()
# a.cube()





#**********write a class train which has methods to book a ticket, get status (no of seat) and get fare information of trains under Indian railway********

# class train :   
#     def __init__(self, name, fare, seats): 
#         self.name = name 
#         self.fare = fare 
#         self.seats = seats 
    
#     def getStatus(self):
#         print(f"The name of the Train is '{self.name}'")
#         print(f"The seats available of the train is {self.seats}")
        
#     def fareInfo(self):
#         print(f"The price of the ticket is : {self.fare}")
        
#     def bookTickets(self): 
#         if (self.seats > 0): 
#             print(f"Your Ticket has been Booked and Your Seat number is {self.seats}")
#             self.seats = self.seats - 1
#         else : 
#             print("Sorry, the seat is full kindly try in tatkal")
            
#     def cancelTickets(self, seatNumber):
#         #implement and append the cancel ticket number in a list and bla bla wala qsn
        
    
# intercity = train("Intercity Express : 14015", 90, 2)
# intercity.getStatus()
# intercity.bookTickets()
# intercity.bookTickets()
# intercity.bookTickets()
# intercity.getStatus()
# # intercity.fareInfo()




#*********Can you change the self parameter inside a class to something else (say 'Ankit'). Try changing self to 'SLF' or 'Ankit' and see the effects**************

class sample: 
    # a = 'Ankit' 
    def __init__(f, name) : 
        f.name = name 
    
obj = sample('Ankit')
# obj.a = 'Harry'
print(obj.name)
