from math import pi

def area_from_circum(circ):
    """2 pi r = c"""
    return pi * (circ / (2 * pi)) ** 2

print(area_from_circum(50.24))