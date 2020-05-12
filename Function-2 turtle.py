import turtle

def draw_square(side_length):
    for i in range(4):
        turtle.forward(side_length)
        turtle.left(90)
        
draw_square(50)
draw_square(100)
draw_square(150)
draw_square(200)
draw_square(250)
turtle.circle(50) # draw a cicle with 50 radius
turtle.circle(100)
turtle.circle(150)
turtle.circle(200)
turtle.circle(250)
turtle.exitonclick()
