# /*
# @Course: CS_121 #19990SP26C
# @author: Jacob Yeung #900494756
# @Date: 20260323
# @version Lab 5: Classes
# */

import math
from Point import Point
# design pattern composition

# Phase 2 — Class: Square (built only from Points)
# Using only Point objects as fields/properties, write a class representing a square.
class Square:
    def __init__(self, p1: Point, p2: Point, p3: Point, p4: Point):
        # Fields should be underscore + capitalized (constant-like).
        # Use Points for square definition (examples):
        # Option A: store 4 corner points (_P1, _P2, _P3, _P4)
        self._P1 = p1
        self._P2 = p2
        self._P3 = p3
        self._P4 = p4

        def __init__(self, p1: Point, p2: Point, p3: Point):
            self._P1 = p1
            self._P2 = p2
            self._P3 = p3
            self._P4 = None

    def perimeter(self)-> float:
        return self._P1.distance(self._P2) + self._P2.distance(self._P3) + self._P3.distance(self._P4)
# Methods:
# area()
# perimeter()
# Hint
#
# If your square stores 4 points in order, a side length can be computed using the distance between two adjacent points. Perimeter is 4 × side, and area is side² (for a true square).