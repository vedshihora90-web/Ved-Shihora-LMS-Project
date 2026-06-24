#text file handeing in python

#syntax
#file=open("file name","mode")

#1.read mode

file=open("demo.py","r")
print(file.read())
file.close()

#2.write mode

file=open("demo.txt","w")
file.write("\n pyhon file handeling!!!!")
file.close()

#3.again read
file=open("demo.txt","r")
print(file.read())
file.close()

#4.append mode
file=open("demo.txt","a")
file.write("\n pyhon is easy to learn!!!!")
file.close()

file=open("demo.txt","r")
print(file.read())
file.close()

#write lines is same like write

#best method for handeling because file close handeling
with open("demo.txt","r")as file:
    print(file.read())




