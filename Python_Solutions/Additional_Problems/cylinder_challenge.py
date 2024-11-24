"""
Water Tank Filling Challenge

You have a cylindrical water tank that is partially filled with water.
Given the radius and height of the tank, and the current height of the water inside,
write a function that calculates the volume of water in the tank.

Problem:
Given the radius "r" of the cylinder and the height "h" of the water (both in meters),
write a Python function to calculate the volume of water in cubic meters.

CONSTRAINT:
    If the value of either radius or water_height is negative or invalid a CUSTOM Exception
    should be raised!!


Examples Input:
radius = 3
water_height = 4

Expected Output:
113.09733552923255

"""

import math

class NegativeValue(ValueError):
    pass

def water_volume (radius, water_height):
    if radius < 0 or water_height < 0:
        raise NegativeValue
    else:
        return (math.pi*(radius**2))*water_height


# print(water_volume(3,4))
# print(water_volume(1,-3))