

number = 12

def test1():
    print(number) #12

test1()

def test2():
    number = 100
    print(number) #100

    if 1 == 1:
        print(number) #100
        if 2 == 2:
            number = 50
            print(number) #50
    print(number) #50

test2() #100
print(number) #12


print("\ntest3\n")

def test3():
    global number
    number = 5
    print("test3", number)
    if 1 == 1:
        number = 6
        print("test3", number)

test3()
print("global number after test3", number)


print("\ntest4\n")

number = 10
def test4(number):
    print("test4 param: ", number)
    number = 20
    print("test4after change", number)

test4(33)
print("number afagter test 4() ", number)

print("\ntest5\n")

number = 10
def foo():
    print("foo() number: ", number)

def bar():
    number = 9
    print("bar number: ", number) #9
    foo()

bar()
print("global number after foo() bar()", number)

print("\n check1 & check2\n")

number = 10
def check1():
    number = 12
    print("check1() number: ", number)
    def check2():
        print("check2 number: ", number) #9
    check2()

check1()
print("global number after check1():", number)


print("\nif test")

if 1 == 1:
    data = 100 #utworzy zmienna globalna

print(data)

if 2 == 1:
    nextData = 15
#print("next data", nextData) #not defined

