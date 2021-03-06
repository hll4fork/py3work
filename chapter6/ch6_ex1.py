#!/usr/bin/env python3
# Author    : huanglilongwk@qq.com
# Time      : 2016/4/14
# Ref       : <Programming in Python3 > chapter6 Shape_ans.py example code

"""
This module provides the Point and Circle classes.

>>> point = Point()
>>> point
Point(0, 0)
>>> point.x = 12
>>> str(point)
'(12, 0)'
>>> a = Point(3, 4)
>>> b = Point(3, 4)
>>> a == b
True
>>> a == point
False
>>> a != point
True

>>> circle = Circle(2)
>>> circle
Circle(2, 0, 0)
>>> circle.radius = 3
>>> circle.x = 12
>>> circle
Circle(3, 12, 0)
>>> a = Circle(4, 5, 6)
>>> b = Circle(4, 5, 6)
>>> a == b
True
>>> a == circle
False
>>> a != circle
True
"""

import math


class Point:

    def __init__(self, x=0, y=0):
        """A 2D cartesian coordinate

        >>> point = Point()
        >>> point
        Point(0, 0)
        """
        self.x = x
        self.y = y

    def distance_from_origin(self):
        """Return the distance from center to origin

         >>> point = Point(3, 4)
         >>> point.distance_from_origin()
         5.0
        """
        return math.hypot(self.x, self.y)

    def __add__(self, other):
        """Return a new Point whose coordinate are the sum of this one's and the other one's

        >>> p = Point(2, 4)
        >>> q = p + Point(3, 5)
        >>> q
        Point(5, 9)
        """
        return Point(self.x + other.x, self.y + other.y)

    def __iadd__(self, other):
        """Retrun a new Point whose coordinate are the sum of this one's and the other one's

        >>> p = Point(2, 4)
        >>> p += Point(3, 5)
        >>> p
        Point(5, 9)
        """
        self.x += other.x
        self.y += other.y
        return self

    def __sub__(self, other):
        """ Point(3, 5) - Point(3, 4) = Point(0, 1)

        >>> p = Point(3, 5)
        >>> q = p - Point(2, 5)
        >>> q
        Point(1, 0)
        """
        return Point(self.x - other.x, self.y - other.y)

    def __isub__(self, other):
        """Returns this Point with its coordinate set to the differencd
        of this one's and the other one's

        >>> p = Point(2, 3)
        >>> p -= Point(3, 6)
        >>> p
        Point(-1, -3)
        """
        self.x -= other.x
        self.y -= other.y
        return self

    def __mul__(self, other):
        """Return a new Point whose coordinate is this one's mutiplied
        by the other nmuber

        >>> p = Point(2, 4)
        >>> q = p * 3
        >>> q
        Point(6, 12)
        """
        return Point(self.x * other, self.y * other)       # create a new Point object

    def __imul__(self, other):
        """Return a new Point whose coordinate is this one's multiplied
        by the other number

        >>> p = Point(4, 6)
        >>> p *= 3
        >>> p
        Point(12, 18)
        """
        self.x *= other     # create new object for x
        self.y *= other
        return self        # Point object reference not change

    def __truediv__(self, other):
        """Return this Point with its coordinate set to this one's
        divided by other number

        >>> p = Point(2, 5)
        >>> p /= 2
        >>> p
        Point(1.0, 2.5)
        """
        self.x /= other
        self.y /= other
        return self

    def __floordiv__(self, other):
        """Returns a new Point whose coordinate is this one's floor
        divided by the other number

        >>> p = Point(2, 4)
        >>> q = p // 2
        >>> q
        Point(1, 2)
        """
        return Point(self.x // other, self.y // other)

    def __ifloordiv__(self, other):
        """Returns this Point with its coordinate set to this one's
        floor divided by the other number

        >>> p = Point(2, 4)
        >>> p //= 2
        >>> p
        Point(1, 2)
        """
        self.x //= other
        self.y //= other
        return self

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return "Point({0.x!r}, {0.y!r})".format(self)

    def __str__(self):
        return "({0.x!r}, {0.y!r})".format(self)


class Circle(Point):

    def __init__(self, radius, x=0, y=0):
        """A Circle

        >>> circle = Circle(2)
        >>> circle
        Circle(2, 0, 0)
        """
        super().__init__(x, y)
        self.radius = radius

    def edge_distance_from_origin(self):
        """The distance of the circle's edge from the origin

        >>> circle = Circle(2, 3, 4)
        >>> circle.edge_distance_from_origin()
        3.0
        """
        return abs(self.distance_from_origin() - self.radius)

    def area(self):
        """The circle's area

        >>> circle = Circle(3)
        >>> a = circle.area()
        >>> int(a)
        28
        """
        return math.pi * (self.radius ** 2)

    def circumference(self):
        """The circle's circumference

        >>> circle = Circle(3)
        >>> d = circle.circumference()
        >>> int(d)
        18
        """
        return 2 * math.pi * self.radius

    def __eq__(self, other):
        return self.radius == other.radius and super().__eq__(other)

    def __repr__(self):
        return "Circle({0.radius!r}, {0.x!r}, {0.y!r})".format(self)

    def __str__(self):
        return repr(self)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
