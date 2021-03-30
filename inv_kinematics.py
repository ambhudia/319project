import numpy as np
import math

class Kinematics:
    def __init__(self, l1, l2):
        self.l1 = l1 # length of primary arm
        self.l2 = l2 # length of secondary arm
        self.len2 = l1**2+l2**2
        self.l1l2 = l1*l2

    def _invert_array(self, x ,y):
        a2 = np.arccos((x**2 + y**2 - self.len2)/(2*self.l1l2))
        a1 = np.arctan(y/x)-np.arctan(self.l2*np.sin(a2)/(self.l1 +self.l2*np.cos(a2))) 
        return a1, a2

    def invert(self, x, y):
        if (type(x)==np.ndarray) and (type(y)==np.ndarray):
            return self._invert_array(x ,y)
        elif ((type(x)==list) and (type(y)==list)) or ((type(x)==tuple) and (type(y)==tuple)):
            return self._invert_array(np.asarray(x), np.asarray(y))
        else:
            a2 = math.acos((x**2 + y**2 - self.len2)/(2*self.l1l2))
            a1 = math.atan(y/x)-math.atan(self.l2*math.sin(a2)/(self.l1 +self.l2*math.cos(a2))) 
            return a1, a2