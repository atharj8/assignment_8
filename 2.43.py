import numpy as np
import matplotlib.pyplot as plt
import math


def line_gen(A,B):
  len =10
  dim = A.shape[0]
  x_AB = np.zeros((dim,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB

#Quadrilateral sides
a = 4
b = 5
c = 4.5

#Co-ordinates of the points A and R are gven below:
p = 4 - 5*math.sin(math.radians(30))
q = 5 * math.cos(math.radians(30))
r = 4 - 5*(math.cos(math.radians(60))) - 4.5*math.cos(math.radians(30))
z = 5 * math.sin(math.radians(60)) - 4.5* math.sin(math.radians(30))

#Coordinates of A and R

print(p,q)
print(r,z)

#vertices
D = np.array([0,0])
E = np.array([4,0])
A = np.array([p,q])
R = np.array([r,z])

#Generating all lines
x_DE = line_gen(D,E)
x_EA = line_gen(E,A)
x_AR = line_gen(A,R)
x_RD = line_gen(R,D)

#Plotting all lines
plt.plot(x_DE[0,:],x_DE[1,:],label='$DE$')
plt.plot(x_EA[0,:],x_EA[1,:],label='$EA$')
plt.plot(x_AR[0,:],x_AR[1,:],label='$AR$')
plt.plot(x_RD[0,:],x_RD[1,:],label='$RD$')

plt.plot(D[0], D[1], 'o')
plt.text(D[0] * (1 - 0.1), D[1] * (1) , 'D')
plt.plot(E[0], E[1], 'o')
plt.text(E[0] * (1 + 0.1), E[1] * (1+0.1) , 'E')
plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1 + 0.03), A[1] * (1 - 0.1) , 'A')
plt.plot(R[0], R[1], 'o')
plt.text(R[0] * (1 + 0.05), R[1] * (1 + 0.01) , 'R')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid()
plt.axis('equal')
plt.plot()
plt.show()