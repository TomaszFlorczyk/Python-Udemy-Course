import os, pickle

scriptDir = os.path.dirname(__file__)

class Person:
    def __init__(self, name, surname, city):
        self.name = name
        self.surname = surname
        self.city = city

    def __str__(self,):
        return str(self.name) + " " + str(self.surname) + " " + self.city

    
person1 = Person("ola", "kowalska", "krk")
person2 = Person("adam", "kot", "waw")
person3 = Person("jas", "dupa", "gdansk")

people = [person1, person2, person3]

fh = open(scriptDir + "/people.dat", "wb")
pickle.dump(people, fh)
fh.close()

fh = open(scriptDir + "/people.dat", "rb")
listFromFile = pickle.load(fh)
fh.close()

print(listFromFile)

for person in listFromFile:
    print(person)