class person : 
    country = "Nepal"
    
    def takeBreath(self) :
        print(f"I am Breathing...")

class Employee : 
    company = "Honda"
    
    def getSalary(self): 
        print(f"Salary is {self.salary}")
        
    def takeBreath(self): 
        print(f"I am Employee so I am luckily breathing..")
        
class Programmer(Employee): 
    company = "Fiverr"
    
    def getSalary(self): 
        print(f"No salary to programmers")
        
       
p = person()
p.takeBreath()

e = Employee()
e.takeBreath()

pr = Programmer()
pr.takeBreath()
pr.company()
pr.country()