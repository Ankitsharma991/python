# def function_name_print(a, b, c, d, e):
#     # print("",a,"\n",b,"\n",c,"\n",d,"\n",e)
#     # print(a, b, c, d, e)
# function_name_print("Harry", "Rohan", "Skillf", "Hammad", "Shivam")

def funargs(normal, *args, **kwargs):         #order or method is normal > args > Kwargs
    # print(args[0])
    # print(type(args))
    print("\t", normal)
    for items in args:
        print(items)
    
    for key, value in kwargs.items():
        print(key, value)
# funargs("Harry", "Rohan", "Skillf", "Hammad", "Shivam")
normal = "This is Normal arguments"
har = ["Harry", "Rohan", "Skillf", "Hammad", "Shivam", "The Programmer","\n"]
kw = {"Ankit":"Programmer", "Rohan":"Students", "Harry":"Youtuber"}
funargs(normal, *har, **kw)
    
    