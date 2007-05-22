from math import sqrt
from util import format_number

class Vector2(object):
    
    __slots__ = ('_x', '_y')
    
    def __init__(self, x=0., y=0.):
        """Initialise a vector
        
        x -- The x value (defaults to 0.), or a container of 2 values
        y -- The y value (defaults to 0.)
        
        """
        if hasattr(x, "__getitem__"):
            self._x = float(x[0])
            self._y = float(x[1])
        else:
            self._x = float(x)
            self._y = float(y)
    
    def _get_length(self):
        return sqrt(self._x*self._x+self._y*self._y)
    def _set_length(self, length):
        try:
            l = length / sqrt(self._x*self._x+self._y*self._y)
        except ZeroDivisionError:
            self._x = 0.
            self._y = 0.            
            return self
            
        self._x *= l
        self._y *= l
        self._z *= l
        
    length = property(_get_length, _set_length, None, "Length of the vector")
    
    @classmethod
    def from_floats(cls, x, y):
        vec = cls.__new__(cls, object)
        vec._x = x
        vec._y = y
        return vec
        
    @classmethod
    def from_iter(cls, iterable):
        """Creates a Vector2 object from an iterable.
        iterable -- An iterable of at least 2 numeric values
        
        """
        it = iter(iterable)
        vec = cls.__new__(cls, object)
        vec._x = float(it.next())
        vec._y = float(it.next())
        return vec

        
    @classmethod
    def from_points(cls, p1, p2):
        """Creates a Vector2 object between two points.
        p1  -- First point
        p2 -- Second point
        
        """
        v = cls.__new__(cls, object)
        v._x = p2[0] - p1[0]
        v._y = p2[1] - p1[1]
        return v
    
    def copy(self):
        """Returns a copy of this object."""
        return Vector2.from_floats(self._x, self._y)
        
    def get_x(self):
        return self._x
    def set_x(self, x):
        self._x = float(x)
    x = property(get_x, set_x, None, "x component.")
    
    def get_y(self):
        return self._y
    def set_y(self, y):
        self._y = float(y)
    y = property(get_y, set_y, None, "y component.")
        
    u = property(get_x, set_y, None, "u component (alias for x).")
    v = property(get_y, set_y, None, "v component (alias for y).")
        
    def __str__(self):
        
        return "(%s, %s)" % (format_number(self._x), format_number(self._y))
    
    def __repr__(self):
        
        return "Vector2(%s, %s)" % (self._x, self._y)
        
    def __iter__(self):
        
        yield self._x
        yield self._y
        
    def __len__(self):
        
        return 2
    
    
    def __getitem__(self, index):
        """Gets a component as though the vector were a list."""
        if index == 0:
            return self._x
        elif index == 1:
            return self._y
        raise IndexError, "There are 2 values in this object, index should be 0 or 1"    
            
    def __setitem__(self, index, value):
        """Sets a component as though the vector were a list."""
        
        if index == 0:
            self._x = float(value)
        elif index == 1:
            self._y = float(value)
        raise IndexError, "There are 2 values in this object, index should be 0 or 1!"        
     
    def __eq__(self, rhs):
        
        return self._x == rhs._x and self._y == rhs._y

    def __ne__(self, rhs):
        
        return self._x != rhs._x or self._y != rhs._y

    def __add__(self, rhs):
        
        return Vector2.from_floats(self._x+rhs[0], self._y+rhs[1])
        
        
    def __iadd__(self, rhs):
        
        self._x += rhs[0]
        self._y += rhs[1]
        return self
        
        
    def __sub__(self, rhs):
        
        return Vector2.from_floats(self._x-rhs[0], self._y-rhs[1])
        
        
    def _isub__(self, rhs):
        
        self._x -= rhs[0]
        self._y -= rhs[1]
        return self
        
        
    def __mul__(self, rhs):
        """Return the result of multiplying this vector with a scalar or a vector-list object."""        
        if hasattr(rhs, "__getitem__"):
            return Vector2.from_floats(self._x*rhs[0], self._y*rhs[1])
        else:
            return Vector2.from_floats(self._x*rhs, self._y*rhs)
            
            
    def __rmul__(self, rhs):
        """Multiplys this vector with a scalar or a vector-list object.""" 
        if hasattr(rhs, "__getitem__"):
            self._x *= rhs[0]
            self._y *= rhs[1]            
        else:
            self._x *= rhs
            self._y *= rhs
        return self
        
        
    def __div__(self, rhs):
        """Return the result of dividing this vector by a scalar or a vector-list object."""        
        if hasattr(rhs, "__getitem__"):
            return Vector2.from_floats(self._x/rhs[0], self._y/rhs[1])
        else:
            return Vector2.from_floats(self._x/rhs, self._y/rhs)
            
            
    def __idiv__(self, rhs):
        """Divides this vector with a scalar or a vector-list object."""
        if hasattr(rhs, "__getitem__"):
            self._x /= rhs[0]
            self._y /= rhs[1]            
        else:
            self._x /= rhs
            self._y /= rhs
        return self
       
       
    def __neg__(self):
        """Return the negation of this vector."""
        return Vector2.from_floats(-self._x, -self._y)
    
    def __call__(self, keys):
        """Used to swizzle a vector.
        keys -- A string containing a list of component names
        i.e. vec = Vector(1, 2)
        vec('yx') --> (2, 1)"""
        return tuple( getattr(self, "_"+key) for key in keys )


    def as_tuple(self):
        """Converts this vector to a tuple."""
        return (self._x, self._y)


    def get_length(self):
        """Returns the length of this vector."""
        return sqrt(self._x*self._x + self._y*self._y)
    get_magnitude = get_length
        
        
    def normalise(self):
        """Normalises this vector."""
        length = self.get_length()
        if length:
            self._x /= length
            self._y /= length        
    normalize = normalise
    
    def get_normalised(self):
        length = self.get_length()
        return Vector2(self._x / length, self._y / length)
    get_normalized = get_normalised
            
    def get_distance_to(self, p):
        """Returns the distance to a point.
        
        p -- A Vector2 or list-like object with at least 2 values."""
        return sqrt( (self._x - p[0])**2 + (self._y - p[1])**2 );    

if __name__ == "__main__":
    
    v1 = Vector2(1, 2)    
    print v1('yx')
    print Vector2.from_points((5,5), (10,10))
    