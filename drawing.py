import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

class Drawing:
    def __init__(self, image):
        self.image = image
        self.fig, self.ax = plt.subplots(1,1, dpi=200)
        self.ax.imshow(image)
        self.xdim, self.ydim = image.shape
        self.line, = self.ax.plot([], [], 'r-')
        self.cid = self.fig.canvas.mpl_connect('motion_notify_event', self.stroke)
        self.xstrokes=[]
        self.ystrokes=[]
        self.state = 0
        plt.grid(b=True, which="minor", color='#666666')
        plt.show()

    def stroke(self, event):    
        if event.button==1:
            self.state=1
            x = np.append(self.line.get_xdata(), event.xdata)
            y = np.append(self.line.get_ydata(), event.ydata)
            self.line.set_data(x, y)
            self.fig.canvas.draw()
            for a,b in zip(self.xstrokes, self.ystrokes):
                plt.plot(a,b, "b-")

        elif self.state==1:
            xarr, yarr = self.line.get_xdata(), self.line.get_ydata()
            self.line.set_data([], [])
            self.state=0
            if len(self.xstrokes)>0:
                self.xstrokes.append(self.get_diff(self.xstrokes[-1], xarr))
                self.ystrokes.append(self.get_diff(self.ystrokes[-1], yarr))
            else:
                self.xstrokes.append(xarr)
                self.ystrokes.append(yarr)

    def get_strokes(self):
        return self.xstrokes, self.ystrokes
    
    def get_diff(self, arr1, arr2):
        dim = arr1.shape[0]
        arr2 = arr2[dim:]
        return arr2

    def get_dims(self):
        return self.xdim, self.ydim