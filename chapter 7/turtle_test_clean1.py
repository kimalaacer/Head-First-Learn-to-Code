import turtle
slowpoke=turtle.Turtle()
slowpoke.shape('turtle')
def make_square(the_turtle):
    for i in range(5):
        the_turtle.forward(100)
        the_turtle.right(72)
make_square(slowpoke)

turtle.mainloop()
