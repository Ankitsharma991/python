class Employee: 
    company = "Google"
    
    def showDetails(self):
        print("This is an employee")
        
class Programmer(Employee) :
    language = "Python"
    # company = "Youtube"

    def getlanguage(self) : 
        print(f"This language is {self.language}")
        
    def showDetails(self):
        print(f"This is an Programmer")
    
e = Employee()
e.showDetails()
p = Programmer()
p.showDetails()
print(p.company)
