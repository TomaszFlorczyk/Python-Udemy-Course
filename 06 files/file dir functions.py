<<<<<<< HEAD
import os, shutil

scriptDir = os.path.dirname(__file__)

fh = open(scriptDir + "/test.txt", "w", encoding="utf-8")
fh.write("Dane randomowoe")
fh.close()

if not os.path.exists(scriptDir + "/newTest.txt"):
    os.rename(scriptDir + "/test.txt",scriptDir + "/newTest.txt")

print(os.path.getsize(scriptDir + "/newTest.txt"))
print(os.path.isfile(scriptDir + "/newTest.txt"))
print(os.path.isdir(scriptDir + "/newTest.txt"))
print(os.path.isdir("./basics"))

if os.path.exists(scriptDir + "/subDir"):
    os.rmdir(scriptDir + "/subDir")

if not os.path.exists(scriptDir + "/subDir"):
    os.mkdir(scriptDir + "/subDir")

if os.path.exists(scriptDir + "/newTest.txt"):
    os.remove(scriptDir + "/newTest.txt")

print("Current working dir: ", os.getcwd())

if not os.path.exists("data-copy.dat"):
    shutil.copyfile("data.dat", "data-copy.dat")
=======
import os, shutil

scriptDir = os.path.dirname(__file__)

fh = open(scriptDir + "/test.txt", "w", encoding="utf-8")
fh.write("Dane randomowoe")
fh.close()

if not os.path.exists(scriptDir + "/newTest.txt"):
    os.rename(scriptDir + "/test.txt",scriptDir + "/newTest.txt")

print(os.path.getsize(scriptDir + "/newTest.txt"))
print(os.path.isfile(scriptDir + "/newTest.txt"))
print(os.path.isdir(scriptDir + "/newTest.txt"))
print(os.path.isdir("./basics"))

if os.path.exists(scriptDir + "/subDir"):
    os.rmdir(scriptDir + "/subDir")

if not os.path.exists(scriptDir + "/subDir"):
    os.mkdir(scriptDir + "/subDir")

if os.path.exists(scriptDir + "/newTest.txt"):
    os.remove(scriptDir + "/newTest.txt")

print("Current working dir: ", os.getcwd())

if not os.path.exists("data-copy.dat"):
    shutil.copyfile("data.dat", "data-copy.dat")
>>>>>>> d4f06d970b4d665710026f2d53dde28fad90b685
