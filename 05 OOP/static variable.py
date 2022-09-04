
class Employee:
    "Emplloyee class destribing company employee"
    # static variables for all bjects based on Employee
    numEmployees = 0
    employeedList = []

    def __init__(self,name):
        "Constructor for employee"
        """
        line 1
        line 2
        """
        self.name = name

        Employee.numEmployees += 1
        print(self.name, "numEmployees: ", Employee.numEmployees)

        Employee.employeedList.append(self)

    def printAllEmployees(self):
        for el in Employee.employeedList:
            print(el.name)

employee1 = Employee("Ola")
employee2 = Employee("Kasia")
employee3 = Employee("Adam")
employee4 = Employee("Karol")

print("Emplyee.numEmployees: ",Employee.numEmployees)
print()

employee1.printAllEmployees()

print(Employee.__doc__)
print(Employee.__name__)
print(Employee.__module__)

print("name attr in Employee: ", hasattr(employee1, "name"))
print("city attr in Employee: ", hasattr(employee1, "city"))

employee1.city = "Krk"
print("city attr in Employee: ", hasattr(employee1, "city"))

setattr(employee1, "name", "Kasia")
print("employee1.name: ", getattr(employee1, "name"))
