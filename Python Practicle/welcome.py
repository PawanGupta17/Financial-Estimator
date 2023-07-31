import turtle
from turtle import *
text="\tWelcome to Analysis of Expenditures and Profits \n\n\n\n\n\n\n\
We have made this project to make you understand the concept of \nlinear programming\
and using the concepts to test them in a quiz.\nDo you want to take a tutorial on \
linear programing\n press t else press m?"
main=turtle.Screen()
main.title('Welcome Screen')
main.setup(width=1000,height=700)
main.bgpic('backimg.png')
cont=turtle.Turtle()
cont.speed(0)
cont.color("black")
cont.penup()
cont.hideturtle()
cont.goto(0,0)
cont.write(text,align='center',font=('algerian',20,'normal'))
def clear1():
    cont.clear()
    import tutorial
def menu():
    main.bye()
    import menu
main.listen()
main.onkeypress(clear1,"t")
main.onkeypress(menu,"m")
