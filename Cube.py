# /*
# @Course: CS_121 #19990SP26C
# @author: Jacob Yeung #900494756
# @Date: 20260323
# @version Lab 5: Classes
# */

import math

from Point import Point
from Square import Square

# Phase 3 — Class: Cube (built only from Squares)
# Using only Square objects as fields/properties, write a cube class.
# Reminder: your points are 2D, so you can't have a third dimension.
# We don't care about that though, we just want the square to give us information about it's volume and surface area.
class Cube:

    def __init__(self, identical_square_face: Square):
        self._face = identical_square_face

    def volume(self)-> float:
        side = math.sqrt(self._face.area())
        return self._face.area() * side

    def surface_area(self)-> float:
        return self._face.area() * 6

    def __repr__(self):
        """Developer-oriented representation."""
        return f"Cube: volume={self.volume():.2f}, surface_area={self.surface_area():.2f}"


def test_cube():
    print("--- Running Cube Test Case ---")

    # 1. Create the base face (Square with side length 3)
    # Points: (0,0), (3,0), (3,3), (0,3)
    p1, p2, p3, p4 = Point(0, 0), Point(3, 0), Point(3, 3), Point(0, 3)

    try:
        base_square = Square(p1, p2, p3, p4)
        my_cube = Cube(base_square)

        print(f"Base Square Area: {base_square.area()}")  # Should be 9

        # 2. Logic Checks
        v = my_cube.volume()
        sa = my_cube.surface_area()

        print(f"Cube Volume: {v} (Expected: 27.0)")
        print(f"Cube Surface Area: {sa} (Expected: 54.0)")

        # 3. Validation
        if math.isclose(v, 27.0) and math.isclose(sa, 54.0):
            print("RESULT: PASS ✅")
        else:
            print("RESULT: FAIL ❌ (Math error)")

    except Exception as e:
        print(f"RESULT: FAIL ❌ (Error during initialization: {e})")


if __name__ == "__main__":
    test_cube()


