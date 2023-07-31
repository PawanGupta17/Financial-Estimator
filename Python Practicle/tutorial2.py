import turtle
from turtle import *
cont1="Financial estimator can easily find the maximum profit here. It can be of great help to \
\ncalculate the number of products to be manufactured to realise the maximum profit.\
\nLet x and y be the number of pieces of model A and B respectively.\
\nSo Profit= 8000x+12000y\
\nThis is our objective function that is to be maximised. Afterwards the information is converted \
\ninto equation form.\
\ni.e.   9x+12y<=180    x+3y<=30      x,y>0\
\nThen these linear inequalities are plotted on graph.\
\n\n Press space bar to see graph."
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
def clear1():
    cont.clear()
    import graph
main.listen()
main.onkeypress(clear1, "space")

