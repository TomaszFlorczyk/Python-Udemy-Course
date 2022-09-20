import os

print("Current working directory: ", os.getcwd() )

files = os.listdir(".")
#print(files)

files = os.listdir("./basics/programs")
#print(files)

files = os.listdir("../Python projects/basics/programs")
print(files)