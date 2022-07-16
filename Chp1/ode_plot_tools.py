## Python file contains code for generating slope fields and interactive plots

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def slope_field(t, x, diffeq, 
                units = 'xy', 
                angles = 'xy',
                scale_units = 'x',
                scale = None, 
                color = 'black',
                ax = None,
                **args):
    """Plots slope field given an ode
    
    Given an ode of the form: dx/dt = f(x, t), plot a slope field (aka direction field) for given t and x arrays. 
    Extra arguments are passed to matplotlib.pyplot.quiver

    Parameters
    ----------
    
    t : array
        The independent variable range
        
    x : array
        The dependent variable range
    
    diffeq : function
        The function f(t,x) = dx/dt

    args:
        Additional arguments are aesthetic choices passed to pyplot.quiver function
    
    ax : pyplot plotting axes
        Optional existing axis to pass to function

    Returns
    -------
    out : ax
        plotting axis with formatted quiver plot
    """
    if (ax is None):
        fig, ax = plt.subplots()
    if scale is not None:
        scale = 1/scale
    T, X = np.meshgrid(t, x)  # create rectangular grid with points
    slopes = diffeq(X, T)
    dt = np.ones(slopes.shape)  # dt = an array of 1's with same dimension as diffeq
    dxu = slopes / np.sqrt(dt**2 + slopes**2)  # normalize dx
    dtu = dt / np.sqrt(dt**2 + slopes**2)  # normalize dt
    ax.quiver(T, X, dtu, dxu,  # Plot a 2D field of arrows
               units = units,  
               angles = angles,  # each arrow has direction from (t,x) to (t+dt, x+dx)
               scale_units = 'x',
               scale = scale,  # sets the length of each arrow from user inputs
               color = color,
               **args)  # sets the color of each arrow from user inputs
    
    return ax


def plot_sol(t, x, diffeq, x0, ax, npts=100, clear=False):
    """Plot Slope field and estimated solution given initial conidtion
    
    Given an ode of the form: dx/dt = f(x, t), plot a slope field (aka direction field) for given t and x arrays. 
    Given an initial condition x0, plot a solution line estimated with `odeint`.
    Extra arguments are passed to matplotlib.pyplot.quiver

    Parameters
    ----------
    
    t : array
        The independent variable range
        
    x : array
        The dependent variable range
    
    diffeq : function
        The function f(t,x) = dx/dt

    x0 : float
        Initial condition
        
    ax : pyplot plotting axes
    
    args:
        Additional arguments are aesthetic choices passed to pyplot.quiver function
    

    Returns
    -------
    out : ax
        plotting axis with formatted quiver plot
    """
    
    if clear:
        ax.cla()

    slope_field(t, x, diffeq, color='grey', ax = ax)
    
    # xlim = ax.get_xlim()
    # ylim = ax.get_ylim()
    
    # Plot solution
    tt = np.linspace(t.min(),t.max(),100)
    sol = odeint(diffeq, x0, tt)
    ax.plot(tt, sol)
    xlim = ax.get_xlim()
    ylim = ax.get_ylim()
    
    # ax.set_ylim(ylim)
    # ax.set_xlim(xlim)
    
    plt.show()
    
    
# Plot Slope field and solution given analytical solution
def plot_dt(t, x, diffeq, t0, x0, dt, nsteps, npts=100, clear=False):
    fig, ax = plt.subplots(1,1)
    if clear:
        ax.cla()
    slope_field(t, x, diffeq, color='grey', ax = ax)
    
    # Store limits to keep approx from changing
    xlim = ax.get_xlim()
    ylim = ax.get_ylim()
    
    # Plot vector
    # scale=1/dt makes the vector 
    tt = np.linspace(t0, t0+dt*(nsteps-1), nsteps)
    xx = forward_euler(diffeq, dt, nsteps, t[0], x0)
    
    # slope_field(t0, x0, diffeq, scale=dt, ax = ax)  
    for i in range(0, nsteps):
        slope_field(tt[i], xx[i], diffeq, scale=dt, ax = ax)  
    
    ax.set_ylim(ylim)
    ax.set_xlim(xlim)
    plt.show()
    

# Euler Methods
def forward_euler(f, Delta_t, n, start_t, y_0):
    # Assuming f is passed as a function of (y, t)
    v = np.zeros(n+1)  # set each y_i by 0 at first
    v[0] = y_0  # set first value to y_0
    
    for i in range(0, n):
        v[i+1] = v[i] + Delta_t * f(v[i], start_t + i*Delta_t)  # Euler's method formula
    return v


# Plot Slope field and solution given analytical solution
def plot_euler(t, x, diffeq, x0, dt, ax, clear=False):
    
    if clear:
        ax.cla()

    slope_field(t, x, diffeq, color='grey', ax = ax)

    # Plot exact
    tt = np.linspace(t.min(),t.max(),100)
    sol = odeint(diffeq, x0, tt)
    ax.plot(tt, sol)
    
    # Store limits to keep approx from changing
    xlim = ax.get_xlim()
    ylim = ax.get_ylim()
    
    # Plot approx
    n = int(t[-1]/dt)
    tt2 = np.linspace(t[0], t[-1], n+1)
    ax.plot(tt2, forward_euler(diffeq, dt, n, t[0], x0), ':', 
             marker='s')
    ax.set_ylim(ylim)
    ax.set_xlim(xlim)
    plt.show()
