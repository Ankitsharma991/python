            # '''----------------Map Functions--------------------------------'''
# number = ["4", "5","2", "8"]
# # print(map(int, number))

# number = list(map(int, number))
# # print(number[0] + 4)

# # for i in range (len(number)) : 
# #     number[i] = int(number[i])
    
# # number[0] = number[0] + 2
# # print(number[0])

# # def sq(a): 
# #     return a*a

# # num = [2, 3, 4, 5, 6, 7, 8]
# # square = list((map(sq, num))
# # print(square)


# # num = [2, 3, 4, 5, 6, 7, 8]
# # square = list(map(lambda x: x*x, num))
# # print(square)


# def square(a): 
#     return a*a

# def cube(a): 
#     return a*a*a

# fune = [square, cube]
# num = [2, 3, 4, 5, 6, 7, 8]
# for i in range(5) : 
#     val = list(map(lambda x: x(i), fune))
#     print(val)
    
            #'''------------------------Filter Function-----------------------------'''
# lsi = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# def isGreater(num) : 
#     return num>3

# greater_than_5 = list(filter(isGreater, lsi))
# print(greater_than_5)



            #'''------------------------Reduce Function-----------------------------'''
#___________________________________________________________________________

from functools import reduce
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
num = reduce(lambda x,y : x+y, list1)
# num = 0
# for i in list1 : 
#     num = num + i
print(num)

