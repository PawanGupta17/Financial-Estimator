from tkinter import *
import tkinter.ttk
import os
from twilio.rest import Client
import math as m
import random as r
import webbrowser
import csv as cv

infofile='file.txt'

def main_screen():
    global nameEL
    global pwordEL
    global mainscreen
    
    mainscreen = Tk()
    mainscreen.geometry("1006x753")  
    mainscreen.title("login/signup")
    bgimage=PhotoImage(file=r"login background(2).png")
    Label(mainscreen,image=bgimage).place(relwidth=1,relheight=1)
    
    logoimg=PhotoImage(file=r"icon1.png")
    logo=Label(mainscreen,image=logoimg)
    logo.place(x=423,y=130)
    loginimg=PhotoImage(file=r"login button.png")
    
    nameL=Label(mainscreen,bg="#ffffff",text='Username: ')
    pwordL=Label(mainscreen,bg="#ffffff",text='Password: ')
    nameL.place(x=355,y=300)
    pwordL.place(x=355,y=350)
    
    nameEL = Entry(mainscreen,width=30)
    pwordEL = Entry(mainscreen, show='*',width=30)
    nameEL.place(x=425,y=300)
    pwordEL.place(x=425,y=350)
    
    loginimg=PhotoImage(file=r"login button.png")
    loginB = Button(mainscreen,bg="#ffffff",image=loginimg,height=35,width=100,
                    command=CheckLogin)
    loginB.place(x=435,y=400)
    
    sep=Label(mainscreen,bg="#ffffff",text="-----------o------------")
    sep.config(font=("Courier",15))
    sep.place(x=354,y=450)

    signin_button=Button(text="Don't have an account?Signup for free",
                         bg="#ffffff",fg="blue",width=41,
                         command=combine_funcs(mainscreen.destroy,Signup))
    signin_button.place(x=354,y=500)
    mainscreen.mainloop()

def Signup(): 
    global pwordE
    global nameE
    global sign
    global otpE

    sign=Tk()
    sign.title('Signup')
    sign.geometry("1006x753")
    bgimage=PhotoImage(file=r"login background(2).png")
    Label(sign,image=bgimage).place(relwidth=1,relheight=1)
    logoimg=PhotoImage(file=r"icon1.png")
    logo=Label(sign,image=logoimg)
    logo.place(x=423,y=130)
 
    nameL = Label(sign,text='Username            :',bg="#ffffff")
    pwordL = Label(sign, text='Password             :',bg="#ffffff")
    nameL.place(x=355,y=300)
    pwordL.place(x=355,y=350)
 
    nameE = Entry(sign,width=30)
    pwordE = Entry(sign, show='*',width=30)
    nameE.place(x=455,y=300)
    pwordE.place(x=455,y=350)

    otpL = Label(sign, text="Mobile Number :",bg="#ffffff")
    otpE = Entry(sign,width=30)
    otpL.place(x=355,y=400)
    otpE.place(x=455,y=400)
    
    signimg=PhotoImage(file=r"signup.png")
    signupButton = Button(sign,image=signimg,bg="#ffffff",text='Signup',height=36,
                          width=115,command=twillioacnt)
    signupButton.place(x=435,y=450)
    sign.mainloop()
    
def twillioacnt():
    warning= Tk()
    warning.title('!Warning!')
    warning.geometry('250x150')
    warning.configure(background='white')
    lbl=Label(warning,bg="white", text='\nDo you have a twillio account?\nIf no then press No\nAfter doing same come back and press Yes')
    yesButton = Button(warning,bg="white",text='YES',height=2,width=5,command=combine_funcs(warning.destroy,acntinfo))
    yesButton.place(x=50,y=70)
    noButton = Button(warning,bg="white",text='NO',height=2,width=5,command=twilliodirect)
    noButton.place(x=150,y=70)
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
    warning.geometry('350x220')
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
    yesButton = Button(warning,bg="white",text='OK',height=2,width=5,command=saveinfo)
    yesButton.place(x=135,y=170)

