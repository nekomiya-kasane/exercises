# -*- coding: utf-8 -*-
# import some packages
import numpy as np
import matplotlib.pyplot as plt
import time
def waveFD(c,u0,ut0,delta,dx,tf,dt,mnr,graph):
    
    st = time.time()
    
    # mesh
    xl = -2;
    xr = 2;
    x = np.arange(xl,xr+dx,dx)
    N = len(x)-1
    t =  np.arange(0,tf+dt,dt)
    M = len(t)-1
    c = 1
    q = c*dt/dx
    
    # initial value
    sol = np.zeros((M+1,N+1))
    sol[0,:] = u0(x)
    
    if q>1:
        print("The method is unstable")
    # initial value
    sol = np.zeros((M+1,N+1))
    sol[0,:] = u0(x)
    
    # get f(x),g(x)
    if mnr:
        f = lambda x:(u0(x))*(np.abs(x)<=2)
        g = lambda x:(u0(x))*(np.abs(x)<=2)
    else:
        f = lambda x:(u0(x%8))*(x%8<2)-(u0(4-x%8))*(x%8<=6)*(x%8>=2)+(u0(x%8-8))*(x%8>6)
        g = lambda x:(u0(x%8))*(x%8<2)-(u0(4-x%8))*(x%8<=6)*(x%8>=2)+(u0(x%8-8))*(x%8>6)
    
    # Exact solution
    se = np.zeros((M+1,N+1))
    for n in range(M+1):
        tn = n*dt
        se[n,:] = f(x-c*tn)/2+g(x+c*tn)/2
    
    
    # Numerical solution
    for n in range(M):
        if n==0: # first step
            for j in range(N+1):
                if j==0:
                    if mnr:
                        sol[n+1,j] = q**2*sol[n,j+1]+(1-q**2)*sol[n,j]+ut0(x[j])*dt
                elif j==N:
                    if mnr:
                        sol[n+1,j] = q**2*sol[n,j-1]+(1-q**2)*sol[n,j]+ut0(x[j])*dt
                else:
                    sol[n+1,j] = 1/2*q**2*sol[n,j-1]+(1-q**2)*sol[n,j]+1/2*q**2*sol[n,j+1]+ut0(x[j])*dt
        else:
            for j in range(N+1):
                if j==0:
                    if mnr:
                        sol[n+1,j] = 1/(q+1)*((2-2*q**2)*sol[n,j]+2*q**2(n,j+1)-(1-q)*sol[n-1,j])
                elif j==N:
                    if mnr:
                        sol[n+1,j] = 1/(q+1)*((2-2*q**2)*sol[n,j]+2*q**2(n,j-1)-(1-q)*sol[n-1,j])
                else:
                    sol[n+1,j] = q**2*sol[n,j-1]+(2-2*q**2)*sol[n,j]+q**2*sol[n,j+1]-sol[n-1,j]
    # compute time
    ft = time.time()
    ct = ft-st
    
    # compute the error             
    maep = np.sum(np.abs(sol-se),axis =1)*dx
    maet = np.sum(maep)*dt
     
    if graph != 0:
        plt.figure(2,figsize=(18,6))
        plt.contourf(t,x,np.transpose(sol),50)    
        plt.xlabel('$t$')            
        plt.ylabel('$x$') 
        plt.colorbar()
        plt.xlim([0,tf])
        plt.ylim([xl,xr])
        plt.savefig(str(graph)+'-1.png')
        plt.show()
        
        plt.figure(2,figsize=(18,6))
        plt.contourf(t,x,np.transpose(se),100)    
        plt.xlabel('$t$')            
        plt.ylabel('$x$') 
        plt.colorbar()
        plt.xlim([0,tf])
        plt.ylim([xl,xr])
        plt.savefig(str(graph)+'-2.png')
        plt.show()

        plt.figure(3,figsize=(18,6))
        plt.contourf(t,x,np.transpose(sol-se),100)    
        plt.xlabel('$t$')            
        plt.ylabel('$x$') 
        plt.colorbar()
        plt.xlim([0,tf])
        plt.ylim([xl,xr])
        plt.savefig(str(graph)+'-3.png')
        plt.show()
        
        plt.figure(4,figsize=(18,6))
        plt.plot(t,maep,linewidth = 2)    
        plt.xlabel('$t$')            
        plt.ylabel('$\\varepsilon(t) $') 
        plt.grid()
        plt.xlim([0,tf])
        plt.savefig(str(graph)+'-4.png')
        plt.show()
        
    return x,t,sol,se,ct,maep,maet

## third project
dxvec = [0.2,0.1,0.05,0.025,0.0125];
deltavec = [0.01,0.1,0.5];
errors = []
cts=[]

plt.figure(figsize= (20,10))
for i in range(len(deltavec)):
    delta = deltavec[i]
    errors = []
    cts = []
    for dx in dxvec:
        q = 1
        dt = dx*q
        tf = 10;
        delta = 0.5;
        c = 1;
        u0 = lambda x:np.cos(np.pi*x/(2*delta))*(abs(x)<=delta);
        ut0 = lambda x: x*0;
        mnr = False;
        graph = 0;
        x,t,sol,se,ct,maep,maet = waveFD(c,u0,ut0,delta,dx,tf,dt,mnr,graph)
        errors.append(maet)
        cts.append(ct)
    plt.subplot(2,len(deltavec),i+1)
    plt.loglog(dxvec,errors,'-o')
    plt.title('$\delta$= '+str(delta))
    plt.xlabel('$\Delta t = \Delta x$')  
    plt.grid()          
    plt.ylabel('$E$') 
    
    plt.subplot(2,len(deltavec),i+1+len(deltavec))
    plt.semilogx(dxvec,cts,'-o')
    plt.title('$\delta$= '+str(delta))
    plt.xlabel('$\Delta t = \Delta x$')            
    plt.ylabel('cost time (s)') 
    plt.grid()  
plt.subplots_adjust(wspace = 0.3,hspace = 0.3)
plt.savefig('4-1.png')
plt.show()












