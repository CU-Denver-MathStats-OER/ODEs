import matplotlib
from matplotlib import pyplot as plt
from matplotlib.patches import Circle, Rectangle
from matplotlib.collections import PatchCollection
from matplotlib.animation import FuncAnimation
from IPython.display import HTML
import numpy as np
from scipy import signal
from scipy.integrate import odeint

# System Functions

## External forcing $A cos(\omega t)$, set $A=0$ to make problem homogeneous
def forcing(t, A=0, omega=1):
    return A*np.cos(omega*t)

## Diffeq returns (x', x''), with algebraic expression for x'' solved above
def diffeq(t, u, m, k, b, A=0, omega=1):
    return (u[1], -b/m*u[1]-k/m*u[0]+forcing(t, A, omega))

def damped_harmonic_oscillator(m=0.2, b=0.1, k=1, x0=[-2, 0], 
                               A=0, omega=1, fps=3, tf=30):
        
    nframe = fps*tf # Setup number of frames for animation

    ts=np.linspace(0, tf, nframe)  # time to evaluate solution

    # Setup and solve 1d system with odeint
    us = odeint(diffeq, x0, ts, tfirst=True, args=(m, k, b, A, omega)) 
    xs = us[:,0]

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12,8), gridspec_kw={'height_ratios': [3, 2]})

    # Outer wheel for flywheel
    r1 = 1.25
    x1 = 0
    y1 = 0
    circles = []
    circle = Circle((x1, y1), r1, animated=True, color='b', alpha=0.25)
    circles.append(circle)

    # inner wheel for flywheel
    r2 = 0.25
    x2 = 0.75
    y2 = 0
    circle = Circle((x2, y2), r2, animated=True, color='r', alpha=0.5)
    circles.append(circle)

    # Driver for spring
    if A == 0:
        h1 = 1
        w1 = 0.5
    else:
        h1 = 1 + np.tanh(np.abs(A)/5)
        w1 = 0.5 + np.tanh(np.abs(A)/5)
    x3 = 4
    y3 = -h1/2
    rectangles = []
    rectangle = Rectangle((x3,y3), w1, h1, animated=True, facecolor='black', alpha=0.5)
    rectangles.append(rectangle)

    # Arm connecting driver to flywheel
    w2 = 3.25
    h2 = 0.25
    rectangle = Rectangle((x3,-h2/2), -w2, h2, animated=True, facecolor='cyan', alpha=0.75)
    rectangles.append(rectangle)

    # Mass
    w3 = 1
    h3 = 1
    max_displacement = np.max(np.abs(xs))
    if max_displacement > 3:
        x4 = 10 + np.max(np.abs(xs))
    else:
        x4 = 10
    y4 = -h3/2
    rectangle = Rectangle((x4, y4), w3, h3, animated=True, facecolor='green', alpha=0.8)
    rectangles.append(rectangle)

    r2 = 0.25
    circle = Circle((x3, y2), r2, animated=True, color='r')
    circles.append(circle)

    ln, = ax1.plot([], [], 'k')

    if max_displacement > 3:
        line_min = x4-max_displacement
        line_max = x4+max_displacement+1
    else:    
        line_min = x4-3
        line_max = x4+4
    ax1.plot([line_min, line_max], -0.5*np.array([1, 1]), 'k')
    ax1.axvline(x4+0.5*w3, ls=':')

    patches = circles + rectangles 
        
    p = PatchCollection(patches, match_original=True)
    ax1.add_collection(p)
    ax1.set_ylim([-1.5, 1.5])
    ax1.set_xlim([-1.5, line_max])
    ax1.set_aspect(1)

    # Set up animation for second plot of displacement over time
    disp_line = ax2.plot([], [], 'b')[0]
    ax2.set_xlabel('Time')
    ax2.set_ylabel('X: Displacement')

    # Limits set for second plot
    ax2.set_xlim([ts.min(), ts.max()])
    ax2.set_ylim([xs.min(), xs.max()])
    ax2.plot([ts.min(),ts.max()],[0,0], 'r:'); # line to show zero displacement

    plt.tight_layout()
    plt.close()

    def animate(i):
        
        if A==0 or omega ==0:
            # flywheel not moving, so only move spring and mass
            x_mass_value = xs[i]+x4
            rectangles[2].set_x(x_mass_value)
            x_rect_value = x3
        else:
            
            # animate the flywheel
            circles[1].set_center((x2*np.cos(omega*ts[i]), 
                              x2*np.sin(omega*ts[i])))

            rectangles[1].set_angle(-np.arcsin(x2*np.sin(omega*ts[i])/w2)*\
                                  180/np.pi)

            x_rect_value = x2*np.cos(omega*ts[i])+\
                         np.sqrt(w2**2 - (x2*np.sin(omega*ts[i]))**2)

            rectangles[0].set_x(x_rect_value)
            rectangles[1].set_x(x_rect_value)

            circles[2].set_center((x2*np.cos(omega*ts[i])+\
                                np.sqrt(w2**2 - (x2*np.sin(omega*ts[i]))**2), 
                                0))

            x_mass_value = xs[i]+x4
            
            rectangles[2].set_x(x_mass_value)
          
        x_spring = np.linspace(x_rect_value+w1, x_mass_value, 500)
        y_spring = 0.4*signal.sawtooth(20*np.pi*\
                                       (x_spring-x_rect_value-w1)/\
                                       (x_mass_value-x_rect_value-w1)+\
                                       np.pi/2, 
                                       0.5)
        ln.set_data(x_spring, y_spring)
        
        p.set_paths(patches)
        
        # Animate displacement over time
        disp_line.set_data(ts[0:i],xs[0:i])
        
        return

    ani = FuncAnimation(fig, animate, frames=nframe, interval=250/fps, blit=False)

    display(HTML(ani.to_jshtml()))
    
