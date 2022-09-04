data = ("Ala", "Ola", "Kasaia")

#data[0] = "Rafał"  błąd

names = data + ("Rafał",)
print(names)
print(len(names))
print(type(names))

numbers = 1, 2, 3
print(type(numbers))

emptyTuple = ()
print(emptyTuple)
print(type(emptyTuple))

print(names[1])
print(names[-1])
print(names[1:3])

cars = ( ( "dodge", "ford"), ("pontiac"))
print(cars[0][0])

if "ford" in cars[0]:
    print("ford w krotce nr 1")

del cars
#print(cars) error

#del names[0] nie mozna usuwac elementów z krotki

tupleX3 = names * 3
print(tupleX3)
