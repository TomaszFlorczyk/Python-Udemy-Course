from cart import *


phone1 = Phone("Phone X", 1000, "red")
tv1 = TV("TV y", 10000, 65)

cart = Cart()
cart.addProduct(phone1)
cart.addProduct(tv1)
cart.addProduct(tv1)
cart.addProduct("dupa")
print(cart)