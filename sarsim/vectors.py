# sarsim.vectors
# Vector helper methods for use in sarsim
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Fri Apr 18 22:46:25 2014 -0400
#
# Copyright (C) 2014 Bengfort.com
# For license information, see LICENSE.txt
#
# ID: vectors.py [] benjamin@bengfort.com $

"""
Vector helper methods for use in sarsim
"""

##########################################################################
## Imports
##########################################################################

import numpy as np

##########################################################################
## Vector Class
##########################################################################

class Vector(np.ndarray):
    """
    Helper class for standard vector computations
    """

    ##////////////////////////////////////////////////////////////////////
    ## Class method "constructors" of various types
    ##////////////////////////////////////////////////////////////////////

    @classmethod
    def arr(klass, array):
        """
        Constructor to initialze the array view
        """
        return array.view(klass)

    @classmethod
    def zero(klass):
        """
        Construct a zero vector
        """
        return klass.arr(np.zeros(2))

    @classmethod
    def arrp(klass, *coords):
        """
        Constructor to initialize from a Python type (tuple or list)
        """
        return klass.arr(np.array(coords))

    @classmethod
    def rand(klass, low, high=None):
        """
        Construct a random integer vector with values in the range from
        low to high, unless high is None, then from 0 to low. The default
        shape of this vector is 2 (for 2 dimensional particle physics).
        """
        return klass.arr(np.random.randint(low, high, size=2))

    ##////////////////////////////////////////////////////////////////////
    ## Vector computation on the array
    ##////////////////////////////////////////////////////////////////////

    @property
    def unit(self):
        """
        Returns the unit vector (length 1) of this vector
        """
        if self.length > 0:
            return self / self.length
        return np.zeros_like(self)

    @property
    def length(self):
        """
        Compute the length of the vector
        """
        return np.linalg.norm(self)

    @property
    def orthogonal(self):
        """
        Returns the unit vector orthogonal in the +z direction
        """
        u = self.unit
        b = np.empty_like(u)
        b[0] = -u[1]
        b[1] = u[0]
        return self.arr(b)

    def angle(self, other, degrees=True):
        """
        Compute the angle between two vectors
        If degrees is true return degrees else radians
        """

        def angle_radians(self, other):
            angle = np.arccos(np.dot(self.unit, other.unit))
            if np.isnan(angle):
                if (self.unit==other.unit).all():
                    return 0.0
                return np.pi
            return angle

        angle = angle_radians(self, other)
        if degrees: return np.degrees(angle)
        return angle

    def distance(self, other):
        """
        Compute the Euclidean distance between two vectors
        """
        return np.linalg.norm(self-other)

if __name__ == '__main__':
    v1 = Vector.arr(np.array([2,4]))
    v2 = Vector.arr(np.array([0,1]))

    print v1.angle(v2)
