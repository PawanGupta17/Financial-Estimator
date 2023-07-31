# import the library pulp as p 
import pulp as p 

# Create a LP Minimization problem 
Lp_prob = p.LpProblem('Problem', p.LpMinimize) 

# Create problem Variables 
x = p.LpVariable("x", lowBound = 0) # Create a variable x >= 0 
y = p.LpVariable("y", lowBound = 0) # Create a variable y >= 0 

# Objective Function 
Lp_prob += 2.0 * x + 4* y 

# Constraints: 
Lp_prob += 9 * x + 3 * y >= 12
Lp_prob += -1.0*x + y <= 3
Lp_prob += x >= 4
Lp_prob += y <= 4

# Display the problem 
print(Lp_prob) 

status = Lp_prob.solve() # Solver 
print(p.LpStatus[status]) # The solution status 

# Printing the final solution
print("Value of x\t","Value of y\t","Max Value")
print(p.value(x),'\t\t', p.value(y),'\t\t', p.value(Lp_prob.objective)) 
