from numpy import *
                      
# Define the domain of your plot here
tht = linspace(0, 2*pi, 50) 
phi = linspace(0, 2*pi, 50)

# Define the function of your plot here
def r(u, v):
    x = (3+cos(u))*cos(v)
    y = (3+cos(u))*sin(v)
    z = 4*sin(u)
    return x, y, z

