import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from time import sleep
class Drawing:
    """
    This is how one programs the robot
    Draw some nice strokes using the Matplotlib GUI
    and have your robot do the same
    """
    def __init__(self, image):
        """
        image: a 2D numpy array (a color channel if you will)
               that acts as the background on which you will draw.
               This also gives the dimensions for scaling your drawing.
        """
        self.image = image
        self.fig, self.ax = plt.subplots(1,1, dpi=100)
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
        """
        The canvas connects to this when there is a key event. 
        if the key is x, record the stroke data.
        
        If the key is released, end the stroke, save it, and
        set the stage for a new stroke
        """
        if event.key == 'x':
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
            self.xstrokes.append(xarr)
            self.ystrokes.append(yarr)

    def get_strokes(self):
        return self.xstrokes, self.ystrokes

    def get_dims(self):
        return self.xdim, self.ydim
