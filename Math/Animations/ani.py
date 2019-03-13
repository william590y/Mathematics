import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
fig = plt.figure()
p = np.pi/2
ax = fig.add_subplot(111, projection='3d')
a = np.linspace(1,10,100)
X,Y=  np.meshgrid(a,a)
b=200
def f(n):
    Z = np.sin(X)*np.sin(Y)*np.sin(np.pi/2+n*(np.pi*2/b))
    ax.clear()
    ax.set_zlim(-1,1) 
    ax.plot_surface(X, Y, Z,facecolors=cm.cool(Z))   
from matplotlib.animation import FuncAnimation
l = FuncAnimation(fig,f,interval = 1)
l.save('ani.gif')
plt.show()