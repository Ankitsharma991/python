# class RailwayForm : 
#     formType = 'RailwayForm'
#     def printData(self):
#         print(f"Name is {self.name}")
#         print(f"Train is {self.train}")

# AnkitApplication = RailwayForm()
# AnkitApplication.name = str(input())
# AnkitApplication.train = str(input())
# AnkitApplication.printData()


t = int(input())
for i in range(t): 
    a, b = list(map(int, input().split()))
    i = 0 
    while i +a <= b : 
        if b%(a+i)==0 : 
            i += 1
            b -= 1
        break
print((a+i), b)

