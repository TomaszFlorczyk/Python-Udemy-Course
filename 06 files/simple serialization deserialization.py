import os, pickle

scriptDir = os.path.dirname(__file__)

number = 123456
listData = ["ania", "ola", "kasia", 12345]
strData = "Test ąśół"

fh = open(scriptDir + "/data.dat", "wb")
pickle.dump(number, fh)
pickle.dump(listData, fh)
pickle.dump(strData, fh)
fh.close()

fh = open(scriptDir + "/data.dat", "rb")
numberInfo = pickle.load(fh)
listInfo = pickle.load(fh)
strInfo = pickle.load(fh)
fh.close()

print(numberInfo)
print(listInfo)
print(strInfo)