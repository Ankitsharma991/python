class Number :          
    def sum(self): 
        return self.a + self.b   
num = Number()
num.a = int(input())
num.b = int(input()) 
s = num.sum()
print(s)

# DRY means Don't Repeat Yourself

'''PascalCase 
EmployeeName--> PascalCase 
camelName 
isNumeric, isFloatorInt --> camelCase'''