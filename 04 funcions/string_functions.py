
print("hello " + " Wolrd!")
print( "Hello" * 3)

string =  "Hello world!"

print( string[0]) #H
print( string[0:5]) #Hello

print( "Hello" in string)
print( "Hello" not in string)

multiline = """ line 1
line 2
line 3
"""

print("ala".capitalize() )
print( "Ola ma kota, Ola ma psa".count("Ola"))

print("Hello".center(20, "-"))

print( string.startswith("Hello"))
print( string.endswith("world!"))

print( string.find("Ola"))
print( string.find("world"))
print("Ola ma psa, Ola ma kota".rfind("Ola"))

print("234567890".isalnum())
print("234567890 sdad".isalnum())
print("234567890 sdad".isalpha())
print("sdad".isalpha())
print("sdad ".isalpha())
print("sdad2".isalpha())

print("test".islower())
print("Test".islower())
print("TEST".isupper())
print("TEst".isupper())

print("TEst".isspace())
print("    \n\n\t".isspace())

print("-|".join(["ala","ola","Adam"]))

print("Hello World".lower())
print("Hello World".upper())
print("Hello World".swapcase())


print( "    \n \t Hello World \n\n  \t".lstrip() )
print( "    \n \t Hello World \n\n  \t".rstrip() )
print( "    \n \t Hello World \n\n  \t".strip() )

print("Ola ma psa, Ola ma kota".replace("Ola", "Kasia"))

print("My name is {myName}, I'm from {country}".format(myName = "Tomcio", country = "Poland"))
print("My name is {myName}, my postal code is {code}".format(myName = "Tomcio", code = 96969))
print("My name is {0}, my postal code is {1}".format("Tomcio", 69696969))
print("My name is {}, my postal code is {}".format("Tomcio", 69696969))

