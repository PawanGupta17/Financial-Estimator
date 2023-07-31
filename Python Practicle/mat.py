import matplotlib.pyplot as plt
import numpy as np

x = np.array(range(10))
y = np.array(3+x)
plt.plot(x,y)

x1 = np.array(range(10))
y1 = np.array((12-9*x)/3)
plt.plot(x1,y1)

x2 = np.array(4)
for i in range(20):
    x2 = np.append(x2,4)   
x2 = np.delete(x2, 0)
y2 = np.array(range(-10,10))
plt.plot(x2,y2)

y3 = np.array(4)
for i in range(20):
    y3 = np.append(y3,4)   
y3 = np.delete(y3, 0)
x3 = np.array(range(-10,10))
plt.plot(x3,y3)

x4 = np.array(range(0,5))
y4 = np.array((12-9*x4)/3)
y5 = np.array(3+x4)
for i in y5:
    if i<=4:
        y6=i
        plt.fill_between(x4, y4, y6,color="#FCFF9B")

plt.show()
