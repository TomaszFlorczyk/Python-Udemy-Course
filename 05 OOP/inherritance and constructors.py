

class Person:
    def __init__(self, name, surname, city):
        self.name = name
        self.surname = surname
        self.city = city
        print("Person constructor")

    def printPersonData(self):
        print("Person.printPersonData: ", self.name, self.surname, self.city)

person1 = Person("Ola", "Kowalska", "Krk")
person1.printPersonData()


class Employee(Person):
    def __init__(self, name, surname, city, companyName, salary):
        Person.__init__(self, name, surname, city)
        self.companyName = companyName
        self.salary = salary
        print("Eployee constructor!")
    
    def printEmployeeData(self):
        print("Employee.printEmployeeData", self.name, self.surname, self.companyName, self.salary)

print()
employee1 = Employee("Kasia", "Kot", "Waw", "tech ltd", 10000)
employee1.printPersonData()
employee1.printEmployeeData()


class Menager(Employee):
    def __init__(self, name, surname, city, companyName, salary, department):
        Employee.__init__(self, name, surname, city, companyName, salary)
        self.department = department
        print("Menager constructor!")
    
    def hireEmployee(self):
        print("Hire employee")

    def printMenagerData(self):
        print("Menager data", self.name, self.surname, self.department)
print()
menager1 = Menager("Ania", "X", "Waw","Tech2 ltd", "15000", "IT")
menager1.printPersonData()
menager1.printEmployeeData()
menager1.printMenagerData()
menager1.hireEmployee()




