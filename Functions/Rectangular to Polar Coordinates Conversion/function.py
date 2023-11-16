import math

#Start Function 
def rectangular_to_polar(x, y):
    #maskig
    x = float(x)
    y = float(y)

    r = math.sqrt(x**2 + y**2)

    # avoid x=0 in thet=y/x
    if x == 0:
        if y > 0:
            theta = math.pi / 2
        elif y < 0:
            theta = -math.pi / 2
        else:
            theta = 0
    else:
        theta = math.atan(y/x)

    return r, theta
# End function
