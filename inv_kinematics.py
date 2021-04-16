import numpy as np

class InvKinematics:
    def __init__(self, l1, l2):
        self.l1 = l1 # length of primary arm
        self.l2 = l2 # length of secondary arm
        self.arm_lengths_sqr = l1**2+l2**2
        self.l1l2 = l1*l2

    def invert(self, x, y):
        """
        x: Array-like or float
        y: Array-like or float

        The assumption is that y is never zero
        """
        arm_lengths_sqr = self.arm_lengths_sqr
        l1l2 = self.l1l2
        l3_sqr = x**2+y**2
        a2 = np.pi - np.arccos(((arm_lengths_sqr)-(l3_sqr))/(2*l1l2))
        a1 = +np.arctan(-x/y) + np.arcsin(self.l2/np.sqrt(l3_sqr)*np.sin(np.pi-a2))
        return np.rad2deg(a1), np.rad2deg(a2)