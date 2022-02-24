'''
Object Introspection means to know about following listed information of object :- 
                -->from which class the objects belongs to
                -->which type of the objects are
                -->how they are being stored
                -->all all the information ab out them
'''

class Employee : 
    def __init__(self, fname, lname): 
        self.fname = fname
        self.lname = lname
        # self.email = f"{fname}.{lname}@codewithharry.com"
        
    def explain(self) : 
        return f"This employee is {self.fname} {self.lname}"
    @property   #Decorators
    def email(self): 
        if self.fname == None or self.lname == None : 
            print("--------Email is not set!!!----------")
        return f"{self.fname}.{self.lname}@codewithharry.com"
    
    @email.setter
    def email(self, string) : 
        print("Setting Now")
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]
        
    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None
        
skillf = Employee("Skill", "R")
# print(skillf.email)

# print(type(skillf))     # Object Introspection
# print(id(skillf))

# print(type("skillf")) 
# print(id("skillf"))
# print(id("skill"))


o = "This is a string"
print(dir(o))

import inspect
print(inspect.getmembers(skillf))
