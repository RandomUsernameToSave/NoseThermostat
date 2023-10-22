import numpy as np
import matplotlib.pyplot as plt 

D = 4.6141 #eV
alpha = 1.81*10**(10) # m-1
r0 = 1.275*10**(-10) #m
kb = 1.38*10**(-23) # usi
mh = 1


def verlet_speed(rj,rj_1,rj_2,deltat):
    return (3*rj-4*rj_1+rj_2)/2/deltat

def verlet_force(dU,s,ps,pi,M):
    """pi is an array
    (er,e theta, ephi)"""
    return -dU- s*ps*pi

def potential(r,potential_type="harmonic",D=D,alpha=alpha,r0=r0, derivation=True):

    if derivation:
        if potential_type == "morse":
            return -2*D*alpha*np.exp(-alpha*(r-r0))*(np.exp(-alpha*(r-r0))-1)
        else : 
            return 2*D*alpha**2*(r-r0)
        
    if potential_type == "morse":
        return D*(np.exp(-alpha*(r-r0))-1)**2
    else : 
        return D*alpha**2*(r-r0)**2

def verlet_position(rj,rj_1,fi,m,deltat):
    rr = 2*rj-rj_1+fi/m*deltat**2
    return rr

def vitesse(sp1,s_1,deltat):
    return (sp1-s_1)/2/deltat

def s_evolution_equation(s,s_1,s_2,p1,m1,p2,m2,T,M,N,deltat):
    ds = (3*s-4*s_1+s_2)/(2*deltat)
    return 2*s-s_1+s/M*(p1**2/m1+p2**2/m2-3*N*kb*T)+1/s*ds**2

def ps_evolution(s,s_1,s_2,M,deltat):
    ds = (3*s-4*s_1+s_2)/(2*deltat)
    ps = M/s*ds
    return ps


def nose_thermostat(x0,v0,deltat,potential_type,M,NumberIteration,T):
    X= np.array([x0,x0])
    V = np.array([v0])
    S = np.array([1/2,1/2,1/2])


    v1 = (X[1]-X[0])/deltat
    V = np.append(V,v1)

    ps = ps_evolution(S[2],S[1],S[0],M,deltat)
    pi = mh*v1
    f1 = verlet_force(potential(X[1],potential_type),S[0],ps,pi,M)
    s = s_evolution_equation(S[2],S[1],S[0],pi,mh,0,1,T,M,2,deltat)
    S = np.append(S,s)
    x = verlet_position(X[1],X[0],f1,mh,deltat)
    X = np.append(X,x)
    for n in range(2,NumberIteration):
        v1 = verlet_speed(X[n],X[n-1],X[n-2],deltat)
        V= np.append(V,v1)

        ps = ps_evolution(S[n],S[n-1],S[n-2],M,deltat)
        pi = mh*v1
        f1 = verlet_force(potential(X[n],potential_type),S[n],ps,pi,M)
        s = s_evolution_equation(S[2],S[1],S[0],pi,mh,0,1,T,M,2,deltat)
        S = np.append(S,s)
        x= verlet_position(X[1],X[0],f1,mh,deltat)
        X = np.append(X,x)
    plt.plot(X)
    plt.show()

nose_thermostat(r0*2,0,10**(-4),"harmonic",1,500,300)


