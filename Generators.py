'''
Iterable -> __iter__() or __getitem__()
Iterator -> __next__()
Iteration -> 

Generators are types of a Iterator which can be traverse just only once
'''

# def gen(n): 
#     for i in range(n) : 
#         yield i
        
# g = gen(3)
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())

h = "harry"
# print(iter(h))
ier = iter(h)
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())

# print(h[0])
# for c in h : 
#     print(c)