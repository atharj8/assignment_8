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
c = 6.5

#Co-ordinates of the points C and D are gven below:
p = 4 + 5*math.cos(math.radians(75))
q = 5*math.sin(math.radians(75))
r = 4 + 5*(math.cos(math.radians(75))) - 6.5* math.cos(math.radians(5))
z = 5* math.sin(math.radians(75)) + 6.5* math.sin(math.radians(5))

#vertices
A = np.array([0,0])
B = np.array([4,0])
C = np.array([p,q])
D = np.array([r,z])

#Generating all lines
x_AB = line_gen(A,B)
x_BC = line_gen(B,C)
x_CD = line_gen(C,D)
x_DA = line_gen(D,A)

#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')
plt.plot(x_CD[0,:],x_CD[1,:],label='$CD$')
plt.plot(x_DA[0,:],x_DA[1,:],label='$DA$')

plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1 - 0.1), A[1] * (1) , 'A')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1 + 0.1), B[1] * (1+0.1) , 'B')
plt.plot(C[0], C[1], 'o')
plt.text(C[0] * (1 + 0.03), C[1] * (1 - 0.1) , 'C')
plt.plot(D[0], D[1], 'o')
plt.text(D[0] * (1 + 0.05), D[1] * (1 + 0.01) , 'D')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid()
plt.axis('equal')
plt.plot()
plt.show()