import  turtle

#akna seaded
aken = turtle.Screen()
aken.setup(300,300)

 
#kujundi loomine
t = turtle.Turtle()
for x in range(5):
    t.right(144)
    t.forward(100)

 
varv = input('mis värvi tahad(inglise keelses) : ')
pikkus = int(input('kui pikkad on su küljed : '))

t = turtle.Turtle()
for x in range(3):
    t.color(varv)
    t.forward(pikkus)
    t.left(120)


turtle.exitonclick()