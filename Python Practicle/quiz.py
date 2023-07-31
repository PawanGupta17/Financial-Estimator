from tkinter import *
from tkinter import ttk
import mysql.connector as mysq

n= ttk.Notebook()
f0= ttk.Frame(n)
f1= ttk.Frame(n)
f2= ttk.Frame(n)
f3= ttk.Frame(n)
f4= ttk.Frame(n)
f5= ttk.Frame(n)
f6= ttk.Frame(n)
f7= ttk.Frame(n)
f8= ttk.Frame(n)
window= ttk.Frame(n)
score=0

def main():
    global total
    n.add(f0, text="Instruction")
    n.add(f1, text="One")
    n.add(f2, text="Two")
    n.add(f3, text="Three")
    n.add(f4, text="Four")
    n.add(f5, text="Five")
    n.add(f6, text="Six")
    n.add(f7, text="Score")
    n.add(f8, text="Attempted Question")
    
    

    Label(f0,bg="white", text="there are total 6 question \
\n correct ans → +4 incorrect ans → -1 Non attempted question → 0",font=('courier',15)).grid(row=2,column=2)

    Label(f1,bg="white", text="A furniture dealer deals in only two items–tables and\
\nchairs. He has Rs 50,000 to invest and has storage space\
\nof at most 60 pieces. A table costs Rs 2500 and a chair\
\nRs 500. He estimates that from the sale of one table, he\
\ncan make a profit of Rs 250 and that from the sale of one\
\nchair a profit of Rs 75. He wants to know how many tables and chairs he should buy\
\nfrom the available money so as to maximise his total profit, assuming that he can sell all\
\nthe items which he buys",font=('courier',15)).grid(row=2,column=2)
    Button(f1,bg="white", text="10 tables and 50 chairs", command=correct).grid(row=3,column=1)
    Button(f1,bg="white", text="20 tables and 40 chairs", command=incorrect).grid(row=3,column=2)
    Button(f1,bg="white", text="30 tables and 40 chairs", command=incorrect).grid(row=3,column=3)

    Label(f2,bg="white", text=" A cooperative society of farmers has 50 hectare\
\nof land to grow two crops X and Y. The profit from crops X and Y per hectare are\
\nestimated as Rs 10,500 and Rs 9,000 respectively. To control weeds, a liquid herbicide\
\nhas to be used for crops X and Y at rates of 20 litres and 10 litres per hectare. Further,\
\nno more than 800 litres of herbicide should be used in order to protect fish and wild life\
\nusing a pond which collects drainage from this land. How much land should be allocated\
\nto each crop so as to maximise the total profit of the society?",font=('courier',15)).grid(row=2,column=2)
    Button(f2,bg="white",text=" 40 hectares for crop X and 10 hectares for crop Y",command=incorrect2).grid(row=3,column=1)
    Button(f2,bg="white", text="30 hectares for crop X and 20 hectares for crop Y", command=correct2).grid(row=3,column=2)
    Button(f2,bg="white", text="20 hectares for crop X and 30 hectares for crop Y", command=incorrect2).grid(row=3,column=3)

    Label(f3,bg="white", text="A manufacturer produces nuts and bolts. It takes 1 hour of work on machine A\
\nand 3 hours on machine B to produce a package of nuts. It takes 3 hours on\
\nmachine A and 1 hour on machine B to produce a package of bolts. He earns a\
\nprofit of Rs17.50 per package on nuts and Rs 7.00 per package on bolts. How\
\nmany packages of each should be produced each day so as to maximise his\
\nprofit, if he operates his machines for at the most 12 hours a day?",font=('courier',15)).grid(row=2,column=2)
    Button(f3,bg="white", text="4 packages of nuts and 2 packages of bolts",command=incorrect3).grid(row=3,column=1)
    Button(f3,bg="white", text="3 packages of nuts and 3 packages of bolts", command=correct3).grid(row=3,column=2)
    Button(f3,bg="white", text="4 packages of nuts and 5 packages of bolts", command=incorrect3).grid(row=3,column=3)

    Label(f4,bg="white", text="A factory manufactures two types of screws, A and B. Each type of screw\
\nrequires the use of two machines, an automatic and a hand operated. It takes\
\n4 minutes on the automatic and 6 minutes on hand operated machines to\
\nmanufacture a package of screws A, while it takes 6 minutes on automatic and\
\n3 minutes on the hand operated machines to manufacture a package of screws\
\nB. Each machine is available for at the most 4 hours on any day. The manufacturer\
\ncan sell a package of screws A at a profit of Rs 7 and screws B at a profit of\
\nRs 10. Assuming that he can sell all the screws he manufactures, how many\
\npackages of each type should the factory owner produce in a day in order to\
\nmaximise his profit? Determine the maximum profit",font=('courier',15)).grid(row=2,column=2)
    Button(f4,bg="white", text="Rs 410",command=correct4).grid(row=3,column=1)
    Button(f4,bg="white", text="Rs 500", command=incorrect4).grid(row=3,column=2)
    Button(f4,bg="white", text="Rs 320", command=incorrect4).grid(row=3,column=3)


    Label(f5,bg="white", text="A cottage industry manufactures pedestal lamps and wooden shades, each\
\nrequiring the use of a grinding/cutting machine and a sprayer. It takes 2 hours on\
\ngrinding/cutting machine and 3 hours on the sprayer to manufacture a pedestal\
\nlamp. It takes 1 hour on the grinding/cutting machine and 2 hours on the sprayer\
\nto manufacture a shade. On any day, the sprayer is available for at the most 20\
\nhours and the grinding/cutting machine for at the most 12 hours. The profit from\
\nthe sale of a lamp is Rs 5 and that from a shade is Rs 3. Assuming that the\
\nmanufacturer can sell all the lamps and shades that he produces, how should he\
\nschedule his daily production in order to maximise his profit?",font=('courier',15)).grid(row=2,column=2)
    Button(f5,bg="white", text="3 Pedestal lamps and 5 wooden shades",command=incorrect5).grid(row=3,column=1)
    Button(f5,bg="white", text="3 Pedestal lamps and 4 wooden shades", command=incorrect5).grid(row=3,column=2)
    Button(f5,bg="white", text="4 Pedestal lamps and 4 wooden shades", command=correct5).grid(row=3,column=3)

    Label(f6,bg="white", text="A company manufactures two types of novelty souvenirs made of plywood.\
\nSouvenirs of type A require 5 minutes each for cutting and 10 minutes each for\
\nassembling. Souvenirs of type B require 8 minutes each for cutting and 8 minutes\
\neach for assembling. There are 3 hours 20 minutes available for cutting and 4\
\nhours for assembling. The profit is Rs 5 each for type A and Rs 6 each for type\
\nB souvenirs. How many souvenirs of each type should the company manufacture\
\nin order to maximise the profit?",font=('courier',15)).grid(row=2,column=2)
    Button(f6,bg="white", text="9 Souvenir of types A and 22 of Souvenir of type B",command=incorrect6).grid(row=3,column=1)
    Button(f6,bg="white", text="7 Souvenir of types A and 24 of Souvenir of type B", command=incorrect6).grid(row=3,column=2)
    Button(f6,bg="white", text="8 Souvenir of types A and 20 of Souvenir of type B", command=correct6).grid(row=3,column=3)
    
    Label(f7,bg="white", text=(score,"Out of 24"),font=('courier',15)).grid(row=2,column=2)
    Button(f7,bg='white', text='Submit',command=combine_funcs(scorewriter,menu)).grid(row=3,column=1)

    Label(f8,bg="white",text="Attempted →",font=('courier',15)).grid(row=1,column=1)
    Label(f8,bg="white",text="Non-Attempted →",font=('courier',15)).grid(row=1,column=3)
    Button(f8,bg="green",height=2,width=5).grid(row=1,column=2)
    Button(f8,bg="red",height=2,width=5).grid(row=1,column=4)
    Button(f8,bg="red",text="Q1",height=2,width=5).grid(row=3,column=1)
    Button(f8,bg="red",text="Q2",height=2,width=5).grid(row=3,column=2)
    Button(f8,bg="red",text="Q3",height=2,width=5).grid(row=3,column=3)
    Button(f8,bg="red",text="Q4",height=2,width=5).grid(row=4,column=1)
    Button(f8,bg="red",text="Q5",height=2,width=5).grid(row=4,column=2)
    Button(f8,bg="red",text="Q6",height=2,width=5).grid(row=4,column=3)
    
