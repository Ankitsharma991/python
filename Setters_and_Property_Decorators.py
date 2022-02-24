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

No_Mcc = Employee("Nepali", "Supporter")
Ankit_sharma = Employee("Ankit", "Sharma")

# print(No_Mcc.email)
# No_Mcc.fname = "US"
# print(No_Mcc.fname)
# print(No_Mcc.email)
# No_Mcc.email = "This.that@codewithharry.com"
print(No_Mcc.email)

del No_Mcc.email
print(No_Mcc.email)
No_Mcc.email = "is.at@codewithharry.com"
print(No_Mcc.email)