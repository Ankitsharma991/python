class A : 
    classvar1 = "I am a class variable in class A"
    def __init__(self): 
        self.var1 = "I am inside class A's constructor"
        self.classvar1 = "Instance var in class A"
        self.special = "special"
        
class B(A):
    classvar1 = "I am in class B"
    # pass
    def __init__(self): 
        super().__init__()
        self.var1 = "I am inside class B's constructor"
        self.classvar1 = "Instance var in class B"
a = A()
b = B()

print(b.special, b.var1, b.classvar1)