def saveinfo():
    with open(infofile,"r") as f:
        data = f.readlines()
        num=len(data)
    if num==0:
        with open(infofile,'a') as f:
            f.write(nameE.get())
            f.write('\n')
            f.write(pwordE.get())
            f.write('\n')
            f.close()
            profileinfo()
            sign.destroy()
            otp()
        
    else:
        with open(infofile,"r") as f:
            data = f.readlines()
            for a in range (0,num,2):
                uname = data[a].rstrip()
                if nameE.get()==uname:
                    warning= Tk()
                    warning.title('!Warning!')
                    warning.geometry('150x50')
                    lbl=Label(warning, text='\n!User name already taken!\n')
                    lbl.pack()  
                    warning.mainloop()
                else:
                    with open(infofile,'a') as f:
                        f.write(nameE.get())
                        f.write('\n')
                        f.write(pwordE.get())
                        f.write('\n')
                        f.close()
                 
                    profileinfo()
                    sign.destroy()
                    otp()
                    

def profileinfo():
    dict={}

    csv_columns = ['uname','password','mobno']
    dict_data = []
    csv_file = "Names.csv"

    name=nameE.get()
    passw=pwordE.get()
    mobno=otpE.get()

    dict['uname']=name
    dict['password']=passw
    dict['mobno']=mobno

    dict_data.append(dict)
    print(dict_data)
    print(dict)
    try:
        with open(csv_file, 'a') as csvfile:
            writer = cv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for data in dict_data:
                writer.writerow(data)
        print('rewev')
    except IOError:
        print("I/O error")
                    
def CheckLogin():
    global un
    global pd
    un=1
    pd=1
    with open(infofile) as f:
        data = f.readlines()
        a=len(data)
        for i in range(0,a,2):
            uname = data[i].rstrip()
            if nameEL.get() == uname:
                un=0
        for j in range(1,a+1,2):
            pword = data[j].rstrip()
            if pwordEL.get() == pword:
                pd=0
        if un==0 and pd==0:
            mainscreen.destroy()
            with open("tempname.txt",'w') as f:
                f.write(uname)
            import welcome
        else:
            warning= Tk()
            warning.title('!Warning!')
            warning.geometry('150x50')
            lbl=Label(warning, text='\n!Invalid Login!\n')
            lbl.pack()
            warning.mainloop()
def otp():
    global otpEL
    global otp
    global otps
    def OTPgen() :  
        string = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        OTP = "" 
        varlen= len(string) 
        for i in range(6) : 
            OTP += string[m.floor(r.random() * varlen)]
        return (OTP)
    
    otp=OTPgen()
    account_sid = sidE.get()
    auth_token = tokenE.get()
    client = Client('AC6fb8ed3e638b26a6f70f2674268dfc51','fe014271c5d0930cd5857b79623c2101')
    message = client.messages.create(body=OTP,from_='+12019755091',to='+918802012379')
    
    otps = Tk()
    otps.geometry("1006x753")  
    otps.title("Verify Number")
    bgimageotp=PhotoImage(file=r"login background(2).png")
    Label(otps,image=bgimageotp).place(relwidth=1,relheight=1)
    
    logoimgotp=PhotoImage(file=r"icon1.png")
    logo=Label(otps,image=logoimgotp)
    logo.place(x=423,y=130)
    
    otpL=Label(otps,bg="#ffffff",text='Enter OTP: ')
    otpEL = Entry(otps,width=30)
    otpL.place(x=355,y=300)
    otpEL.place(x=425,y=300)
    signupimgotp=PhotoImage(file=r"signup.png")
    loginB = Button(otps,bg="#ffffff",image=signupimgotp,height=35,width=100
                    ,command=Checkotp)
    loginB.place(x=435,y=350)
    otps.mainloop()
    
def Checkotp():
    if otpEL.get()==otp:
        otps.destroy()
        main_screen()
    else :
        warning= Tk()
        warning.title('!Warning!')
        warning.geometry('150x50')
        lbl=Label(warning, text='\n!Invalid OTP!\n')
        lbl.pack()
        warning.mainloop()
        
def combine_funcs(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return combined_func
main_screen()
