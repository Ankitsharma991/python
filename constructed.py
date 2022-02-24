class Employee :   
    company = "Google"
   
    def __init__(self, name, salary, subunit): #construction declaration
        # super().__init__()
        self.name = name
        self.salary = salary
        self.subunit = subunit
        print("Employee is created ")
        
    def getDetails(self): 
        print(f"The name of the employee is {self.name}")
        print(f"The salary of the employee is {self.salary}")
        print(f"The subunit of the employee is {self.subunit}")
    
    def getSalary(self, signature):
        print(f"Salary of this Employee working in {self.company} is {self.salary}\n {signature}")  # print("Salary is 100k")
        
    @staticmethod
    def greet():
        print("Good Morning, Sir")
        
    @staticmethod
    def time():   
        print("The time is 9AM in the morning")
        
harry = Employee("Ankit", 1000, "Youtube")
harry.getDetails()