from turtle import (
    penup, pendown, setpos, seth,
    fd, rt, lt,
    circle, color, begin_fill, end_fill,
)

def p(x, y):
    penup(); setpos(x, y)
    pendown(); seth(0)

def rect(x1, y1, x2, y2):
    penup(); setpos(x1, y1)
    pendown(); seth(0)
    d = abs(x2 - x1)
    h = abs(y2 - y1)
    fd(d); rt(90)
    fd(h); rt(90)
    fd(d); rt(90)
    fd(h)

def fill_circle(x, y, r, c):
    penup(); setpos(x, y - r)
    pendown(); seth(0)
    color("black", c)
    begin_fill()
    circle(r)
    end_fill()

def kv(x1, y1, x2, y2, c=None):
    penup(); setpos(x1, y1)
    pendown(); seth(0)
    d = abs(x2 - x1)
    if c is None:
        color("black")
    else:
        color("black", c)
    begin_fill()
    for _ in range(4):
        fd(d); rt(90)
    end_fill()

def star(n, x, y, d):
    penup(); setpos(x, y)
    pendown(); seth(0)
    u = 180 - 180 / n
    for _ in range(n):
        fd(d); rt(u)

def pr_tr(x, y, a, b, c):
    penup(); setpos(x - a, y)
    pendown(); seth(0)
    color(c, c)
    begin_fill()
    fd(a); rt(90); fd(b)
    end_fill()

def poly_star(n, x, y, d):
    penup(); setpos(x, y)
    pendown(); seth(0)
    color("red", "yellow")
    begin_fill()
    u1 = 180 - 360 / n
    u2 = 180 - 720 / n
    for _ in range(n):
        fd(d); rt(u1)
        fd(d); lt(u2)
    end_fill()

def row(y):
    x = -100; r = 10
    while x < 100:
        fill_circle(x, y, r, "yellow")
        x += 20

def georgin(n, x, y, r, c1="black", c2=None):
    penup(); setpos(x, y)
    pendown(); seth(0)
    if c2 is None:
        color(c1)
    else:
        color(c1, c2)
    begin_fill()
    for _ in range(n):
        circle(r)
        lt(360 // n)
    end_fill()

def romashka(n, x, y, r, c1="black", c2=None):
    penup(); setpos(x, y)
    pendown(); seth(0)
    if c2 is None:
        color(c1)
    else:
        color(c1, c2)
    begin_fill()
    for _ in range(n):
        circle(r, 90); lt(90)
        circle(r, 90); rt(-90)
        lt(360 // n)
    end_fill()

def rozan(n, x, y, r, c1="black", c2=None):
    penup(); setpos(x, y)
    pendown(); seth(0)
    if c2 is None:
        color(c1)
    else:
        color(c1, c2)
    begin_fill()
    for _ in range(n):
        circle(r, 360, 4)
        lt(360 // n)
    end_fill()