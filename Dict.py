#creating a dictionary
D1 = {
    "Name" : "Ankit",
    "Title" : "Sharma",
    "Harry" : "Burger",
    "Rohan" : "Fish",
    "Neeraj" : "Meat",
    "Shubham" : {
        "Breakfast" : "Sandwich",
    
        "Lunch" : {
            "item1" : "Rice",
            "item2" : "Fish curry",
            "item3" : "Salad"
        },
        "Snacks" : {
            "s1" : "Tea",
            "s2" : "Banana"
        },
        "Dinner" : {
            "d1" : "Naan",
            "d2" : "Chicken Biryani"
        }
    }
}
p, q = input().split()
D1[p] = q
# D1[420] = "Kabab"
print(D1)
# D2 = D1.copy() #use to copy thevalues and items from one dictionary to another
#print(D1)
#del D1[420] #this command will delete the keys and values pair of 420 from dictionaryD1
#del D2[420] # use to delete the keys and values pair of 420 from dictionary
# D2.update({"Hemant" : "Toffee"}) #use to update the keys and values pair of a dictionary
#D1.get["Hemant"]
# print(D2.keys()) # print out the keys name of a dictionary
# print(D1.items()) # print out the items name of a dictionary



