<<<<<<< HEAD
import turtle
import time

t = turtle.Turtle()
win = turtle.Screen()

win.title("Application")
win.bgcolor("yellow")
win.setup(width=550, height=550)

t.forward(100)
print("x", t.xcor())
print("y", t.ycor())

def keyPressedW():
    print("w clicked")
    t.fd(20)

def keyPressedS():
    print("s clicked")
    t.bk(20)

win.listen()
win.onkey(keyPressedW, "w")
win.onkey(keyPressedS, "s")

win.tracer(0)

while True:
    win.update()
    time.sleep(0.1)
=======
import turtle
import time

t = turtle.Turtle()
win = turtle.Screen()

win.title("Application")
win.bgcolor("yellow")
win.setup(width=550, height=550)

t.forward(100)
print("x", t.xcor())
print("y", t.ycor())

def keyPressedW():
    print("w clicked")
    t.fd(20)

def keyPressedS():
    print("s clicked")
    t.bk(20)

win.listen()
win.onkey(keyPressedW, "w")
win.onkey(keyPressedS, "s")

win.tracer(0)

while True:
    win.update()
    time.sleep(0.1)
>>>>>>> d4f06d970b4d665710026f2d53dde28fad90b685
win.mainloop()