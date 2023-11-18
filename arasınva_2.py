import turtle
import random
import math

screen = turtle.Screen()
screen.bgcolor("white")
screen.setup(width=500, height=500)
screen.screensize(500, 500)
t = turtle.Turtle()
t.speed(20) 

def rastgele_cember():
   while True:
        x = random.randint(-200, 200)
        y = random.randint(-200, 200)
        radius = random.choice([5, 10, 15, 20, 25, 30]) 
        clear_to_draw = True
        for existing_circle in circles:
            distance = math.sqrt((x - existing_circle[0])**2 + (y - existing_circle[1])**2)
            if distance < radius + existing_circle[2]:
                clear_to_draw = False
                break

        if clear_to_draw:
            t.penup()
            t.goto(x, y - radius)
            t.pendown()
            renk = (random.random(), random.random(), random.random())
            t.fillcolor(renk)
            t.begin_fill()
            t.circle(radius)
            t.end_fill()

            circles.append((x, y, radius))
            break

circles = []
for _ in range(800):
    rastgele_cember()

turtle.done()
