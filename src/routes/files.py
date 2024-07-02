import os
filenames = os.listdir()
for file in filenames:
    with open(file,"r", encoding="utf-8") as my_file:
        print(file)
        print(my_file.read())
        print(file)