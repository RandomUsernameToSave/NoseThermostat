import numpy as np
import matplotlib.pyplot as plt 
import utils.utils as u
import math as m
import utils.utils_display as u_display

N = 2000
# M = m.inf
D = 4.6141*1.6*10**(-19) #eV
alpha = 1.81*10**(10) # m-1
r0 = 1.275*10**(-10) #m
kb = 1.38*10**(-23) # usi
mh = 1.67*10**(-27) #kg
mCl = 5.89*10**(-26) #kg
T0 = 500 # K

R0 = alpha*r0

Lambda = np.sqrt(3/2*kb*T0/D) #lambda parameter
deltat = 0.01
x0 = 3*np.random.rand(3)
y0 = 3*np.random.rand(3)
vH = [np.random.rand(3)]
vCl = [np.random.rand(3)]
s = [0.4,0.4]
TimeScale = np.sqrt(mh/D/2)/alpha 

M = m.inf #mCl*1 #m.inf  #2*6*kb*T0*(TimeScale)**2
print(M)
rCl = [x0,x0+np.random.rand(3)]
rH = [y0,y0+np.random.rand(3)]

vH = u.first_time_differential_first_iteration_vector(rH[1],rH[0],deltat)
vCl = u.first_time_differential_first_iteration_vector(rCl[1],rCl[0],deltat)
ds = u.first_time_differential_first_iteration(s[1],s[0],deltat)

ps = u.get_ps_from_ds(s[1],ds)
pH = u.get_pi_from_vi(vH,Lambda)
pCl = u.get_pi_from_vi(vCl,Lambda)
kine_energy = u.kinetic_energy(pH,pCl)

s.append(u.np1_iteration_s(s[1],s[0],kine_energy,Lambda,deltat,ds,mh,M))
rCl.append(u.np1_iteration_position(rCl[1],rCl[0],s[1],ps,pCl,Lambda,deltat,R0,rH[-1]))
rH.append(u.np1_iteration_position(rH[1],rH[0],s[1],ps,pH,Lambda,deltat,R0,rCl[-2]))

for i in range(N):
    vH = u.first_time_differential_nth_iteration_vector(rH[-1],rH[-2],rH[-3],deltat)
    vCl = u.first_time_differential_nth_iteration_vector(rCl[-1],rCl[-2],rCl[-3],deltat)
    ds = u.first_time_differential_nth_iteration(s[-1],s[-2],s[-3],deltat)

    ps = u.get_ps_from_ds(s[-1],ds)
    pH = u.get_pi_from_vi(vH,Lambda)
    pCl = u.get_pi_from_vi(vCl,Lambda)
    kine_energy = u.kinetic_energy(pH,pCl)


    s.append(u.np1_iteration_s(s[-1],s[-2],kine_energy,Lambda,deltat,ds,mh,M))
    rCl.append(u.np1_iteration_position(rCl[-1],rCl[-2],s[-1],ps,pCl,Lambda,deltat,R0,rH[-1]))
    rH.append(u.np1_iteration_position(rH[-1],rH[-2],s[-1],ps,pH,Lambda,deltat,R0,rCl[-2]))

#plt.plot(rCl)
#plt.legend(['x'])
#plt.plot(s)
#plt.show()

u_display.plot_3d_trajectory_animation_with_balls(np.transpose(np.array(rH)),np.transpose(np.array(rCl)),s)
