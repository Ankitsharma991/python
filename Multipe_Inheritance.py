class Employee : 
    no_of_holidays = 10
    var = 8

    def __init__(self, aname, asalary, arole):         # here __init__ works as a constructor
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

class players : 
    var = 9
    no_of_games = 4
    def __init__(self, name, game): 
        self.name = name
        self.game = game
        
    def printdetails(self):
        return f"The Name is {self.name}. Game is {self.game}"

class coolProgrammer(Employee, players):
    # var = 10
    language = "C++"
    def printLanguage(self): 
        print(self.language)

ankit = Employee("Ankit", 502, "Learner")
rohan = Employee("Rohan", 204, "Tutor")

shubham = players("Shubham", ["Cricket"])
karan = coolProgrammer("karan", 64, "CoolProgrammer")
# print(karan)
det = karan.printdetails()
karan.printLanguage()
print(det)
print(karan.var)
