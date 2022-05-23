# Slope field plotting module
import numpy as np
import matplotlib.pyplot as plt

# Test function
def slope_field(ax, t, x, fxt, 
                param_dict={'angles':'xy', 'scale_units':'xy', 'scale':2, 'headlength':0, 'headwidth':1}):
    """Plots slope field given an ode
    
    Given an ode of the form: dx/dt = f(x, t), plot a slope field (aka direction field) for given t and x arrays. 
    Extra arguments are passed to matplotlib.pyplot.quiver

    Parameters
    ----------
    ax: Axes
        The axes to draw to
        
    t : array
        The time data range
        
    x : array
        The x data range
    
    fxt : function
        The function f(x,t) = dx/dt
    
    param_dict: dict
        Dictionary of keyword arguments to pass to ax.plot. Default values chosen to match typical slope field aesthetic

    Returns
    -------
    out : list
        a list of artists added
    """
    
    # Create Grid of Points
    T, X = np.meshgrid(t,x)
    
    # Calculate slopes for given array values
    dXdT = fxt(T,X)
    U = (1/(1+dXdT**2)**.5)*np.ones(T.shape)
    V = (1/(1+dXdT**2)**.5)*dXdT
    
    out = ax.quiver(T, X, U, V, **param_dict)
    ax.set_title('Slope Field')
    ax.set_xlabel('Time')
    ax.set_ylabel('X')
    
    return out