import turtle


def draw_square(some_turtle):
    for i in range(1, 5):
        some_turtle.forward(100)
        some_turtle.right(90)


def draw_triangle(another_turtle):
    for i in range(1, 4):
        another_turtle.backward(100)
        another_turtle.left(120)


def draw_shape():
    window = turtle.Screen()
    window.bgcolor('darkgreen')
# draw square
    anna = turtle.Turtle()
    anna.shape('turtle')
    anna.color('yellow')
    anna.speed(1)
    draw_square(anna)

# draw circle
    levi = turtle.Turtle()
    levi.shape('arrow')
    levi.color('orange')
    levi.circle(100)

    # draw triangle
    kobe = turtle.Turtle()
    kobe.shape('turtle')
    kobe.color('magenta')
    kobe.speed(1)
    draw_triangle(kobe)

    window.exitonclick()


draw_shape()
