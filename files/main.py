import os
f = open("book.txt", "r")
#f.write("Now the file has one more line!")
os.remove("myfile.txt")


print(f.read())

