# /*
# @Course: CS_121 #19990SP26C
# @author: Jacob Yeung #900494756
# @Date: 20260323
# @version Lab 5: Classes
# */

import math

# Phase 1 — Class: Point (2D)
# Write a class representing a 2D point with two fields (coordinates) and methods for distance and slope.
class Point:
    def __init__(self, x: int, y: int):
        # Fields: _X ans  _Y (underscore + capitalized)
        self._X = x
        self._Y = y

    def getX(self):
        return self._X

    def getY(self):
        return self._Y

    # Method: distance(other) → returns Euclidean distance to another point
    def distance(self, other: 'Point')-> float:
        return math.sqrt(self.__eigen_distance__(other))

    def __eigen_distance__(self, other: 'Point')-> int:
        return (self._X - other._X)**2 + (self._Y - other._Y)**2

    # Method: slope(other) → returns slope between points
    def slope(self, other: 'Point')-> float:
        return math.inf if (other._X == self._X) else (other._Y - self._Y) / (other._X - self._X)
    # Slope is (y2 - y1) / (x2 - x1). Consider what happens when x2 == x1 (vertical line).
    # You may choose to raise an exception for vertical slope or return math.inf—just be consistent and test it.

    def __str__(self): # toString()
        """Human-readable representation."""
        return f"({self._X}, {self._Y})"

    def __repr__(self):
        """Developer-oriented representation."""
        return f"Point: x={self._X}, y={self._Y}"

    def __eq__(self, other):
        return isinstance(other, Point) and self._X == other._X and self._Y == other._Y

# For test
# if __name__ == "__main__":
#     p1 = Point(0, 0)
#     p2 = Point(3, 4)
#     p3 = Point(3, 10)
#
#     print(f"Distance: {p1.distance(p2)}")  # Should be 5.0
#     print(f"Slope (Normal): {p1.slope(p2)}") # Should be 1.333...
#     print(f"Slope (Vertical): {p2.slope(p3)}") # Should be inf