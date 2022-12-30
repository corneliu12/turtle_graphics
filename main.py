from turtle import Turtle, Screen
import random

brush = Turtle()

colors = ['royale blue', 'blue', 'medium blue', 'navy', 'light sky blue', 'turquoise', 'aquamarine',
        'dark sea green', 'medium sea green', 'sea green', 'lime green', 'firebrick', 'maroon', 'tomato', 
        'orange red', 'red', 'crimson', 'salmon', 'indian red', 'medium violet red', 'purple', 'yellow',
        'gold', 'goldenrod', 'peru', 'pale goldenrod', 'orange']


def draw_shape(n_side):
    angle = 360/n_side
    for _ in range(n_side):
        brush.forward(100)
        brush.right(angle)


for shape_side_n in range(3, 11):
    brush.color(random.choice(colors))
    draw_shape(shape_side_n)




screen = Screen()
screen.exitonclick()