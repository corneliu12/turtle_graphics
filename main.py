from turtle import Turtle, Screen
import random

brush = Turtle()
brush.speed("fastest")

colors = ['royale blue', 'blue', 'medium blue', 'navy', 'light sky blue', 'turquoise', 'aquamarine',
        'dark sea green', 'medium sea green', 'sea green', 'lime green', 'firebrick', 'maroon', 'tomato', 
        'orange red', 'red', 'crimson', 'salmon', 'indian red', 'medium violet red', 'purple', 'yellow',
        'gold', 'goldenrod', 'peru', 'pale goldenrod', 'orange']

def draw_shape(n_side):
    """drawing polygons up to n_side one on top of each other"""
    
    # calculate the angle of eachh poligon
    angle = 360 / n_side 
    
    # loop to draw each side of the poligon
    for _ in range(n_side): 
        brush.forward(100)
        brush.right(angle)

# loop to draw each poligon with random color
for shape_side_n in range(3, 11):
    brush.color(random.choice(colors)) 
    draw_shape(shape_side_n)

screen = Screen()
screen.exitonclick()