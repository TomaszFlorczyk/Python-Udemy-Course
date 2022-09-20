<<<<<<< HEAD


import os

print("Absolute Path to script file", __file__)
scriptDir = os.path.dirname(__file__)
print("Absolute path to script directory: ", scriptDir)


pathToFile = scriptDir + "\\newFile.txt"
print("Path to file:", pathToFile)
fh = open(scriptDir + "\\newFile.txt", "w")
fh.write("content")
=======


import os

print("Absolute Path to script file", __file__)
scriptDir = os.path.dirname(__file__)
print("Absolute path to script directory: ", scriptDir)


pathToFile = scriptDir + "\\newFile.txt"
print("Path to file:", pathToFile)
fh = open(scriptDir + "\\newFile.txt", "w")
fh.write("content")
>>>>>>> d4f06d970b4d665710026f2d53dde28fad90b685
fh.close()