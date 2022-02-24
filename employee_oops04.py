class Employee:   
    company = "Google"
    salary = 100
    
ankit = Employee()
rajni = Employee()

# creating instance attribute salary for both the object
# ankit.salary = 300
# rajni.salary = 400

# print(ankit.company)
# print(rajni.company)
Employee.company="Facebook"
# print(ankit.company)
# print(rajni.company)
print(ankit.salary)
print(rajni.salary)

# below line will throw an error as address is not present in instance/class
# print(ankit.address)

#now it will work
# Employee.address="Internet"
# print(ankit.address)

# An attribute that belongs to the instance (object) Assuming the class from the previous example