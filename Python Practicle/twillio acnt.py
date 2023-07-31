from tkinter import *
import tkinter.ttk
import webbrowser
def twillioacnt():
    warning= Tk()
    warning.title('!Warning!')
    warning.geometry('250x150')
    warning.configure(background='white')
    lbl=Label(warning,bg="white", text='\nDo you have a twillio account?\nOnce made then come back and press "YES"')
    yesButton = Button(warning,bg="white",text='YES',height=2,width=5)
    yesButton.place(x=50,y=50)
    noButton = Button(warning,bg="white",text='NO',height=2,width=5,command=twilliodirect)
    noButton.place(x=150,y=50)
    lbl.pack()
    warning.mainloop()
    
def twilliodirect():
    url='https://www.twilio.com/try-twilio'
    webbrowser.open(url)

def acntinfo():
    global sidE
    global tokenE
    global numE
    warning= Tk()
    warning.title('!Warning!')
    warning.geometry('350x150')
    warning.configure(background='white')

    lbl=Label(warning,bg="white",text='Enter following information')
    sidL=Label(warning,bg="white",text='account_sid                  :')
    tokenL=Label(warning,bg="white",text='auth_token                   :')
    numL=Label(warning,bg="white",text='Twillio account Phno. :')
    lbl.pack()
    sidL.place(x=10,y=20)
    tokenL.place(x=10,y=70)
    numL.place(x=10,y=120)
    
    
    sidE= Entry(warning, show='*',width=30)
    tokenE= Entry(warning, show='*',width=30)
    numE= Entry(warning, show='*',width=30)
    sidE.place(x=135,y=20)
    tokenE.place(x=135,y=70)
    numE.place(x=135,y=120)
    yesButton = Button(warning,bg="white",text='YES',height=2,width=5,command=printinfo)
    yesButton.place(x=50,y=50)


def printinfo():
    sid=sidE.get()
    token=tokenE.get()
    num=numE.get()
    print(sid,token,num)
acntinfo()
