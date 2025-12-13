# 0x08. Python - More Classes and Objects

This directory contains several implementations of a `Rectangle` class.  
Each task adds new behavior such as validation, area/perimeter methods, string representation, instance counting, and utility methods.

---

## Files Description

- **0-rectangle.py**  
  Basic empty `Rectangle` class.

- **1-rectangle.py**  
  Rectangle with private `width` and `height` attributes and validation:
  - `width` and `height` must be integers ≥ 0.

- **2-rectangle.py**  
  Rectangle with:
  - Validated `width` and `height`
  - `area()` method
  - `perimeter()` method (returns `0` if either side is `0`).

- **3-rectangle.py**  
  Same as above, plus:
  - `__str__` to return a string representation of the rectangle using `#`.

- **4-rectangle.py**  
  Same behavior as `3-rectangle.py`, plus:
  - `__repr__` returning a string like: `Rectangle(width, height)`  
    (usable with `eval()` to recreate the object).

- **5-rectangle.py**  
  Same behavior as `4-rectangle.py`, plus:
  - `__del__` prints `"Bye rectangle..."` when an instance is deleted.

- **6-rectangle.py**  
  Rectangle with:
  - Class attribute `number_of_instances` (counts how many `Rectangle` objects exist).
  - Size validation, `area()`, `perimeter()`, `__str__`, `__repr__`, `__del__`.

- **7-rectangle.py**  
  Same as `6-rectangle.py`, plus:
  - Class attribute `print_symbol` used to draw the rectangle (can be any type that converts to string).

- **8-rectangle.py**  
  Same as `7-rectangle.py`, plus:
  - Static method `bigger_or_equal(rect_1, rect_2)`  
    Returns the rectangle with the bigger (or equal) area.

- **9-rectangle.py**  
  Same as `8-rectangle.py`, plus:
  - Class method `square(size=0)`  
    Returns a new `Rectangle` instance where `width == height == size`.

---

## Common Features

Across these implementations, the `Rectangle` class provides:

- Input validation for `width` and `height`:
  - Must be integers
  - Must be ≥ 0
- Area and perimeter calculation
- String representation using `print_symbol`
- A reproducible `__repr__`
- Optional instance counting and comparison helpers

---

## Usage Example

```python
from rectangle import Rectangle

r1 = Rectangle(3, 4)
print(r1.area())        # 12
print(r1.perimeter())   # 14
print(r1)               # Printed as a grid of print_symbol

r2 = Rectangle.square(5)  # Only in 9-rectangle.py
print(r2.area())          # 25
