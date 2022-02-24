# def function1(): 
#     print('Subscribe now')

# func2 = function1
# del function1
# func2()

# def funcret(num) : 
#     if num == 0: 
#         return print
#     if num == 1: 
#         return int
# a = funcret(0)
# print(a)

# def executor(func) : 
#     func("this")

# executor(print)

def dec1(func1) : 
    def nowexecute(): 
        print("Executing now")
        func1()
        print("Executed")
    return nowexecute

def whoisHarry(): 
    print("Harry is a good boy")

whoisHarry = dec1(whoisHarry)
whoisHarry()

