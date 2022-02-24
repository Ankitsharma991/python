#*************** Lambda funtion or Anoymous funtion ***************

# def add(a, b) : 
#     return a+b 
# print(add(9,4))
# # minus = lambda x, y : x-y #This line has no value , output can be shown without this line


# def minus (x, y) : 
#     return x-y 
# print(minus(9,4)


# def a_first(a):
#     return a[1]
# a = [[1,14],[55,16],[118,2]]
# a.sort(key=a_first)
# print(a)

# def a_first(a) : 
#     return a[1] 
a=[[1,14],[5,6],[28,23]]
a.sort(key= lambda x: x[1])
b=sorted(a)
print(b)
print(a)
