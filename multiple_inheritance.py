# two parents and one child (parents may be more too) 
class Employee: 
    company = "Visa"
    ecode = 120 
    
class Freelancer : 
    company ="Fiver"
    level = 0
    
    def upgradeLevel(self): 
        self.level = self.level + 1
        
class Programmer(Employee, Freelancer): 
    name = "Rohit"
    
p = Programmer()
p.upgradeLevel()
# p.upgradeLevel()
print(p.level)
print(p.company)
# print(p.level)
