import math


import math
import random


print(type( str(12)))
print(type( str([12,34])))

number = int("123")
print(type(number))

number += 10
print(number)

print( "123" + "10")

floatNum = float( "45.67")
print(type(floatNum))
floatNum = floatNum * 2

print( floatNum)

print( abs(9))
print( abs(-9.1))

print(math.ceil(11.0000001))
print(math.ceil(-1.0000001))
print(math.ceil(-1.9999999))


print(math.floor(11.0000001)) #11
print(math.floor(11.9999999)) #11
print(math.floor(5.12)) #5
print(math.floor(-5.12)) #-6
print(math.floor(-5.999999)) #-6


print( max(10, 1 ,-9, 33 ,89, 0))
print( max([10, 1 ,-9, 33 ,89, 0]))
print( max((10, 1 ,-9, 33 ,89, 0)))

print( min((10, 1 ,-9, 33 ,89, 0)))

print( 4 ** 3)
print( pow(4 ,3))

print(math.sqrt(128)) #11.31.....


print( round(12.78912345567, 3))
print( round(12.78912345567, 2))
print( round(12.78912345567, 1))

print(random.random())
print(random.random() * 100)
print(int(random.random() * 100))


print(random.choice([0,1,2,3,4]))
print(random.choice(("ola", "Ania", "Adam")))

print(random.randrange(-10, 30, 5))

listData = [0,1,2,3,4,5,6,7]
random.shuffle(listData)
print(listData)
