
for v in [1,3,4]:
    print(v * 2)

for v in ("Krotka", "Ania", "Rafał"):
    print(v)

for el in {3,4,5,6,"Ola"}:
    print(el)

for v in "Hello":
    print(v)
else:
    print("petla zakonczona")

dictionaryData = { "ania" : "ania@example.com", "adam" : "adam@ezample.com" }

for key in dictionaryData:
    print(key)

for key in dictionaryData.keys():
    print(key)

for key in dictionaryData.keys():
    print(dictionaryData[key])

for key, value in dictionaryData.items():
    print( key, " : ", value)

for v in dictionaryData.values():
    print(v)