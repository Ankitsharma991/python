# File io basics
# "r" - open file for reading -- deafault mode
# "w" - open file for writing 
#"x" - create files if not exists
# "a" - add more content to a file
# "t" - text mode -- Default mode
# "b" - binary mode 
# "+" - read and write mode



f = open("Ankit.txt", "rt")
print(f.readlines())
#print(f.readline())
#print(f.readline())
#print(f.readline())
#content = f.read()
#print(content)
#for i in range(len(f)) : 
#    p = f.read(i)
#    print(p)
#for line in f : 
#    print(line)
f.close()

