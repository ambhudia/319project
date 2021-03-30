import numpy as np
import matplotlib.pyplot as plt
from celluloid import Camera
import plotter

class VirtualPlotter(plotter.Plotter):
    def animate(self, a1s, a2s, name):
        self.fig, self.ax = plt.subplots(1,1)
        camera = Camera(self.fig)
        lines = []

        for a1, a2 in zip(a1s, a2s):
            x1, y1 = l1*np.cos(a1), l1*np.sin(a1)
            x2, y2 = x1+l2*np.cos(a1+a2), y1+l2*np.sin(a1+a2)
            linex = []
            liney = []
            for x, y in self.get_double_joint_lines(x1, y1, x2, y2):
                self.ax.plot(x, y, "r-") # robot arms
                for a, b in lines:
                    self.ax.plot(a, b, "k-")
                linex.append(x[-1])
                liney.append(y[-1])
                self.ax.plot(linex, liney, "b-")
                camera.snap()
            lines.append((linex, liney))
            
        animation = camera.animate()
        animation.save(f'{name}.gif', writer = 'imagemagick')

    def get_double_joint_lines(self, x1, y1, x2, y2):
        for a,b,c,d in zip(x1, y1, x2, y2):
            yield np.array([0, a, c]), np.array([0, b, d])