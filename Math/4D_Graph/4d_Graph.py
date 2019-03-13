import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib as mpl
import numpy as np
from matplotlib import style

style.use('fivethirtyeight')

# create some fake data
x = y = np.arange(-4.0, 4.0, 0.02)
# here are the x,y and respective z values
X, Y = np.meshgrid(x, y)
Z = np.sinc(np.sqrt(X*X+Y*Y))
# this is the value to use for the color
V = np.sin(Y)

fig = plt.figure(figsize = (12,8))
ax = plt.subplot2grid((1,8),(0,7))
cmap = mpl.cm.Oranges
norm = mpl.colors.Normalize(vmin=V.min(), vmax=V.max())

cb1 = mpl.colorbar.ColorbarBase(ax, cmap=cmap,
                                norm=norm,
                                orientation='vertical')
cb1.set_label('Some Units')
ax2 = plt.subplot2grid((1,8),(0,0),colspan = 7,projection = '3d')
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm


# here we create the surface plot, but pass V through a colormap
# to create a different color for each patch
ax2.plot_surface(X, Y, Z, facecolors=cm.Oranges(V))
plt.show()