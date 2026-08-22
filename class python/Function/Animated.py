import colorsys
import math
import turtle


def draw_vortex():
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.title("vortex")
    screen.setup(width=800, height=800)
    screen.colormode(1.0)  # RGB 0.0 to 1.0 mode set karne ke liye

    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    screen.tracer(10, 0)

    iterations = 360
    cycles = 6

    for i in range(iterations):
        hue = i / iterations
        color = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
        t.pencolor(color)
        t.pensize(abs(math.sin(i * 0.05)) * 2 + 1)

        angle = i * (360 / cycles) + (i * 0.5)
        distance = math.sqrt(i) * 16

        t.penup()
        t.goto(0, 0)
        t.setheading(angle)
        t.forward(distance)
        t.pendown()

        # Fill color set aur start karne ka sahi tarika
        fill_color = colorsys.hsv_to_rgb((hue + 0.5) % 1.0, 0.8, 0.8)
        t.fillcolor(fill_color)
        t.begin_fill()

        # Shape draw karna
        for _ in range(5):
            t.forward(i * 0.15)
            t.right(144)
            t.forward(i * 0.15)
            t.forward(i * 0.15)
            t.left(72)

        t.end_fill()  # Shape khatam hone ke baad fill finish karein

    screen.update()
    turtle.done()


draw_vortex()