list = ["Ola", "Ania", 23, 99, "Rafał"]
print(type(list))
print(list)


print(list[0])
print(len(list))
print(list[4])
print(list[len(list)-1]) #drukuj 4index

#print(list[5]) błąd: of of range

print(list[-1])
print(list[-2])
print(list[-3])
print(list[-4])
print(list[-5])
#print(list[-6]) of of range

print(list[1:4]) #ania, 23, 99
print(list[2:])

list[0] = "Kasia"
print(list)

del list[2]
print(list)

print(99 in list)
print("Rafał" in list)
print("Ola" in list)

if "Ania" in list:
    print("Ania jest w liscie list")

for v in list:
    print(v)

data = [ 
    ["Daniel", "Rafał"],
    ["Kasia", "Ania"],
    ["Ola", "Adam"]
    ]

print(len(data))

print(data[1][0])
print(data[2][1])

data1 = [1,2,3]
data2 = [4,5,6]
numbers = data1 + data2
print(numbers)

numbersx2 = numbers * 2
print(numbersx2)