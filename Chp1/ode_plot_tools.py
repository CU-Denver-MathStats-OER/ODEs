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
    
    Given an ode of the form: dx/dt = f(t, x), plot a slope field (aka direction field) for given t and x arrays. 
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
    slopes = diffeq(T, X)
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


def plot_sol(t, x, diffeq, x_0, ax = None, npts=100, clear=False):
    """Plot Slope field and estimated solution given initial conidtion
    
    Given an ode of the form: dx/dt = f(t, x), plot a slope field (aka direction field) for given t and x arrays. 
    Given an initial condition x_0, plot a solution line estimated with `odeint`.
    Extra arguments are passed to matplotlib.pyplot.quiver

    Parameters
    ----------
    
    t : array
        The independent variable range
        
    x : array
        The dependent variable range
    
    diffeq : function
        The function f(t,x) = dx/dt

    x_0 : float
        Initial condition at t[0]
        
    ax : pyplot plotting axes
    
    args:
        Additional arguments are aesthetic choices passed to pyplot.quiver function
    

    Returns
    -------
    out : ax
        plotting axis with formatted quiver plot
    """
    
    if (ax is None):
        fig, ax = plt.subplots()
    if clear:
        ax.cla()

    slope_field(t, x, diffeq, color='grey', ax = ax)
    
    # Plot solution
    tt = np.linspace(t.min(),t.max(),100)
    sol = odeint(diffeq, x_0, tt, tfirst=True)
    
    xlim = ax.get_xlim()
    ylim = ax.get_ylim()
    
    ax.plot(tt, sol)
    
    ax.set_xlim(xlim)
    ax.set_ylim(ylim)
    
    plt.show()
    return ax
    
    
# Plot Slope field and solution given analytical solution
def plot_dt(t, x, diffeq, t_0, x_0, dt, nsteps, ax=None, npts=100, clear=False):
    
    if (ax is None):
        fig, ax = plt.subplots()
    if clear:
        ax.cla()
    slope_field(t, x, diffeq, color='grey', ax = ax)
    
    # Store limits to keep approx from changing
    xlim = ax.get_xlim()
    ylim = ax.get_ylim()
    
    # Plot vector
    # scale=1/dt makes the vector 
    tt = np.linspace(t_0, t_0+dt*(nsteps-1), nsteps)
    xx = forward_euler(diffeq, dt, nsteps, t[0], x_0)
    
    for i in range(0, nsteps):
        slope_field(tt[i], xx[i], diffeq, scale=dt, ax = ax)  
    
    ax.set_ylim(ylim)
    ax.set_xlim(xlim)
    plt.show()
    return ax

# Euler Methods
def forward_euler(f, dt, n, t_0, x_0):
    # Assuming f is passed as a function of (t, x)
    v = np.zeros(n+1)  # set each x_i by 0 at first
    v[0] = x_0  # set first value to x_0
    
    for i in range(0, n):
        v[i+1] = v[i] + dt * f(t_0 + i*dt, v[i])  # Euler's method formula
    return v


# Plot Slope field and solution given analytical solution
def plot_euler(t, x, diffeq, t_0, x_0, dt, n=None, ax=None, clear=False):
    
    if (ax is None):
        fig, ax = plt.subplots()
    if clear:
        ax.cla()

    slope_field(t, x, diffeq, color='grey', ax = ax)

    # Plot exact
    tt = np.linspace(t_0,t.max(),100)
    sol = odeint(diffeq, x_0, tt, tfirst=True)
    ax.plot(tt, sol)
    
    # Store limits to keep approx from changing
    xlim = ax.get_xlim()
    ylim = ax.get_ylim()
    
    # Plot approx
    if n is None:
        n = int(t[-1]/dt)
    tt2 = np.linspace(t_0, n*dt, n+1)
    ax.plot(tt2, forward_euler(diffeq, dt, n, t[0], x_0), ':', 
             marker='s')
    ax.set_ylim(ylim)
    ax.set_xlim(xlim)
    plt.show()
    return ax