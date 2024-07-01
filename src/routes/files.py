#with open("hello.txt", encoding="utf-8" "w") as my_file:
   # my_file.read()
    #my_file.write("Some contents")
#some code...
import os
filenames = os.listdir()
for file in filenames:
    with open(filename,"r", encoding="utf-8" as my_file):
        print(filename)
        print(my_file.read())
        print(file)