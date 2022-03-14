import  turtle

#akna seaded
t = turtle.Turtle()
aken = turtle.Screen()
aken.setup(800,800)
t.speed(10)
tur = 0

#kujundi loomine

for x in range(4):
    t.left(tur)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
    tur  = 180
    

turtle.exitonclick()