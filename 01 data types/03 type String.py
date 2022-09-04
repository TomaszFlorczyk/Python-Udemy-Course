str = "Hello World!"
print(str)
print( len(str))
print(type(str))

print( str[len(str) - 1])

print( str[0:5]) #Hello

print(str * 4)

strx3 = str * 3

print(strx3)

str2 = str + " and Hello again!"
print(str2)

print(str2[6:]) #World and hello again

print(str2[::3]) #co 3 literka

multiLine = """Pierwsza lina
Druga linia
Trzecia linia
"""

print(multiLine)

multiLine2 = "Pierwsza linia\nDruga linia\nTrzecia \t linia\" \\\\ "
print(multiLine2)