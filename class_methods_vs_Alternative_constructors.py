class Employee : 
    no_of_leaves = 10
    # pass
    def __init__(self, aname, asalary, arole):         # here __init__ works as a constructor
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"Name is {self.name}. salary is {self.salary} and role is {self.role}"
    
# Employee.no_of_leaves = 89

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves
    
    @classmethod
    def from_dash(cls, string):
        params = string.split("-")
        print(params)
        return cls(params[0], params[1], params[2])
        # return cls(*string.split("-"))

ankit = Employee("Ankit", 502, "Learner")
rohan = Employee("Rohan", 204, "Tutor")

karan = Employee.from_dash("Karan-400-student")
print(karan.salary)
print(karan.name)
print(karan.role)
print(karan.no_of_leaves)