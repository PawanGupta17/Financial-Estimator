from tkinter import *
import tkinter.ttk
import tkinter.font as tkFont
import csv

test_file = 'Names.csv'
with open ('tempname.txt') as f:
    name=f.read()
with open(test_file, 'r')as c:
    csv_file = csv.DictReader(c)    
    for line in csv_file:
        if name==line['uname']:
            uname=line['uname']
            passw=line['password']
            mbno=line['mobno']

def goback():
    mainscreen.destroy()
    import menu

def savechanges():
    with open('file.txt','r') as f:
        data = f.readlines()
        a=len(data)
        for i in range(0,a,2):
            name1 = data[i].rstrip()
            if uname == name1:
                data[i]=nameE.get()+'\n'
                
        for j in range(1,a+1,2):
            pword = data[j].rstrip()
            if passw == pword:
                data[j]=pwordE.get()+'\n'
    with open('file.txt','w') as f:
        f.writelines(data)
    root=Tk()
    b=Label(root,text='Changes saved').grid(row=1,column=1)


mainscreen = Tk()
mainscreen.geometry("1006x753")  
mainscreen.title("login/signup")
bgimage=PhotoImage(file=r"backprofile.png")
Label(mainscreen,image=bgimage).place(relwidth=1,relheight=1)

logoimg=PhotoImage(file=r"icon1.png")
logo=Label(mainscreen,image=logoimg)
logo.place(x=444,y=90)
loginimg=PhotoImage(file=r"login button.png")

fontStyle=tkFont.Font(size=17)
nameL=Label(mainscreen,bg="#ffffff",text='Username : ',font=fontStyle)
pwordL=Label(mainscreen,bg="#ffffff",text='Password  : ',font=fontStyle)
mobnoL=Label(mainscreen,bg="#ffffff",text='Phone No. : ',font=fontStyle)
nameL.place(x=300,y=300)
pwordL.place(x=300,y=350)
mobnoL.place(x=300,y=400)

mystr = StringVar()
nameE = Entry(mainscreen,width=30,font=fontStyle)
pwordE = Entry(mainscreen,width=30,font=fontStyle)
mobnoE = Entry(mainscreen,textvariable=mystr,width=30,fg='black',bg='white',font=fontStyle,state=DISABLED)
mystr.set(mbno)
nameE.place(x=430, y=300)
pwordE.place(x=430, y=350)
mobnoE.place(x=430, y=400)
nameE.insert(END,uname)
pwordE.insert(END,passw)

save = Button(mainscreen, text='Save Changes', command=savechanges,bg='white',font=fontStyle)
goback = Button(mainscreen, text='Go Back', command=goback,bg='white',font=fontStyle)
save.place(x=300,y=450)
goback.place(x=500,y=450)

