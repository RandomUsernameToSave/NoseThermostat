import numpy as np
import math as m

mh = 1.67*10**(-27) #kg
mCl = 5.89*10**(-26) #kg
def kinetic_energy(pH,pCl):
    """return the kinetic energy from the normalized momentum of hydrogen and Chlore"""

    #if not (m.isnan((np.linalg.norm(pH)**2 + np.linalg.norm(pCl)**2))):
     #   print(np.linalg.norm(pH)**2 + np.linalg.norm(pCl)**2)
    return (np.linalg.norm(pH)**2 + np.linalg.norm(pCl)**2)

def Morse_force(r,r0):
    return -np.exp(r-r0)*(np.exp(r-r0)-1)

def first_time_differential_first_iteration(X1,X0,deltat):
    """Return a scalar : the first time differential of the quantity X at the iteration 1"""
    return (X1-X0)/deltat

def first_time_differential_first_iteration_vector(X1,X0,deltat):
    """Return a vector : the first time differential of the quantity X at the iteration 1"""
    x = first_time_differential_first_iteration(X1[0],X0[0],deltat)
    y = first_time_differential_first_iteration(X1[1],X0[1],deltat)
    z = first_time_differential_first_iteration(X1[2],X0[2],deltat)

    return np.array([x,y,z])

def first_time_differential_nth_iteration_vector(Xn,Xn_1,Xn_2,deltat):
    """Return a vector : the first time differential of the quantity X at the iteration 1"""
    x = first_time_differential_nth_iteration(Xn[0],Xn_1[0],Xn_2[0],deltat)
    y = first_time_differential_nth_iteration(Xn[1],Xn_1[1],Xn_2[1],deltat)
    z = first_time_differential_nth_iteration(Xn[2],Xn_1[2],Xn_2[2],deltat)

    return np.array([x,y,z])

def first_time_differential_nth_iteration(Xn,Xn_1,Xn_2,deltat):
    """Return a scalar : the first time differential of the quantity X at the iteration n"""
    return (3*Xn-4*Xn_1+Xn_2)/deltat/2

def get_ps_from_ds(s,ds):
    return ds*(1/s)**2

def get_pi_from_vi(vi, Lambda):
    """vi needs to be a numpy array"""
    return vi/Lambda

def np1_iteration_position(R,R_1,s,ps,pi,Lambda,deltat,R0,Rother ,if_morse=False):
    """ps a scalar, pi,R,R_1 numpy arrays
     Rother the position of the other atom """
    norm = np.linalg.norm(R-Rother) # distance of atoms
    e_r = (R-Rother)/norm # the er vector 

    if if_morse:
        x = 2*R[0]-R_1[0]+ (Morse_force(norm,R0)*e_r[0]- s*ps*pi[0]*Lambda)*deltat**2
        y = 2*R[1]-R_1[1]+ (Morse_force(norm,R0)*e_r[1]- s*ps*pi[1]*Lambda)*deltat**2
        z = 2*R[2]-R_1[2]+ (Morse_force(norm,R0)*e_r[2]- s*ps*pi[2]*Lambda)*deltat**2
    else:
        x = 2*R[0]-R_1[0]+ (-(norm-R0)*e_r[0]- s*ps*pi[0]*Lambda)*deltat**2
        y = 2*R[1]-R_1[1]+ (-(norm-R0)*e_r[1]- s*ps*pi[1]*Lambda)*deltat**2
        z = 2*R[2]-R_1[2]+ (-(norm-R0)*e_r[2]- s*ps*pi[2]*Lambda)*deltat**2
    return np.array([x,y,z])


def np1_iteration_s(S,S_1,kinetic_energy,Lambda,deltat,ds,m,M):
    """ """
    s = 2*S- S_1+ (S*Lambda*m/M*(kinetic_energy-1) + 1/S*(ds**2))*deltat**2
    return s
