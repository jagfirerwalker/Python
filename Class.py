# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 19:00:56 2016

@author: mathias
"""

#class Clock(object):
#    def __init__(self, time):
#        self.time = time
#    def print_time(self):
#        time = '6:30'
#        print(self.time)
#
#clock = Clock('5:30')
#clock.print_time()
#
#class Clock(object):
#    def __init__(self, time):
#        self.time = time
#    def print_time(self, time):
#        print(time)
#
#clock = Clock('5:30')
#clock.print_time('10:30')
#
#class Clock(object):
#    def __init__(self, time):
#            self.time = time
#    def print_time(self):
#            print(self.time)
#
#boston_clock = Clock('5:30')
#paris_clock = boston_clock
#paris_clock.time = '10:30'
#boston_clock.print_time()


#class Weird(object):
#    def __init__(self, x, y): 
#        self.y = y
#        self.x = x
#    def getX(self):
#        return x 
#    def getY(self):
#        return y
#
#class Wild(object):
#    def __init__(self, x, y): 
#        self.y = y
#        self.x = x
#    def getX(self):
#        return self.x 
#    def getY(self):
#        return self.y
#
#X = 7
#Y = 8
#
#w2 = Wild(X, Y)
#print(w2.getX())
#print(w2.getY())
#w3 = Wild(17, 18)
#print(w3.getX())
#print(w3.getY())
#w4 = Wild(X, 18)
#print(w4.getX())
#print(w4.getY())
#X = w4.getX() + w3.getX() + w2.getX()
#print(X)
#print(w4.getX())
#Y = w4.getY() + w3.getY()
#Y = Y + w2.getY()
#print(Y)
#print(w2.getY())


#class Coordinate(object):
#    def __init__(self, x, y):
#        self.x = x
#        self.y = y
#
#    def getX(self):
#        # Getter method for a Coordinate object's x coordinate.
#        # Getter methods are better practice than just accessing an attribute directly
#        return self.x
#
#    def getY(self):
#        # Getter method for a Coordinate object's y coordinate
#        return self.y
#
#    def __str__(self):
#        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'
#        
#    def __eq__(self, other):
#        # First make sure `other` is of the same type 
#        assert type(other) == type(self)
#        # Since `other` is the same type, test if coordinates are equal
#        return self.getX() == other.getX() and self.getY() == other.getY()
#
#    def __repr__(self):
#        return 'Coordinate(' + str(self.getX()) + ', ' + str(self.getY()) + ')'
#        
#class intSet(object):
#    """An intSet is a set of integers
#    The value is represented by a list of ints, self.vals.
#    Each int in the set occurs in self.vals exactly once."""
#
#    def __init__(self):
#        """Create an empty set of integers"""
#        self.vals = []
#
#    def insert(self, e):
#        """Assumes e is an integer and inserts e into self""" 
#        if not e in self.vals:
#            self.vals.append(e)
#
#    def member(self, e):
#        """Assumes e is an integer
#           Returns True if e is in self, and False otherwise"""
#        return e in self.vals
#
#    def remove(self, e):
#        """Assumes e is an integer and removes e from self
#           Raises ValueError if e is not in self"""
#        try:
#            self.vals.remove(e)
#        except:
#            raise ValueError(str(e) + ' not found')
#
#    def intersect(self, other):
#        """Assumes other is an intSet
#           Returns a new intSet containing elements that appear in both sets."""
#        # Initialize a new intSet    
#        commonValueSet = intSet()
#        # Go through the values in this set
#        for val in self.vals:
#            # Check if each value is a member of the other set    
#            if other.member(val):
#                commonValueSet.insert(val)
#        return commonValueSet
#
#    def __str__(self):
#        """Returns a string representation of self"""
#        self.vals.sort()
#        return '{' + ','.join([str(e) for e in self.vals]) + '}'
#
#    def __len__(self):
#        """Returns the length of the set.
#           This method is called by the `len` built-in function."""
#        return len(self.vals)
#
#class A(object):
#    def __init__(self):
#        self.a = 1
#    def x(self):
#        print("A.x")
#    def y(self):
#        print("A.y")
#    def z(self):
#        print("A.z")
#
#class B(A):
#    def __init__(self):
#        A.__init__(self)
#        self.a = 2
#        self.b = 3
#    def y(self):
#        print("B.y")
#    def z(self):
#        print("B.z")
#
#class C(object):
#    def __init__(self):
#        self.a = 4
#        self.c = 5
#    def y(self):
#        print("C.y")
#    def z(self):
#        print("C.z")
#
#class D(C, B):
#    def __init__(self):
#        C.__init__(self)
#        B.__init__(self)
#        self.d = 6
#    def z(self):
#        print("D.z")
#        
#obj = D()
#obj.y()