import turtle
from turtle import * 

main=turtle.Screen()
main.title('Tutorial')
main.setup(width=1300, height=800)
main.bgpic('backimg.png')
def tutorial1():
    global intro
    intro1="Many applications in mathematics involve systems of inequalities/equations.Here we are\
    \ngoing to apply the systems of linear inequalities/equations to solve some real life problems.\
    \nFor eg.,\nA manufacturing company makes two models A and B of a product. Each piece of model A \
    \nrequires 9 hours of labour for fabricating and 1 hour for finishing. Each piece of model B \
    \nrequires 12 hours of labour for fabricating and 3 hours for finishing. The maximum number of\
    \nlabour hours, available for fabricating and for finishing, are 180 and 30 respectively. The \
    \ncompany makes a profit of ₹ 8,000 and ₹12,000 on each piece of model A and model B respectively.\
    \n Such type of problems which seek to maximise or minimise profit or cost \
    \nform a general class of problems called optimisation problems. Thus, an optimisation problem may\
    \ninvolve finding maximum profit, minimum cost, or minimum use of resources etc.\nA special but a \
    very important class of optimisation problems is linear programming problem. \
    \n\n Press space bar to continue."
    intro=turtle.Turtle()
    intro.speed(0)
    intro.color("black")
    intro.penup()
    intro.hideturtle()
    intro.goto(0,0)
    intro.write(intro1,align='center',font=('algerian',18,'normal'))
    main.listen()
    main.onkeypress(clear, "space")

def tutorial2():
    global cont 
    cont1="Financial estimator can easily find the maximum profit here. It can be of great help to \
    \ncalculate the number of products to be manufactured to realise the maximum profit.\
    \nLet x and y be the number of pieces of model A and B respectively.\
    \nSo Profit= 8000x+12000y\
    \nThis is our objective function that is to be maximised. Afterwards the information is converted \
    \ninto equation form.\
    \ni.e.   9x+12y<=180    x+3y<=30      x,y>0\
    \nThen these linear inequalities are plotted on graph.\
    \n\n Press space bar to see graph."
    cont=turtle.Turtle()
    cont.speed(0)
    cont.color("black")
    cont.penup()
    cont.hideturtle()
    cont.goto(0,0)
    cont.write(cont1,align='center',font=('algerian',18,'normal'))
    main.listen()
    main.onkeypress(clear1, "space")

def graph():
    main=turtle.Screen()
    main.title('Graph')
    main.setup(width=1246, height=605)
    main.bgpic('graph.png')
    main.listen()
    main.onkeypress(clear2, "space")

def tutorial3():
    main=turtle.Screen()
    main.title('Tutorial')
    main.setup(width=1300, height=800)
    main.bgpic('backimg.png')
    cont1="he feasible solution lies at the corners of the enclosed area.\
    \nTo find the maximum profit every corner point will be put on the objective function.\
    \nSince (12,6) point gives maximum value,it will yield maximum profit.\
    \nSo 12 units of model A and 6 units of model B are required to attain a maximum profit of Rs. 168000\
    \nPress space bar to go to menu."
    cont2=turtle.Turtle()
    cont2.speed(0)
    cont2.color("black")
    cont2.penup()
    cont2.hideturtle()
    cont2.goto(0,0)
    cont2.write(cont1,align='center',font=('algerian',18,'normal'))
    main.listen()
    main.onkeypress(menu,"space")

def clear():
    intro.clear()
    tutorial2()

def clear1():
    cont.clear()
    graph()

def clear2():
    tutorial3()

def menu():
    main.bye()
    import menu

tutorial1()
