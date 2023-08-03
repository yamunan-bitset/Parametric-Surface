import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d as Axes3D

class Parametric3D:
    def __init__(self, funtion, in_dim, out_dim, tht, phi, title=''): # function: R^in_dim -> R^out_dim
        self.title = title
        try:
            assert(0 < out_dim <= 3)
        except AssertionError:
            print("Warning: Plotting only available in 1, 2 or 3 dimensions")

        self.n = in_dim
        self.m = out_dim
        self.tht, self.phi = np.meshgrid(tht, phi)
        self.f = funtion(self.tht, self.phi)
        # self.f: R^self.n -> R^self.m
        

    def plot(self):
        try:
            assert(0 < self.m <= 3)
        except AssertionError:
            print("Error: Plotting only available in 1, 2 or 3 dimensions")
            exit(0)

        x, y, z = self.f
        fig = plt.figure('Parametric Surfaces: ' + self.title)
        ax = fig.add_subplot(111, projection=str(self.m)+'d')
        h = ax.plot_surface(x, y, z, cmap='jet', edgecolor='k')
        fig.colorbar(h)

        ax.set_xlabel('X', fontweight="bold")
        if self.m >= 2:
            ax.set_ylabel('Y', fontweight="bold")
        if self.m == 3:
            ax.set_zlabel('Z', fontweight="bold")
        ax.set_title('Parametric Surfaces: ' + self.title, fontweight="bold")

        ax.axis('square')
        plt.show()

if __name__ == '__main__':
    tht = np.linspace(0, 2*np.pi, 50)
    phi = np.linspace(0, 2*np.pi, 50)

    def cone(u, v):
        x = u*np.cos(v)
        y = u*np.sin(v)
        z = u
        return x, y, z

    def r(u, v):
        x = u*v*np.cos(v)*np.sin(u)
        return x

    p = Parametric3D(cone, 2, 3, tht, phi)
    p.plot()