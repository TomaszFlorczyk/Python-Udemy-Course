

import os

print("Absolute Path to script file", __file__)
scriptDir = os.path.dirname(__file__)
print("Absolute path to script directory: ", scriptDir)


pathToFile = scriptDir + "\\newFile.txt"
print("Path to file:", pathToFile)
fh = open(scriptDir + "\\newFile.txt", "w")
fh.write("content")
fh.close()