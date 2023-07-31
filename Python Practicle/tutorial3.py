import turtle
from turtle import*
cont1="he feasible solution lies at the corners of the enclosed area.\
\nTo find the maximum profit every corner point will be put on the objective function.\
\nSince (12,6) point gives maximum value,it will yield maximum profit.\
\nSo 12 units of model A and 6 units of model B are required to attain a maximum profit of Rs. 168000\
\nPress space bar to go to menu."
main=turtle.Screen()
main.title('Tutorial')
main.setup(width=1300, height=800)
main.bgpic('backimg.png')
cont=turtle.Turtle()
cont.speed(0)
cont.color("black")
cont.penup()
cont.hideturtle()
cont.goto(0,0)
cont.write(cont1,align='center',font=('algerian',18,'normal'))
def menu():
    main.bye()
    import menu
main.listen()
main.onkeypress(menu,"space")
