# Slope field plotting module
import numpy as np
import matplotlib.pyplot as plt

def slope_field(t, x, diffeq, 
                units = 'xy', 
                angles = 'xy', 
                width = .08, 
                color = 'black'):
    """Plots slope field given an ode
    
    Given an ode of the form: dx/dt = f(x, t), plot a slope field (aka direction field) for given t and x arrays. 
    Extra arguments are passed to matplotlib.pyplot.quiver

    Parameters
    ----------
    
    t : array
        The time data range
        
    x : array
        The x data range
    
    diffeq : function
        The function f(x,t) = dx/dt
    
    Additional arguments are aesthetic choices passed to pyplot.quiver function

    Returns
    -------
    out : plot
        generates a quiver plot
    """
    T, X = np.meshgrid(t, x)  # create rectangular grid with points
    dt = np.ones(diffeq.shape)  # dt = an array of 1's with same dimension as dx
    dxu = diffeq / np.sqrt(dt**2 + diffeq**2)  # normalize diffeq
    dtu = dt / np.sqrt(dt**2 + diffeq**2)  # normalize dt
    plt.quiver(T, X, dtu, dxu,  # Plot a 2D field of arrows
               units = units,  
               angles = angles,  # each arrow has direction from (t,x) to (t+dt, x+dx)
               width = width,  # sets the width of each arrow from user inputs
               color = color)  # sets the color of each arrow from user inputs
    return plt.show()