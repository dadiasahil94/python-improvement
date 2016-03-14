from matplotlib import cm
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


def SCATTER_PLOT_3D(x,y,z,marker='o',color='b',xlabel="X-Axis",ylabel = "Y-Axis",zlabel="Z-Axis",title = 'SCATTER PLOT'):
    ''' 3d scatter plot of data points'''
    fig = plt.figure()
    ax = fig.add_subplot(111,projection='3d')
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_zlabel(zlabel)
    ax.set_title(title)
    ax.scatter(x,y,z,color=color,marker=marker)

def LINE_PLOT_3D(x,y,z,marker='o',color='b',xlabel="X-Axis",ylabel = "Y-Axis",zlabel="Z-Axis",title = 'LINE PLOT'):
    ''' 3d line plot of data points'''
    fig = plt.figure()
    ax = fig.add_subplot(111,projection='3d')
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_zlabel(zlabel)
    ax.set_title(title)
    ax.plot(x,y,z,color=color,marker=marker)

def WIREFRAME_PLOT_3D(x,y,z,rstride=1,cstride=1,xlabel="X-Axis",ylabel = "Y-Axis",zlabel="Z-Axis" , title = 'WIREFRAME PLOT'):
    ''' 3d wireframe plot of data'''
    fig = plt.figure()
    ax = fig.add_subplot(111,projection='3d')
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_zlabel(zlabel)
    ax.set_title(title)
    ax.plot_wireframe(x,y,z,rstride=rstride,cstride=cstride)

def SURFACE_PLOT_3D(x,y,z,rstride=1,cstride=1,xlabel="X-Axis",ylabel = "Y-Axis",zlabel="Z-Axis",title = 'SURFACE PLOT'):
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

def CONTOUR_PLOT_3D(x,y,z,cmap=cm.coolwarm,xlabel="X-Axis",ylabel = "Y-Axis",zlabel="Z-Axis",title='CONTOUR PLOT'):
    ''' 3d wireframe plot of data'''
    fig = plt.figure()
    ax = fig.add_subplot(111,projection='3d')
    cont = ax.plot_surface(x,y,z,cmap=cm.coolwarm)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_zlabel(zlabel)
    ax.set_title(title)


#
#
#
#
# x= np.linspace(0,20,12)
# y= np.linspace(0,20,12)
# z= np.linspace(-600,200,12)
# X = np.arange(-50, -25, 1)
# Y = np.arange(-50, -25, 1)
# R = np.sqrt(X**2 + Y**2)
# Z = np.sin(R)+np.cos(R)
# SCATTER_PLOT_3D(X,Y,0)
# WIREFRAME_PLOT_3D(X,Y,Z)
# SURFACE_PLOT_3D(X,Y,Z)
# CONTOUR_PLOT_3D(x,y,z)
# plt.show()
