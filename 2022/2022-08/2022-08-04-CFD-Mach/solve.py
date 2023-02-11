
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

import math

M_inf = 1.3
gamma=1.4
U_inf=1

def BC_F(x):
    pi = np.pi
    beta = 0.1
    
    if x < 1 or x > 2:
        return 0.0
    else:
        return U_inf*beta *pi* np.cos(pi*(x-1))
    
def error(phi):   # calculate to what extent the eq are not being satisfied. if = 0, we solved it.
    newphi = phi.copy()
    Nx = newphi.shape[0]
    Ny = newphi.shape[1]
    err = 0.0
    for i in range(2,Nx-1):
        for j in range(1,Ny-1):
            A_x = 1 - M_inf * M_inf-(gamma+1)*M_inf*M_inf*(newphi[i,j]-newphi[i-2,j])/(2*h) #what value is h?
            
            B_y=1
            
            C0 = A_x-2*B_y
            eq = - C0 * newphi[i,j] + (-B_y * newphi[i,j+1] - B_y * newphi[i,j-1] +2*A_x*newphi[i-1,j]-
                        A_x * newphi[i-2,j])

            
            err += abs(eq)

    return err/(Nx*Ny)
    
def velocity_vec(phi):
    U = np.zeros((phi.shape[0]-2, phi.shape[1]-2))
    V = np.zeros((phi.shape[0]-2, phi.shape[1]-2))

    print(U.shape, V.shape)
    
    hx = 1/phi.shape[0]
    hy = 1/phi.shape[1]
                 
    for i in range(1,phi.shape[0]-1):
        for j in range(1,phi.shape[1]-1):
            U[i-1,j-1] = 0.5 * (phi[i+1,j] - phi[i-1,j])/hx    #  U = DP/Dx
            V[i-1,j-1] = 0.5 * (phi[i,j+1] - phi[i,j-1])/hy     # V = Dp/Dy 
    return U,V

def SOR(phi):
    h = 3.0 / phi.shape[0] 
    newphi = phi.copy()
    sor = 1.    # sor = 12 is Gauss-eidel relation
    
    for i in range(2,newphi.shape[0]-1):
        for j in range(1,newphi.shape[1]-1):
            A_x = 1 - M_inf * M_inf-(gamma+1)*M_inf*M_inf*(newphi[i,j]-newphi[i-2,j])/(2*h)
            
            B_y=1
            
            C0 = A_x-2*B_y

            dp = -newphi[i,j] - (B_y * newphi[i,j+1] + B_y * newphi[i,j-1] -2*A_x*newphi[i-1,j]+
                        A_x * newphi[i-2,j])/C0
            newphi[i,j] += sor * dp

        j = 0
        for i in range(2,newphi.shape[0]-1):
            A_x = 1 - M_inf * M_inf - (gamma+1)*M_inf*M_inf*(newphi[i,j]-newphi[i-2,j])/(2*h)
            
            B_y=1
            
            C0 = A_x-2*B_y
            
            dp = -newphi[i,j] -  (2*B_y * newphi[i,j+1] -2*A_x*newphi[i-1,j]+
                        A_x * newphi[i-2,j]-2*h*BC_F(i*h))/C0

            newphi[i,j] += sor * dp
    
    return newphi


N = 32
phi = np.zeros((3*N,N))
U_inf=1
h = 1 / N


#  x = i * h
# y = j * h

for i in range(3*N):
    for j in range(N):
        phi[i,j] = U_inf * i * h 


for iter in range(5001):
    phi = SOR(phi)
    if iter % 100 == 0:
        print(iter, error(phi)) 

U,V = velocity_vec(phi)
x = np.linspace(0, 3, 94)
y = np.linspace(0,1, 30)
X ,Y = np.meshgrid(x,y)

plt.streamplot(X,Y,np.transpose(U),np.transpose(V), density = 0.5)
plt.show()

dim = [phi.shape[0]-2, phi.shape[1]-2]

mach = np.zeros((dim[0],dim[1]))
for i in range(dim[0]):
    for j in range(dim[1]):
        mach[i,j] = math.sqrt(U[i,j] * U[i,j] + V[i,j] * V[i,j])

plt.contour(X,Y, np.transpose(mach))
plt.show()