from tkinter import *
import tkinter.ttk

def tutorial():
    import tutorial

def score():
    menu.destroy()
    import score

def quiz():
    import quiz

def doubt():
    menu.destroy()
    import doubt
def combine_funcs(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return combined_func
def profile():
    menu.destroy()
    import Profile
menu = Tk()
menu.geometry("626x626")  
menu.title("MENU")
bgimage=PhotoImage(file=r"menuback.png")
Label(menu,image=bgimage).place(relwidth=1,relheight=1)
tutimg=PhotoImage(file=r'tutorial.png')
tut=Button(menu,bg='#ffffff',image=tutimg,height=35,width=160,command=combine_funcs(menu.destroy,tutorial))
tut.place(x=50,y=120)
quizimg=PhotoImage(file=r'quiz.png')
quiz=Button(menu,bg="#ffffff",image=quizimg,height=40,width=100,command=combine_funcs(menu.destroy,quiz))
quiz.place(x=50,y=200)
scoreimg=PhotoImage(file=r'score.png')
score=Button(menu,bg="#ffffff",image=scoreimg,height=40,width=105,command=score)
score.place(x=50,y=280)
doubtimg=PhotoImage(file=r'doubt.png')
doubt=Button(menu,bg='#ffffff',image=doubtimg,height=35,width=260,command=doubt)
doubt.place(x=50,y=360)
profileimg=PhotoImage(file=r"profile.png")
profile=Button(menu,image=profileimg,height=60,width=50,command=profile)
profile.place(x=570,y=0)
