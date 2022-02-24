# ls = []
# for i in range(100): 
#     if i%3 == 0 :
#         ls.append(i)
# print(ls)

# ls = [i for i in range(100) if i%3 == 0]     # Comprehension
# print(ls)

# dict1 = {i:f"item(i)" for i in range(5)} 
# dict2 = {value:key for key, value in dict1.items()}
# print(dict1,"\n", dict2)

# dress = {dress for dress in ["dress1", "dress2", "dress1", "dress2", "dress1", "dress2"]}       # this is set introspection
# print(type(dress))

            #--------------Generator Comprehension-----------
evens = (i for i in range(100) if i % 2 == 0)
# print((evens.__next__()))
# print(*evens)
for item in evens:
    print(item)