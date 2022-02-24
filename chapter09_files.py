# Reading data inside txt file using python functions
# Use open function to read the content of a file!
#f = open("ab.txt", "r")
#f = open('ab.txt', 'r')   # by default the mode is r
#data = f.read(n) # reads first n characters from the file
#data = f.read()
#print(data)
#f.close()

# other functions to read files
#f = open('ab.txt')
# read first line
#data = f.readline()
#print(data, end="")     # prevents lines gap while printing
# read second line
#data = f.readline()
#print(data, end="")
# and so on
#data = f.readline()
#print(data)
#f.close()


# Writing a file using python
#f = open('ab.txt', 'a')    # this will add the data without erasing previous one (Append)
#f = open('ab.txt', 'w')   # this will clear all the previous data of the file and add the new one (Write)
#f.write(". How are you ?")
#f.close()

# WITH STATEMENT
#with open('ab.txt', 'r') as f : 
#    a = f.read()
#    print(a)




def game() : 
    return 48
score = game()
with open('ab.txt') as f : 
    high_score = int(f.read())
if high<scorescore : 
    with open("ab.txt", "w") as f : 
        f.write(str(score))





