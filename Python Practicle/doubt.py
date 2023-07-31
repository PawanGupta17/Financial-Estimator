import pulp as p
import matplotlib.pyplot as plt
import numpy as np

mm=input('Enter(MIN) to minimize  and  (MAX) to maximise')

def menu():
    import menu
if mm.upper()=='MIN':
    Lp_prob = p.LpProblem('Problem', p.LpMinimize) 

    x = p.LpVariable("x", lowBound = 0) 
    y = p.LpVariable("y", lowBound = 0) 
    print(30*'*','MENU',30*'*')
    print('Objective Function-->(aX+bY=z)')
    print('Following are types of Constraints')
    print('1.)aX+bY>=c')
    print('2.)aX+bY<=c')
    print('3.)X>=c & Y<=c1')
    print('4.)X<=c & Y>=c1')
    objx=float(input('Enter coefficient of "X" for objective function'))
    objy=float(input('Enter coefficient of "Y" for objective function'))
    Lp_prob += objx * x + objy* y
    n=int(input("Enter number of constraints"))
    for i in range (0,n):
        ch=int(input("Enter your choice of constraint"))
        if ch==1:
            consx=float(input('Enter coefficient of "X"'))
            consy=float(input('Enter coefficient of "Y"'))
            consc=float(input('Enter constant'))
            Lp_prob += consx * x + consy * y>=consc
            
        elif ch==2:
            consx1=float(input('Enter coefficient of "X"'))
            consy1=float(input('Enter coefficient of "Y"'))
            consc1=float(input('Enter constant'))
            Lp_prob += consx1 * x + consy1 * y<=consc1
            
        elif ch==3:
            conscx=float(input('Enter constant of "X"'))
            conscy=float(input('Enter constant of "Y"'))
            Lp_prob += x >=conscx
            Lp_prob += y <=conscy

        elif ch==4:
            conscx=float(input('Enter constant of "X"'))
            conscy=float(input('Enter constant of "Y"'))
            Lp_prob += x <=conscx
            Lp_prob += y >=conscy

    print(Lp_prob) 

    status = Lp_prob.solve() 
    print(p.LpStatus[status])

    print("Value of x\t","Value of y\t","Max Value")
    print(p.value(x),'\t\t', p.value(y),'\t\t', p.value(Lp_prob.objective))
    enter=input("Press enter to see its graph")
    
elif mm.upper()=='MAX':
    Lp_prob = p.LpProblem('Problem', p.LpMaximize) 

    x = p.LpVariable("x", lowBound = 0)  
    y = p.LpVariable("y", lowBound = 0) 
    print(30*'*','MENU',30*'*')
    print('Objective Function-->(aX+bY=z)')
    print('Following are types of Constraints')
    print('1.)aX+bY>=c')
    print('2.)aX+bY<=c')
    print('3.)X>=c & Y<=c1')
    print('4.)X<=c & Y>=c1')
    objx=float(input('Enter coefficient of "X" for objective function'))
    objy=float(input('Enter coefficient of "Y" for objective function'))
    Lp_prob += objx * x + objy* y
    n=int(input("Enter number of constraints"))
    for i in range (0,n):
        ch=int(input("Enter your choice of constraint"))
        if ch==1:
            consx=float(input('Enter coefficient of "X"'))
            consy=int(input('Enter coefficient of "Y"'))
            consc=float(input('Enter constant'))
            Lp_prob += consx * x + consy * y>=consc
            
        elif ch==2:
            consx1=float(input('Enter coefficient of "X"'))
            consy1=int(input('Enter coefficient of "Y"'))
            consc1=float(input('Enter constant'))
            Lp_prob += consx1 * x + consy1 * y<=consc1
            
        elif ch==3:
            conscx=float(input('Enter constant of "X"'))
            conscy=int(input('Enter constant of "Y"'))
            Lp_prob += x >=conscx
            Lp_prob += y <=conscy

        elif ch==4:
            conscx1=float(input('Enter constant of "X"'))
            conscy1=float(input('Enter constant of "Y"'))
            Lp_prob += x <=conscx1
            Lp_prob += y >=conscy1

    print(Lp_prob) 

    status = Lp_prob.solve() 
    print(p.LpStatus[status]) 

    print("Value of x\t","Value of y\t","Max Value")
    print(p.value(x),'\t\t', p.value(y),'\t\t', p.value(Lp_prob.objective))
    enter=input("Press enter to see its graph")
    
def graph():
    x = np.array(range(-10,10))
    y = np.array((consc-consx * x)/consy)
    plt.plot(x,y)

    x1 = np.array(range(-10,10))
    y1 = np.array((consc1-consx1 * x)/consy1)
    plt.plot(x1,y1)

    try:
        x2 = np.array(conscx)
        for i in range(20):
            x2 = np.append(x2,conscx)   
        x2 = np.delete(x2, 0)
        y2 = np.array(range(-10,10))
        plt.plot(x2,y2)

        y3 = np.array(conscy)
        for i in range(20):
            y3 = np.append(y3,conscy)   
        y3 = np.delete(y3, 0)
        x3 = np.array(range(-10,10))
        plt.plot(x3,y3)
    except NameError:
        x2 = np.array(conscx1)
        for i in range(20):
            x2 = np.append(x2,conscx1)   
        x2 = np.delete(x2, 0)
        y2 = np.array(range(-10,10))
        plt.plot(x2,y2)

        y3 = np.array(conscy1)
        for i in range(20):
            y3 = np.append(y3,conscy1)   
        y3 = np.delete(y3, 0)
        x3 = np.array(range(-10,10))
        plt.plot(x3,y3)
        
    plt.show()
    m=input("Press enter to go back to menu")
    menu()
graph()
