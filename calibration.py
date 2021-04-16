import math
l1 = 12.6 #cm
l2 = 15.9

# all angles in degrees
a1_initial = 180-4.952511035901741
a2_initial = 180-14.16934273049585
a1_90_deflection = a1_initial-79.21113597953509
a2_90_deflection = a2_initial-84.79906637542962
a1_45_deflection = a1_initial-113.17041915855883
a2_45_deflection = a2_initial-125.0221538718897

a1_correction = (a1_initial)/180*1.05
a2_correction = (a2_initial)/180

def angles(p1, p2, p3, p4):
    """
    find the angles between two lines, given points p1, p2 
    belonging to line 1 and points p3, p4 belonging to line
    2
    """
    m1 = (p2[1]-p1[1])/((p2[0]-p1[0]))
    m2 = (p4[1]-p3[1])/((p4[0]-p3[0]))

    angle = abs(math.degrees(math.atan((m2-m1)/(1+m1*m2))))
    return min(abs(180-angle), angle)


def scale_angles(a1, a2):
    """
    A rough translation of real world angles to servo angles
    """
    a1 = 180-(a1_initial-a1)/a1_correction
    a2 = 180-(a2_initial-a2)/a2_correction
    
    return a1, a2