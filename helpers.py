# Some Helper Functions
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# Plot a unit sphere. 
def plot_sphere():
    fig = plt.figure()
    fig.set_size_inches(8, 8)
    ax = fig.add_subplot(projection='3d')
    ax.axis('off')
    
    # Make data
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)
    x = np.outer(np.cos(u), np.sin(v))
    y = np.outer(np.sin(u), np.sin(v))
    z = np.outer(np.ones(np.size(u)), np.cos(v))
    
    # Plot the surface
    ax.plot_surface(x, y, z)
    
    # Set an equal aspect ratio
    ax.set_aspect('equal')
    
    plt.show()