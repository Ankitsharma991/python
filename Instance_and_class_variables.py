class Employee :                                           
    no_of_leaves = 5                                                
    pass                                                                                   

harry = Employee()                                   
rohan = Employee()                            

harry.name = 'Harry'                                      
rohan.name = 'Rohan'                                   

harry.salary = 255                           
rohan.salary = 120                                  

harry.role = "Instructor"                               
rohan.role = "Student"                                     

print(harry.salary)                                 
print(rohan.no_of_leaves)                                    
Employee.no_of_leaves = 12                          
print(Employee.no_of_leaves) 
# print(rohan.no_of_leaves)                         
print(rohan.__dict__)     # __dict__ is an instance variables which is defined in all classes 
rohan.no_of_leaves = 22                                 
print(rohan.__dict__)                          
print(rohan.no_of_leaves)                 
