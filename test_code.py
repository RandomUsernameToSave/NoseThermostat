import numpy as np


def harmonic_pot(x, m=1, omega=1):
    '''
    The harmonic potential
    '''

    return 0.5 * m * omega**2 * x**2

def harmonic_for(x, m=1, omega=1):
    '''
    The force of harmonic potential
    '''

    return - m * omega**2 * x

def Ekin(v, m=1):
    '''
    The force of harmonic potential
    '''

    return 0.5 * m * v**2

def log(x, v, m=1, omega=1):
    '''
    '''

    print("{:20.8E} {:20.8E} {:20.8E} {:20.8E} {:20.8E}".format(
        x, v,
        Ekin(v, m), 
        harmonic_pot(x, m, omega),
        harmonic_pot(x, m, omega) + Ekin(v, m)
    ))



def nose_hoover(x0, v0, T, Q, f0=None, m=1, omega=1, dt=0.01, nsteps=1000):
    '''
    Velocity Verlet integration for Langevin thermostat
    '''

    if f0 is None:
        f0 = harmonic_for(x0, m, omega)

    log(x0, v0, m, omega)

    eta0 = 0

    # 0, 1, 2 represents t, t + 0.5*dt, and t + dt, respectively
    for ii in range(nsteps):
        x2   = x0 + v0 * dt + 0.5 * dt**2 * (f0 / m - eta0 * v0)
        v1   = v0 + 0.5 * dt * (f0 / m - eta0 * v0) # speed calculcation
        f2   = harmonic_for(x2, m, omega)  # force calculation
        eta1 = eta0 + (dt / 2 / Q) * (0.5 * m * v0**2 - 0.5 * T)
        eta2 = eta1 + (dt / 2 / Q) * (0.5 * m * v1**2 - 0.5 * T)
        v2   = (v1 + 0.5 * dt * f2 / m) / (1 + 0.5 * dt * eta2)

        log(x2, v2, m, omega)
        x0, v0, f0 = x2, v2, f2


if __name__ == "__main__":
    T0 = 0.1
    v0 = np.sqrt(2*T0) * 2
    x0 = 0.0
    dt = 0.1
    N  = 20000

    nose_hoover(x0, v0, T=T0, Q=0.1, dt=0.1, nsteps=N)

