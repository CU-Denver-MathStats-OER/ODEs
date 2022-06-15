# Slope field plotting module
import numpy as np
import matplotlib.pyplot as plt

def slope_field(t, x, diffeq, 
                units = 'xy', 
                angles = 'xy', 
                width = .08, 
                color = 'black'):
    T, X = np.meshgrid(t, x)  # create rectangular grid with points
    dt = np.ones(diffeq.shape)  # dt = an array of 1's with same dimension as dx
    dxu = diffeq / np.sqrt(dt**2 + diffeq**2)  # normalize diffeq
    dtu = dt / np.sqrt(dt**2 + diffeq**2)  # normalize dt
    plt.quiver(T, X, dtu, dxu,  # Plot a 2D field of arrows
               units = 'xy',  
               angles = 'xy',  # each arrow has direction from (t,x) to (t+dt, x+dx)
               width = .08,  # sets the width of each arrow
               color = 'black')  # sets the color of each arrow
    return plt.show()