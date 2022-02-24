class Employee : 
    no_of_leves = 10
    
    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole
        
    def printDetails(self):
        return f"The Name is {self.name}, Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_Inname(cls, newleaves) : 
        cls.no_of_leves = newleaves
        
    def __add__(self, other):   # mapping operators to function
        return self.salary + other.salary
    
    def __truediv__(self, other) :  # mapping operators to function
        return self.salary / other.salary
        
    def __repr__(self) : 
        # return self.printDetails()
        return f"Employee('{self.name}', '{self.salary}', '{self.role}')"
    
    def __str__(self) :
        return f"The Name is {self.name}, Salary is {self.salary} and role is {self.role}"
    
    
emp1 = Employee("Harry", 145, "Programmer")
emp2 = Employee("Ankit", 290, "Carpenter")
# print(emp1 + emp2)
# print(emp1 / emp2)
print(str(emp1))