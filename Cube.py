# /*
# @Course: CS_121 #19990SP26C
# @author: Jacob Yeung #900494756
# @Date: 20260323
# @version Lab 5: Classes
# */

import math
from Square import Square

# Phase 3 — Class: Cube (built only from Squares)
# Using only Square objects as fields/properties, write a cube class.
# Reminder: your points are 2D, so you can't have a third dimension.
# We don't care about that though, we just want the square to give us information about it's volume and surface area.
class Cube:

    def __init__(self, identical_square_face: list[Square]):
        if len(identical_square_face) != 6:
            raise ValueError("A cube must have exactly 6 square faces.")
        # float compare
        if not math.isclose(min(s.area() for s in identical_square_face),max(s.area() for s in identical_square_face)):
            raise ValueError("All faces of a cube must be identical in size.")

        self._Squares = identical_square_face

    def volume(self)-> float:
        areas = list(map(lambda s: s.area(), self._Squares))
        return (sum(areas) / len(areas)) ** 1.5
        # side = math.sqrt(self._Square.area())
        # return self._Square.area() * side

    def surface_area(self)-> float:
        return sum(s.area() for s in self._Squares)

    def __repr__(self):
        """Developer-oriented representation."""
        return f"Cube: volume={self.volume():.2f}, surface_area={self.surface_area():.2f}"


import math
from Point import Point
from Square import Square

def test_cube_final():
    print("--- Running Phase 3: Cube Array Test ---")

    try:
        # 1. Create 4 points for a 3x3 square
        p1, p2, p3, p4 = Point(0, 0), Point(3, 0), Point(3, 3), Point(0, 3)

        # 2. Create an "array" (list) of 6 identical squares
        base_square = Square(p1, p2, p3, p4)
        faces_array = [base_square for _ in range(6)]

        # 3. Initialize Cube
        my_cube = Cube(faces_array)

        # 4. Extract results
        v = my_cube.volume()
        sa = my_cube.surface_area()

        print(f"Face Area: {base_square.area()}")
        print(f"Cube Volume: {v:.2f} (Expected: 27.00)")
        print(f"Cube Surface Area: {sa:.2f} (Expected: 54.00)")

        # 5. Validation
        if math.isclose(v, 27.0) and math.isclose(sa, 54.0):
            print("RESULT: PASS ✅")
        else:
            print("RESULT: FAIL ❌ (Math mismatch - check your Square.area logic!)")

    except ValueError as ve:
        print(f"Validation Error: {ve}")
    except Exception as e:
        print(f"Unexpected Error: {e}")


if __name__ == "__main__":
    test_cube_final()