#######################

def damped_harmonic_oscillator_comp(m=[0.2, 0.4], 
                                    b=[0.1, 0.1], 
                                    k=[1, 1], 
                                    A=[0, 0], 
                                    omega=[1, 1], 
                                    x0=[[-2, 0],[-2,0]],
                                    fps=3, tf=30):
        
    nframe = fps*tf # Setup number of frames for animation

    ts=np.linspace(0, tf, nframe)  # time to evaluate solution

    # Setup and solve 1d system with odeint
    xs = np.zeros((2,nframe))
    for i in range(2):
        us = odeint(diffeq, x0[i], ts, tfirst=True, args=(m[i], k[i], 
                                                          b[i], A[i], 
                                                          omega[i])) 
        xs[i,:] = us[:,0]

    fig, axs = plt.subplots(3, 1, figsize=(12,9))

    p = []
    circles = []
    rectangles = []
    patches = []
    lns = []
    w1s = []
    w3s = []
    for i in range(2):
        # Outer wheel for flywheel
        r1 = 1.25
        x1 = 0
        y1 = 0
        circles.append([])
        circle = Circle((x1, y1), r1, animated=True, color='b', alpha=0.25)
        circles[i].append(circle)

        # inner wheel for flywheel
        r2 = 0.25
        x2 = 0.75
        y2 = 0
        circle = Circle((x2, y2), r2, animated=True, color='r', alpha=0.5)
        circles[i].append(circle)

        # Driver for spring
        if A[i] == 0:
            h1 = 1
            w1 = 0.5
        else:
            h1 = 1 + np.tanh(np.abs(A[i])/5)
            w1 = 0.5 + np.tanh(np.abs(A[i])/5)
        w1s.append(w1)
        x3 = 4
        y3 = -h1/2
        rectangles.append([])
        rectangle = Rectangle((x3,y3), w1, h1, animated=True, facecolor='black', alpha=0.5)
        rectangles[i].append(rectangle)

        # Arm connecting driver to flywheel
        w2 = 3.25
        h2 = 0.25
        rectangle = Rectangle((x3,-h2/2), -w2, h2, animated=True, facecolor='cyan', alpha=0.75)
        rectangles[i].append(rectangle)

        # Mass
        w3 = 1 + np.tanh(m[i])
        w3s.append(w3)
        h3 = 1 + np.tanh(m[i])
        max_displacement = np.max(np.abs(xs))
        if max_displacement > 3:
            x4 = 10 + np.max(np.abs(xs))
        else:
            x4 = 10
        y4 = -h3/2
        rectangle = Rectangle((x4, y4), w3, h3, animated=True, facecolor='green', alpha=0.8)
        rectangles[i].append(rectangle)

        r2 = 0.25
        circle = Circle((x3, y2), r2, animated=True, color='r')
        circles[i].append(circle)

        ln, = axs[i].plot([], [], 'k')
        lns.append(ln)

        if max_displacement > 3:
            line_min = x4-max_displacement
            line_max = x4+max_displacement+1
        else:    
            line_min = x4-3
            line_max = x4+4
        axs[i].plot([line_min, line_max], -h3/2*np.array([1, 1]), 'k')
        axs[i].axvline(x4+0.5*w3, ls=':')

        patches.append([])
        patches[i] = circles[i] + rectangles[i]
            
        p.append(PatchCollection(patches[i], match_original=True))
        axs[i].add_collection(p[i])
        axs[i].set_ylim([-1.5, 1.5])
        axs[i].set_xlim([-1.5, line_max])
        axs[i].set_aspect(1)
        axs[i].set_title("Setup " + str(i+1), fontsize=14)

    # Set up animation for second plot of displacement over time
    disp_line_1 = axs[2].plot([], [], 'b', label='Setup 1')[0]
    disp_line_2 = axs[2].plot([], [], 'k', label='Setup 2')[0]
    axs[2].set_xlabel('Time')
    axs[2].set_ylabel('X: Displacement')
    axs[2].legend([disp_line_1, disp_line_2], 
          [disp_line_1.get_label(), disp_line_2.get_label()], 
          loc='upper right')

    # Limits set for second plot
    axs[2].set_xlim([ts.min(), ts.max()])
    axs[2].set_ylim([xs.min(), xs.max()])
    axs[2].plot([ts.min(),ts.max()],[0,0], 'r:'); # line to show zero displacement

    fig.tight_layout()
    plt.close()

    def animate(i):
        
        for j in range(2):

            if A[j]==0 or omega[j] ==0:
                # flywheel not moving, so only move spring and mass
                x_mass_value = xs[j,i]+x4
                rectangles[j][2].set_x(x_mass_value)
                x_rect_value = x3
            else:
                # animate the flywheel
                circles[j][1].set_center((x2*np.cos(omega[j]*ts[i]), 
                                  x2*np.sin(omega[j]*ts[i])))

                rectangles[j][1].set_angle(-np.arcsin(x2*np.sin(omega[j]*ts[i])/w2)*180/np.pi)

                x_rect_value = x2*np.cos(omega[j]*ts[i])+np.sqrt(w2**2 -
                                                            (x2*np.sin(omega[j]*ts[i]))**2)
                
                rectangles[j][0].set_x(x_rect_value)
                rectangles[j][1].set_x(x_rect_value)
                
                circles[j][2].set_center((x2*np.cos(omega[j]*ts[i])+\
                                    np.sqrt(w2**2 - (x2*np.sin(omega[j]*ts[i]))**2), 
                                    0))

                x_mass_value = xs[j,i]+x4
                
                rectangles[j][2].set_x(x_mass_value)
              
            x_spring = np.linspace(x_rect_value+w1s[j], x_mass_value, 500)
            y_spring = 0.4*signal.sawtooth(20*np.pi*\
                                      (x_spring-x_rect_value-w1s[j])/(x_mass_value-x_rect_value-w1s[j])+np.pi/2, 
                                      0.5)
            lns[j].set_data(x_spring, y_spring)
            
            p[j].set_paths(patches[j])
        
        # Animate displacement over time
        disp_line_1.set_data(ts[0:i], xs[0, 0:i])
        disp_line_2.set_data(ts[0:i], xs[1, 0:i])
        
        return

    ani = FuncAnimation(fig, animate, frames=nframe, interval=250/fps, blit=False)

    display(HTML(ani.to_jshtml()))

    return