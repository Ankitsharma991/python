class Employee : 
    no_of_leaves = 10
    _protec = 10        # method to declare protected access
    __private = 89       # method to declare private access   

    def __init__(self, aname, asalary, arole): 
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"Name is {self.name}. salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves
    
    @classmethod
    def from_dash(cls, string):
        return cls(*string.split("-"))
    
    @staticmethod
    def printcode(string) : 
        print("This is good " + string)
        return 89  
    
emp = Employee("Ankit", 250, "coder")
print(emp._protec)      #---> method to extract protected access

emp2 = Employee("a", 56, "bag")
print(emp2._Employee__private)  #---> method to extract private access