def correct():
    global score
    score+=4
    Label(f1,bg="white", text="Correct",font=('courier',15)).grid(row=1,column=2)
    Label(f7,bg="white", text=(score,"Out of 24"),font=('courier',15)).grid(row=2,column=2)
    Button(f8,bg="green",text="Q1",height=2,width=5).grid(row=3,column=1)

def incorrect():
    global score
    score-=1
    Label(f1,bg="white", text="Incorrect",font=('courier',15)).grid(row=1,column=2)
    Label(f7,bg="white", text=(score,"Out of 24"),font=('courier',15)).grid(row=2,column=2)
    Button(f8,bg="green",text="Q1",height=2,width=5).grid(row=3,column=1)

def correct2():
    global score
    score+=4
    Label(f2,bg="white", text="Correct",font=('courier',15)).grid(row=1,column=2)
    Label(f7,bg="white", text=(score,"Out of 24"),font=('courier',15)).grid(row=2,column=2)
    Button(f8,bg="green",text="Q2",height=2,width=5).grid(row=3,column=2)

def incorrect2():
    global score
    score-=1
    Label(f2,bg="white", text="Incorrect",font=('courier',15)).grid(row=1,column=2)
    Label(f7,bg="white", text=(score,"Out of 24"),font=('courier',15)).grid(row=2,column=2)
    Button(f8,bg="green",text="Q2",height=2,width=5).grid(row=3,column=2)

