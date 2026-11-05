# function-for-turtle

[![PyPI version](https://img.shields.io/pypi/v/function-for-turtle.svg)](https://pypi.org/project/function-for-turtle/)
[![Python versions](https://img.shields.io/pypi/pyversions/function-for-turtle.svg)](https://pypi.org/project/function-for-turtle/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PyPI downloads](https://img.shields.io/pypi/dm/function-for-turtle.svg)](https://pypi.org/project/function-for-turtle/)

A small helper library for Python's `turtle` module. Draws basic shapes
and flowers with a single call — no need to hand-write `forward`/`right`
loops every time.

A small helper library for Python's `turtle` module. Draws basic shapes
and flowers with a single call — no need to hand-write `forward`/`right`
loops every time.

## Installation

```bash
pip install function-for-turtle
```

For local development:

```bash
git clone https://github.com/ilyashulga13/function-for-turtle.git
cd function-for-turtle
pip install -e .
```

## Quick start

```python
import turtle
from function_for_turtle import rect, kv, star, georgin

rect(0, 0, 100, 50)                       # rectangle 100×50
kv(0, 0, 50, 50)                          # square with side 50
star(5, 100, 100, 60)                     # five-pointed star
georgin(8, 0, 0, 20, "black", "yellow")   # dahlia flower

turtle.done()
```

A `turtle` window opens, draws everything, and waits to be closed.

## Functions

### Basic shapes

| Function | Description |
|---|---|
| `p(x, y)` | Move the turtle to `(x, y)` without drawing, set heading to east (0°). |
| `rect(x1, y1, x2, y2)` | Draw a rectangle from two opposite corners. |
| `kv(x1, y1, x2, y2, c=None)` | Draw a square with side `abs(x2 - x1)`. If `c` is given, fill with that color. |
| `pr_tr(x, y, a, b, c)` | Draw a right triangle with legs `a` and `b`, filled with color `c`. |

### Circles and stars

| Function | Description |
|---|---|
| `fill_circle(x, y, r, c)` | Draw a filled circle of radius `r` centered at `(x, y)`. |
| `star(n, x, y, d)` | Draw a "classic" star with `n` rays of length `d`. |
| `poly_star(n, x, y, d)` | Draw a "fluffy" star (each ray is two segments). Fill: red outline, yellow fill. |
| `row(y)` | Draw a row of yellow circles along the horizontal line `y`. |

### Flowers

| Function | Description |
|---|---|
| `georgin(n, x, y, r, c1="black", c2=None)` | Dahlia made of `n` circular petals of radius `r`. |
| `romashka(n, x, y, r, c1="black", c2=None)` | Chamomile made of `n` petals. |
| `rozan(n, x, y, r, c1="black", c2=None)` | Rose made of `n` square petals. |

For all flowers, `c1` is the outline color and `c2` is the fill color.
If `c2` is omitted, only the outline is drawn (no fill).

## Example: a drawing with several shapes

```python
import turtle
from function_for_turtle import p, rect, kv, star, georgin, romashka, rozan

# frame
rect(-200, -150, 200, 150)

# shapes inside
kv(-150, -100, -100, -50, "lightblue")
star(5, 0, 50, 40)
georgin(8, 100, 100, 15, "green", "yellow")
romashka(6, -100, 80, 12, "black", "white")
rozan(4, 100, -80, 20, "darkred", "pink")

turtle.done()
```

## Compatibility

- Python 3.8+
- `turtle` is part of the standard library — no separate installation needed.
- Works on Windows, macOS, and Linux (requires Tkinter, which ships with the official Python installer).

## License

MIT — see [LICENSE](LICENSE).

## Author

[2bytes](https://github.com/ilyashulga13)
