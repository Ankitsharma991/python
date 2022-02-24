        # program to create a poem in a file and find out the twinkle word , whether it is presented there or not.
# f = open("sampl.txt")
# t = f.read()
# if 'twinkle' in t : 
#     print("twinkle is present")
# else : 
#     print("Twinkle is not present")
# f.close()

        #a game function in a program let set a user play a game    
# def game():
#     a = (input('input your score\n'))
#     return a
# score = game()
# with open('highscore.txt') as f : 
#     hiscore = (f.read())
# if hiscore =='': 
#      with open('highscore.txt', 'w') as f : 
#         f.write(str(score))
# elif hiscore<score:  
#     with open('highscore.txt', 'w') as f : 
#         f.write(str(score))

            #program to create a multiple table and write in different file
            # did in table folder
# p = int(input())
# for i in range(p, (p*10)+1) : 
#     with open(f"tables/multiplication_table_of{i}", 'w') as f :
#         for j in range(1, 11) : 
#             f.write(f"{i}*{j}={i*j}\n")
#         break
            
##program 4 to create a program which can sense bad words and remove those words from the file 

# with open('text1.txt') as f : 
#     content = f.read()
    
# content = content.replace('donkey', "$%^@#$^#")
# with open('text1.txt', 'w') as f : 
#     content = f.write(content)
    
    
    #repeate program 4 for a list of such words to be sensoried 
# words=['donkey', 'kaddu', 'mote']
# with open('text2.txt') as f : 
#     content = f.read()
# for word in words :   
#     content = content.replace(word, "$%^@#$^#")      
# with open('text2.txt', 'w') as f : 
#     content = f.write(content)

        
        ## program to create a log file 
# with open('log.txt') as f : 
#     content = f.read()
# if 'python' in content.lower() : 
#     print("Yes python is present")
# else : 
#     print("No python is not present")
    
    ## program to find the location and line number of the word in a log file 
# content=True
# i=1
# with open('log.txt') as f : 
#     while content :    
#         content = f.readline()
#         if 'python' in content.lower() : 
#             print(content)
#             print(f"Yes python is present in line {i}")
#         i+=1

            ## write a program to make copy of a text file (this.txt)
# with open('this.txt') as f : 
#     content = f.read()
# with open('copy.txt', 'w') as f : 
#     f.write(content)
    
        ##write a program to find out whether a file is identical and matches the content of another file or not
# file1 = 'copy.txt' 
# file2 = 'text1.txt' 

# with open(file1) as f : 
#     f1 = f.read()     

# with open(file2) as f : 
#     f2 = f.read()

# if f1 == f2 : 
#     print("files are identical")
# else : 
#     print("files are not identical")
    

            ## write a program to wipe out the content of a file using python  
# with open('text1.txt', 'w') as f : 
#     f.write("")
    
        ## write a program to rename a file to "renamed_by_python.txt" using python 
import os 
oldname = "dl.txt"
newname = "renamed_by_python.txt"        
with open(oldname) as f : 
    content = f.read()
with open(newname, 'w') as f :   
    f.write(content)
    
os.remove(oldname)
    
        