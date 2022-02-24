class Employee : 
    no_of_leaves = 5
    # pass
    def __init__(self, aname, asalary, arole):         # here __init__ works as a constructor
        self.name = aname
        self.salary = asalary
        self.role = arole


    def printdetails(self):
        return f"Name is {self.name}. salary is {self.salary} and role is {self.role}"

# harry = Employee()
# rohan = Employee()
ankit = Employee("Ankit", 502, "Learner")
print(ankit.salary)

# harry.name = 'Harry'                  
# rohan.name = 'Rohan' 

# harry.salary = 255                            
# rohan.salary = 120
   
# harry.role = "Instructor"     
# rohan.role = "Student" 

# print(harry.salary)                                                
# print(rohan.no_of_leaves)   
                                                           
# Employee.no_of_leaves = 12                                          
# print(Employee.no_of_leaves) 

# # print(rohan.no_of_leaves)                                                           
# print(rohan.__dict__)           # __dict__ is an instance variables which is defined in all classes 
# rohan.no_of_leaves = 22                                          
# print(rohan.__dict__)                                                      
# print(rohan.no_of_leaves) 

# print(harry.printdetails())
# print(rohan.printdetails())

'''
Constructor :- 
'''
