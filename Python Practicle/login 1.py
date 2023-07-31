from tkinter import *
import tkinter.ttk
import os
infofile='file.temp'
def Signup(): 
    global pwordE
    global nameE
    global roots
 
    roots = Tk()
    roots.title('Signup')
    intruction = Label(roots, text='Please Enter new Credidentials\n')
    intruction.grid(row=0, column=0, sticky=E)
 
    nameL = Label(roots, text='New Username: ')
    pwordL = Label(roots, text='New Password: ')
    nameL.grid(row=1, column=0, sticky=W)
    pwordL.grid(row=2, column=0, sticky=W)
 
    nameE = Entry(roots)
    pwordE = Entry(roots, show='*')
    nameE.grid(row=1, column=1)
    pwordE.grid(row=2, column=1)
 
    signupButton = Button(roots, text='Signup', command=saveinfo)
    signupButton.grid(columnspan=2, sticky=W)
    roots.mainloop()
 
def saveinfo():
    with open(infofile, 'w') as f:
        f.write(nameE.get())
        f.write('\n')
        f.write(pwordE.get())
        f.close()
 
    roots.destroy()
    Login()
 
def Login():
    global nameEL
    global pwordEL
    global rootA
 
    login= Tk()
    login.title('Login')
 
    intruction = Label(login, text='Please Login\n')
    intruction.grid(sticky=E)
 
    nameL=Label(login, text='Username: ')
    pwordL=Label(login, text='Password: ')
    nameL.grid(row=1, sticky=W)
    pwordL.grid(row=2, sticky=W)
 
    nameEL = Entry(login)
    pwordEL = Entry(login, show='*')
    nameEL.grid(row=1, column=1)
    pwordEL.grid(row=2, column=1)
 
    loginB = Button(login, text='Login' , command=CheckLogin)
    loginB.grid(columnspan=2, sticky=W)
 
    rmuser = Button(login, text='Delete User', fg='red', command=DelUser)
    rmuser.grid(columnspan=2, sticky=W)
    login.mainloop()
 
def CheckLogin():
    with open(infofile) as f:
        data = f.readlines()
        uname = data[0].rstrip()
        pword = data[1].rstrip()
 
        if nameEL.get() == uname and pwordEL.get() == pword:
            import welcome
        else:
            warning= Tk()
            warning.title('!Warning!')
            warning.geometry('150x50')
            lbl=Label(warning, text='\n!Invalid Login!\n')
            lbl.pack()
            warning.mainloop()     
def DelUser():
    os.remove(infofile)
    login.destroy()
    Signup()
 
    if os.path.isfile(infofile):
        Login()
    else:
        Signup()
def main_screen():
    mainscreen = Tk()
    mainscreen.geometry("994x695")  
    mainscreen.title("login/signup")
    bgimage=PhotoImage(file=r"login background(2).png")
    Label(mainscreen,image=bgimage).place(relwidth=1,relheight=1)
    loginimg=PhotoImage(file=r"login button.png")
    mycolor = '#%02x%02x%02x' % (255, 255, 255)
    login_button=Button(mainscreen,bg=mycolor,image=loginimg, height="40", width="100",command=Login).pack()
    Label(text="")
    Label(text="")
    signin_button=Button(bg=mycolor,text="Signup", height="4",width="40",command=Signup).pack()
    mainscreen.mainloop()

main_screen()
