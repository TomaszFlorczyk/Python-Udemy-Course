<<<<<<< HEAD
import os

scriptDir = os.path.dirname(__file__)
print(scriptDir)


fh = open(scriptDir + "/ogonki.txt", "w", encoding = "utf-8")
fh.write("tekst z ogonkami: ąśćół\n")
fh.write("tekst z ogonkami: ąśćół\n") 
fh.write("tekst z ogonkami: ąśćół\n")
=======
import os

scriptDir = os.path.dirname(__file__)
print(scriptDir)


fh = open(scriptDir + "/ogonki.txt", "w", encoding = "utf-8")
fh.write("tekst z ogonkami: ąśćół\n")
fh.write("tekst z ogonkami: ąśćół\n") 
fh.write("tekst z ogonkami: ąśćół\n")
>>>>>>> d4f06d970b4d665710026f2d53dde28fad90b685
fh.close()