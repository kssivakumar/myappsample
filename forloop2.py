print("This will execute first")

for _ in range(3):
    print("This line will execute three times")
    print("This line will also execute three times")

print("Now we are outside the for loop!")


import turtle
wn = turtle.Screen()
elan = turtle.Turtle()

distance = 10
angle = 90
for _ in range(150):
    elan.forward(distance)
    elan.right(angle)
    elan.pensize(5)
    elan.pencolor("green")
    distance = distance + 5

wn.exitonclick()



import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.color("blue")
tess.shape("turtle")

distance = 5
tess.up()
for _ in range(130):
    tess.stamp()
    tess.forward(distance)
    tess.right(24)
    dist = distance + 5
wn.exitonclick()
