from matplotlib import cm
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


def SCATTER_PLOT_3D(x,y,z,marker='o',color='b',xlabel="X-Axis",ylabel = "Y-Axis",zlabel="Z-Axis",title = '3D SCATTER PLOT'):
    ''' 3d scatter plot of data points'''
    fig = plt.figure()
    ax = fig.add_subplot(111,projection='3d')
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_zlabel(zlabel)
    ax.set_title(title)
    ax.scatter(x,y,z,color=color,marker=marker)

def LINE_PLOT_3D(x,y,z,marker='o',color='b',xlabel="X-Axis",ylabel = "Y-Axis",zlabel="Z-Axis",title = '3D LINE PLOT'):
    ''' 3d line plot of data points'''
    fig = plt.figure()
    ax = fig.add_subplot(111,projection='3d')
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_zlabel(zlabel)
    ax.set_title(title)
    ax.plot(x,y,z,color=color,marker=marker)

def WIREFRAME_PLOT_3D(x,y,z,rstride=1,cstride=1,xlabel="X-Axis",ylabel = "Y-Axis",zlabel="Z-Axis" , title = '3D WIREFRAME PLOT'):
    ''' 3d wireframe plot of data'''
    fig = plt.figure()
    ax = fig.add_subplot(111,projection='3d')
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_zlabel(zlabel)
    ax.set_title(title)
    ax.plot_wireframe(x,y,z,rstride=rstride,cstride=cstride)

def SURFACE_PLOT_3D(x,y,z,rstride=1,cstride=1,xlabel="X-Axis",ylabel = "Y-Axis",zlabel="Z-Axis",title = '3D SURFACE PLOT'):
    ''' 3d surface plot of data'''
    fig = plt.figure()
    ax = fig.add_subplot(111,projection='3d')
    x,y = np.meshgrid(x,y)
    surf = ax.plot_surface(x,y,z,rstride=rstride,cstride=cstride,cmap=cm.jet)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_zlabel(zlabel)
    ax.set_title(title)
    fig.colorbar(surf, shrink=0.5, aspect=5)

def CONTOUR_PLOT_3D(x,y,z,cmap=cm.coolwarm,xlabel="X-Axis",ylabel = "Y-Axis",zlabel="Z-Axis",title='3D CONTOUR PLOT'):
    ''' 3d wireframe plot of data'''
    fig = plt.figure()
    ax = fig.add_subplot(111,projection='3d')
    cont = ax.plot_surface(x,y,z,cmap=cm.coolwarm)
    ax.set_ylabel(ylabel)
    ax.set_zlabel(zlabel)
    ax.set_xlabel(xlabel)
    ax.set_title(title)

def SCATTER_PLOT_2D(x,y,figure_no=1,xlabel="X-Axis",ylabel = "Y-Axis",title = '2D SCATTER PLOT'):
    ''' 2d scatter plot of data'''
    plt.figure(figure_no)
    plt.subplot(111)
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    plt.title(title)

def LINE_PLOT_2D(y,x=None,figure_no=1,color='b',xlabel="X-Axis",ylabel = "Y-Axis",title = '2D LINE PLOT'):
    ''' 2d line plot of data--y values not necessary'''
    plt.figure(figure_no)
    plt.subplot(111)
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    plt.title(title)
    if x!=None:
        plt.plot(x,y,str(color))
    else:
        plt.plot(y)

def HISTOGRAM_PLOT_1D(x,bins=20,figure_no=1,normed=False,color='b',xlabel="Data points",ylabel = "Counts",title = "1D HISTOGRAM"):
    ''' Plots 1d histogram'''
    plt.figure(figure_no)
    plt.subplot(111)
    plt.hist(x,bins=bins,normed=normed,color=color)
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    plt.grid(True)
    if normed:
        plt.title('NORMALISED '+title)
        plt.ylabel('Percentage of occurance')
    else:
        plt.title(title)



def HISTOGRAM_PLOT_2D(x,y,bins=20,figure_no=1,normed=False,xlabel="X-Data point",ylabel = "Y-Data point",title = "2D HISTOGRAM"):
    ''' plots 2d histogram'''
    plt.figure(figure_no)
    plt.subplot(111)
    H, xedges, yedges = np.histogram2d(x,y,bins=bins,normed=normed)
    H = np.rot90(H) # H needs to be rotated and flipped
    H = np.flipud(H)
    # Mask zeros
    Hmasked = np.ma.masked_where(H==0,H) # Mask pixels with a value of zero
    plt.pcolormesh(xedges,yedges,Hmasked)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    cbar = plt.colorbar()
    if normed:
        plt.title('NORMALISED '+title)
        cbar.ax.set_ylabel('Percentage')
    else:
        plt.title(title)
        cbar.ax.set_ylabel('Counts')



x= np.linspace(0,20000,12)
y= np.linspace(-200,20,12)
data = np.random.uniform(low=-3, high=3, size=1000)

# z= np.linspace(-600,200,12)
# X = np.arange(-50, -25, 1)
# Y = np.arange(-50, -25, 1)
# R = np.sqrt(X**2 + Y**2)
# Z = np.sin(R)+np.cos(R)
# SCATTER_PLOT_3D(X,Y,0)
# WIREFRAME_PLOT_3D(X,Y,Z)
# SURFACE_PLOT_3D(X,Y,Z)
# CONTOUR_PLOT_3D(x,y,z)
# LINE_PLOT_2D(x,color='g')
# LINE_PLOT_2D(y=y,x=x)
n = 100000
x = np.random.randn(n)
y = (1.5 * x) + np.random.randn(n)
# HISTOGRAM_PLOT_2D(x,y,normed=False,bins=200)
HISTOGRAM_PLOT_1D(x,normed=True,bins=200)
plt.show()
