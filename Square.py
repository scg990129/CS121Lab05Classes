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
        self._Points = [self._P1, self._P2, self._P3, self._P4]

        if not self._is_square():
            raise Exception('Square is not square')

        # Option B: store two points that define a side (then infer the rest) — only if you can justify it clearly
        # python do not support overloading in constructor
        # def __init__(self, corner1: Point, opposite_corner: Point):
        #     self._P1 = corner1
        #     self._P4 = opposite_corner
        #     cx = (p1.getX() + p4.getX()) // 2
        #     cy = (p1.getY() + p4.getY()) // 2
        #     dx = (p1.getX() - p4.getX()) // 2
        #     dy = (p1.getY() - p4.getY()) // 2
        #     self._P2 = Point(cx - dy, cy + dx)
        #     self._P3 = Point(cx + dy, cy - dx)
        #     if not self._is_square():
        #         raise Exception('Square is not square')

    def _is_square(self) -> bool:
        distances = []
        for i in range(4):
            for j in range(i + 1, 4):
                # int compare better than float compare
                eigen_distance = (self._Points[i].getX() - self._Points[j].getX()) ** 2 + (self._Points[i].getY() - self._Points[j].getY()) ** 2
                distances.append(eigen_distance)
        distances.sort()
        return (len(set(distances)) == 2 and
                distances[0] > 0 and
                2 * distances[0] == distances[4])

    # perimeter()
    def perimeter(self)-> float:
        distances = []
        for i in range(4):
            for j in range(i + 1, 4):
                # int compare better than float compare
                eigen_distance = (self._Points[i].getX() - self._Points[j].getX()) ** 2 + (self._Points[i].getY() - self._Points[j].getY()) ** 2
                distances.append(eigen_distance)
        distances.sort()
        return math.sqrt(min(distances) )* 4

    # area()
    def area(self)-> float:
        distances = []
        for i in range(4):
            for j in range(i + 1, 4):
                # int compare better than float compare
                eigen_distance = (self._Points[i].getX() - self._Points[j].getX()) ** 2 + (self._Points[i].getY() - self._Points[j].getY()) ** 2
                distances.append(eigen_distance)
        distances.sort()
        return math.sqrt(min(distances)) ** 2

    def __repr__(self):
        """Developer-oriented representation."""
        return f"Square: {self._Points}"

def run_tests():
    print("=== Square Class Test Suite ===")

    # Test 1: Standard Axis-Aligned Square
    # Points: (0,0), (2,0), (2,2), (0,2) -> Side = 2
    try:
        p1, p2, p3, p4 = Point(0,0), Point(2,0), Point(2,2), Point(0,2)
        sq1 = Square(p1, p2, p3, p4)
        print(f"Test 1 (Normal): PASS (Area: {sq1.area()}, Perimeter: {sq1.perimeter()})")
    except Exception as e:
        print(f"Test 1 (Normal): FAIL - {e}")

    # Test 2: Invalid Square (A Rectangle)
    # Points: (0,0), (4,0), (4,2), (0,2) -> Should raise Exception
    try:
        p1, p2, p3, p4 = Point(0,0), Point(4,0), Point(4,2), Point(0,2)
        sq2 = Square(p1, p2, p3, p4)
        print("Test 2 (Rectangle): FAIL (Should have raised Exception)")
    except Exception:
        print("Test 2 (Rectangle): PASS (Correctly rejected invalid square)")

    # Test 3: Tilted Square (Rotated)
    # Points: (1,0), (2,1), (1,2), (0,1) -> Side = sqrt(2) ≈ 1.414
    # Area should be 2, Perimeter should be 4 * sqrt(2) ≈ 5.65
    try:
        p1, p2, p3, p4 = Point(1,0), Point(2,1), Point(1,2), Point(0,1)
        sq3 = Square(p1, p2, p3, p4)
        print(f"Test 3 (Tilted): PASS (Area: {sq3.area():.1f}, Perimeter: {sq3.perimeter():.2f})")
    except Exception as e:
        print(f"Test 3 (Tilted): FAIL - {e}")

if __name__ == "__main__":
    run_tests()