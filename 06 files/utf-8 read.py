<<<<<<< HEAD
import os

scriptDir = os.path.dirname(__file__)

fh = open(scriptDir + "/ogonki.txt", "r", encoding = "utf-8")
lines = fh.readlines()
fh.close()

print(lines)
for line in lines:
    print(line)


fh = open(scriptDir + "/ogonki.txt", "r", encoding = "utf-8")
print("\n")

while True:
    line = fh.readline()
    if not line:
        break
    print(line)

=======
import os

scriptDir = os.path.dirname(__file__)

fh = open(scriptDir + "/ogonki.txt", "r", encoding = "utf-8")
lines = fh.readlines()
fh.close()

print(lines)
for line in lines:
    print(line)


fh = open(scriptDir + "/ogonki.txt", "r", encoding = "utf-8")
print("\n")

while True:
    line = fh.readline()
    if not line:
        break
    print(line)

>>>>>>> d4f06d970b4d665710026f2d53dde28fad90b685
fh.close()