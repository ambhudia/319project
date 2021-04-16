import numpy as np

class Plotter:
    """
    I wrote this class then interpolation was required to account for
    differences in angular speed, and to smooth out splines.
    
    It turned out that my sampling rate was high enough that this 
    was not needed
    """
    def __init__(self, l1, l2):
        # it is assumed that both servos move with omega=1
        # thus the returned values are the corrections that 
        # need to be made to the rotational speeds
        self.l1 = l1
        self.l2 = l2
        self.w1 = 1
        self.w2 = 1

    def step(self, a1, a2):
        return a1+self.w1, a2+self.w2

    def interpolate_strokes(self, a1, a2, deg2rad=False):
        a1_strokes = []
        a2_strokes = []

        for a1_stroke, a2_stroke in zip(a1, a2):
            current_a1 = a1_stroke[0]
            current_a2 = a2_stroke[0]

            a1s = []
            a2s = []

            self.w1 = 1
            self.w2 = 1
            
            # interpolate between the points with angular motion
            for c1, c2 in zip(a1_stroke[1:], a2_stroke[1:]):
                n_steps_1 = abs(int((c1-current_a1)/self.w1))
                n_steps_2 = abs(int((c2-current_a2)/self.w2))
                n_steps = min(n_steps_1, n_steps_2)
                w1_eff = (c1-current_a1)/n_steps
                w2_eff = (c2-current_a2)/n_steps
                for _ in range(n_steps):
                    current_a1 += w1_eff
                    current_a2 += w2_eff
                    a1s.append(current_a1)
                    a2s.append(current_a2)
                a1s.append(c1)
                a2s.append(c2)
            
            if deg2rad:
                a1s = np.deg2rad(np.asarray(a1s))
                a2s = np.deg2rad(np.asarray(a2s))

            a1_strokes.append(a1s)
            a2_strokes.append(a2s)
        
        return a1_strokes, a2_strokes

