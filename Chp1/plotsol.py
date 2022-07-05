# Slope field plotting module
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def slope_field_ivp(t, x, diffeq, x0, 
                units = 'xy', 
                angles = 'xy', 
                width = .08, 
                color = 'black',
                ax = None):
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

   x0 : function
        Initial conction
    
    Additional arguments are aesthetic choices passed to pyplot.quiver function
    
    ax : pyplot plotting axes
        Optional existing axis to pass to function

    Returns
    -------
    out : ax
        plotting axis with formatted quiver plot and solution through given initial value
    """
    if (ax is None):
        fig, out = plt.subplots()
    T, X = np.meshgrid(t, x)  # create rectangular grid with points
    slopes = diffeq(X, T)
    dt = np.ones(slopes.shape)  # dt = an array of 1's with same dimension as diffeq
    dxu = slopes / np.sqrt(dt**2 + slopes**2)  # normalize dx
    dtu = dt / np.sqrt(dt**2 + slopes**2)  # normalize dt
    # new lines of code
    # max_value = np.max(t)
    ts = np.linspace(0, 7, 100)
    xsol = odeint(diffeq, x0, ts)  # Solves first order ode with x(0) = x0
    plt.quiver(T, X, dtu, dxu,  # Plot a 2D field of arrows
               units = units,  
               angles = angles,  # each arrow has direction from (t,x) to (t+dt, x+dx)
               width = width,  # sets the width of each arrow from user inputs
               color = color)  # sets the color of each arrow from user inputs
    # new line of code
    plt.plot(ts, xsol, '-', color = 'red')  # plot solution
    out = plt.show
    return out