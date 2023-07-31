import mysql.connector as ms
db = ms.connect(host="localhost",user="root",password='qwerty')
cursor = db.cursor()
cursor.execute("Create Database Company")
cursor.execute("Use Company")
cursor.execute("create table employee(eid varchar(3) primary key,ename varchar(30), salary decimal(10,2))")
def menu():
    c='y'
    while (c=='y'):
        print ("1. add record")
        print ("2. update record ")
        print ("3. delete record")
        print("4. display records")
        print("5. Exiting")
        choice=int(input("Enter your choice: "))
        if choice == 1:
            adddata()
        elif choice== 2:
            updatedata()
        elif choice== 3:
            deldata()
        elif choice== 4:
            fetchdata()
        elif choice == 5:
            print("Exiting")
            break
    else:
        print("wrong input")

    c=input("Do you want to continue or not: ")
def fetchdata():
    try:
        cursor.execute("SELECT * FROM employee" )
        results = cursor.fetchall()
        for x in results:
            print(x)
    except:
        print ("Error: unable to fetch data")
        
def adddata():
    cursor.execute("INSERT INTO employee VALUES('A01','Ritu',50000)")
    cursor.execute("INSERT INTO employee VALUES('A02','Ankush',60000)")
    db.commit()
    print("Records added") 
        

def updatedata():
    try:
        sql = ("Update employee set salary=salary+5000 where ename='Ritu'")
        cursor.execute(sql)
        print("Record Updated")
        db.commit()
    except Exception as e:
        print (e)
        
def deldata():
    sql = "delete from employee where ename='Ritu'"
    cursor.execute(sql)
    print("Record Deleted")
    db.commit()
