class Employee :   
    company = "Google"
    def getSalary(self, signature):
        print(f"Salary of this Employee working in {self.company} is {self.salary}\n {signature}")  # print("Salary is 100k")
    @staticmethod
    def greet():
        print("Good Morning, Sir")
    @staticmethod
    def time():   
        print("The time is 9AM in the morning")
        
harry = Employee()
harry.greet()  #Employee.greet()
harry.salary = 100000
harry.getSalary("Thanks!") # Employee.getSalary(harry)
harry.time()