def correct3():
    global score
    score+=4
    Label(f3,bg="white", text="Correct",font=('courier',15)).grid(row=1,column=2)
    Label(f7,bg="white", text=(score,"Out of 24"),font=('courier',15)).grid(row=2,column=2)
    Button(f8,bg="green",text="Q3",height=2,width=5).grid(row=3,column=3)

def incorrect3():
    global score
    score-=1
    Label(f3,bg="white", text="Incorrect",font=('courier',15)).grid(row=1,column=2)
    Label(f7,bg="white", text=(score,"Out of 24"),font=('courier',15)).grid(row=2,column=2)
    Button(f8,bg="green",text="Q3",height=2,width=5).grid(row=3,column=3)

def correct4():
    global score
    score+=4
    Label(f4,bg="white", text="Correct",font=('courier',15)).grid(row=1,column=2)
    Label(f7,bg="white", text=(score,"Out of 24"),font=('courier',15)).grid(row=2,column=2)
    Button(f8,bg="green",text="Q4",height=2,width=5).grid(row=4,column=1)

def incorrect4():
    global score
    score-=1
    Label(f4,bg="white", text="Incorrect",font=('courier',15)).grid(row=1,column=2)
    Label(f7,bg="white", text=(score,"Out of 24"),font=('courier',15)).grid(row=2,column=2)
    Button(f8,bg="green",text="Q4",height=2,width=5).grid(row=4,column=1)

def correct5():
    global score
    score+=4
    Label(f5,bg="white", text="Correct",font=('courier',15)).grid(row=1,column=2)
    Label(f7,bg="white", text=(score,"Out of 24"),font=('courier',15)).grid(row=2,column=2)
    Button(f8,bg="green",text="Q5",height=2,width=5).grid(row=4,column=2)

def incorrect5():
    global score
    score-=1
    Label(f5,bg="white", text="Incorrect",font=('courier',15)).grid(row=1,column=2)
    Label(f7,bg="white", text=(score,"Out of 24"),font=('courier',15)).grid(row=2,column=2)
    Button(f8,bg="green",text="Q5",height=2,width=5).grid(row=4,column=2)

def correct6():
    global score
    score+=4
    Label(f6,bg="white", text="Correct",font=('courier',15)).grid(row=1,column=2)
    Label(f7,bg="white", text=(score,"Out of 24"),font=('courier',15)).grid(row=2,column=2)
    Button(f8,bg="green",text="Q6",height=2,width=5).grid(row=4,column=3)

def incorrect6():
    global score
    score-=1
    Label(f6,bg="white", text="Incorrect",font=('courier',15)).grid(row=1,column=2)
    Label(f7,bg="white", text=(score,"Out of 24"),font=('courier',15)).grid(row=2,column=2)
    Button(f8,bg="green",text="Q6",height=2,width=5).grid(row=4,column=3)

def menu():
    n.destroy()
    import1()
    
def import1():
    import menu

def scorewriter():
    with open ('tempname.txt') as f:
        name=f.read()
    mydb=mysq.connect(host="localhost",user='root',passwd='qwerty',database='quiz')
    mycs=mydb.cursor()
    uname1=name
    score1=str(score)
    def check():
        mycs.execute('select uname from score')
        data=mycs.fetchall()
        for i in range (0,len(data)):
            un=data[i][0]
            print(un)
            if uname1==un:
                cnd="select num from score where uname="+"'"+uname1+"'"
                mycs.execute(cnd)
                num=mycs.fetchall()
                cnds="select score from score where uname="+"'"+uname1+"'"
                mycs.execute(cnds)
                sc=mycs.fetchall()
                score2=sc[0][0]
                score2+=score
                score2=str(score2)
                num1=num[0][0]
                num1+=1
                num1=str(num1)
                cmmnd='update score set score='+score2+',num='+num1+' ' +'where uname='+"'"+uname1+"'"
                print(cmmnd)
                mycs.execute(cmmnd)
                break
            else :
                cmmnd1='insert into score value ('+"'"+uname1+"',"+score1+",1"+")"
                print(cmmnd1)
                mycs.execute(cmmnd1)
                break

    check()
    print('rw')
    mydb.commit()

def combine_funcs(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return combined_func

main()
n.pack()
n.mainloop()
