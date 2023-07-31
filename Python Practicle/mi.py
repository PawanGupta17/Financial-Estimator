import mysql.connector as mysq
mydb=mysq.connect(host="localhost",user="root",passwd="qwerty")
mycursor=mydb.cursor()
mycursor.execute("use practice;")
mycursor.execute("select * from school where std_name='Pawan Gupta'")
print(mycursor)
for x in mycursor:
    print (x,end='')
