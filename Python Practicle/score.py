from tkinter import *
import mysql.connector as mysq

lst=[('User Name','Score','Number of quizes')]

mydb=mysq.connect(host='localhost',passwd='qwerty',user='root',database='quiz')
mycs=mydb.cursor()
mycs.execute('select * from score')

data = mycs.fetchall()
for i in data:
    lst.append(i)
total_rows = len(lst) 
total_columns = len(lst[0])
root = Tk(className='SCORE')
root.configure(bg='white')

def menu():
    root.destroy()
    import menu

for i in range(total_rows): 
    for j in range(total_columns): 
          
        e = Entry(root, width=20, fg='blue', 
                       font=('Algerian',20,'bold'))
        e.insert(END,lst[i][j])
        e.grid(row=i, column=j)

goback=Button(root,text='go back',bg='white',width=19, fg='blue',font=('Algerian',18,'bold'),command=menu)
goback.grid(row=i+1,column=j-1)
root.mainloop()
