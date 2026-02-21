f=open("file.txt")
print(f.read())
f.close()

#This same can be written using with statment like this:
with open("file.txt")as f:
    print(f.read())
    
# You dont have to emplicity close the file
