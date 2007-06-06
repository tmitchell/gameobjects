from math import sqrt
from util import format_number

class Vector2(object):
    
    __slots__ = ('_v')
    
    def __init__(self, x=0., y=0.):
        """Initialise a vector
        
        x -- The x value (defaults to 0.), or a container of 2 values
        y -- The y value (defaults to 0.)
        
        """
        if hasattr(x, "__getitem__"):
            x, y = x
            self._v = [float(x), float(y)]
        else:
            self._v = [float(x), float(y)]
    
    def _get_length(self):
        x, y = self._v
        return sqrt(x*x + y*y)
    def _set_length(self, length):
        try:
            x, y = self._v
            l = length / sqrt(x*x +y*y)
        except ZeroDivisionError:
            self._v = [0., 0.]
            return self
        _v = self._v
        _v[0] = x*l
        _v[1] = y*l
        
        
    length = property(_get_length, _set_length, None, "Length of the vector")
    
    @classmethod
    def from_floats(cls, x, y):
        vec = cls.__new__(cls, object)
        vec._v = [x, y]        
        return vec
        
    @classmethod
    def from_iter(cls, iterable):
        """Creates a Vector2 object from an iterable.
        iterable -- An iterable of at least 2 numeric values
        
        """
        next = iter(iterable).next
        vec = cls.__new__(cls, object)        
        vec._v = [float(next()), float(next())]        
        return vec

        
    @classmethod
    def from_points(cls, p1, p2):
        """Creates a Vector2 object between two points.
        p1  -- First point
        p2 -- Second point
        
        """
        v = cls.__new__(cls, object)
        x, y = p1
        xx, yy = p2
        v._v = [float(xx-x), float(yy-y)]        
        return v
    
    def copy(self):
        """Returns a copy of this object."""
        vec = self.__new__(self.__class__, object)
        vec._v = self._v[:]
        return vec
        
    def get_x(self):
        return self._v[0]
    def set_x(self, x):
        assert isinstance(x, float), "Must be a float"
        self._v[0] = x
    x = property(get_x, set_x, None, "x component.")
    
    def get_y(self):
        return self._v[1]
    def set_y(self, y):
        assert isinstance(x, float), "Must be a float"
        self._v[1] = y
    y = property(get_y, set_y, None, "y component.")
        
    u = property(get_x, set_y, None, "u component (alias for x).")
    v = property(get_y, set_y, None, "v component (alias for y).")
        
    def __str__(self):
        
        return "(%s, %s)" % (format_number(self.x), format_number(self.y))
    
    def __repr__(self):
        
        return "Vector2(%s, %s)" % (self.x, self.y)
        
    def __iter__(self):
        
        return iter(self._v[:])
        
    def __len__(self):
        
        return 2
    
    
    def __getitem__(self, index):
        """Gets a component as though the vector were a list."""
        try:
            return self._v[index]
        except IndexError:        
            raise IndexError, "There are 2 values in this object, index should be 0 or 1"    
            
    def __setitem__(self, index, value):
        """Sets a component as though the vector were a list."""
        
        assert isinstance(value, float), "Must be a float"
        try:
            self._v[index] = value
        except IndexError:        
            raise IndexError, "There are 2 values in this object, index should be 0 or 1!"        
     
     
    def __eq__(self, rhs):
        x, y = self._v
        xx, yy = rhs
        return x == xx and y == yy

    def __ne__(self, rhs):
        x, y = self._v
        xx, yy, = rhs
        return x != xx or y != yy
    
    def __hash__(self):
        
        x, y = self._v
        return hash((x, y))

    def __add__(self, rhs):
        x, y = self._v
        xx, yy = rhs
        return Vector2.from_floats(x+xx, y+yy)
        
        
    def __iadd__(self, rhs):
        x, y = self._v
        xx, yy = rhs
        self._v[0] = x + xx
        self._v[1] = y + yy
        return self
        
    def __radd__(self, lhs):
        x, y = self._v
        xx, yy = lhs
        return self.from_floats(x+xx, y+yy)
        
    def __sub__(self, rhs):
        x, y = self._v
        xx, yy = rhs
        return Vector2.from_floats(x-xx, y-yy)
        
    def __rsub__(self, lhs):
        x, y = self._v
        xx, yy = lhs
        return self.from_floats(xx-x, yy-y)
        
    def _isub__(self, rhs):
        
        xx, yy = rhs
        self._v[0] -= xx
        self._v[1] -= xx
        return self
        
        
    def __mul__(self, rhs):
        """Return the result of multiplying this vector with a scalar or a vector-list object."""
        x, y = self._v
        if hasattr(rhs, "__getitem__"):            
            xx, yy = rhs
            return Vector2.from_floats(x*xx, y*yy)
        else:
            return Vector2.from_floats(x*rhs, y*rhs)
            
            
    def __imul__(self, rhs):
        """Multiplys this vector with a scalar or a vector-list object.""" 
        if hasattr(rhs, "__getitem__"):
            xx, yy = rhs
            self._x *= xx
            self._y *= yy            
        else:
            self._x *= rhs
            self._y *= rhs
        return self
        
    def __rmul__(self, lhs):
        
        x, y = self._v
        if hasattr(lhs, "__getitem__"):
            xx, yy = lhs
        else:
            xx = lhs
            yy = lhs
        return self.from_floats(x*xx, y*yy)
        
        
    def __div__(self, rhs):
        """Return the result of dividing this vector by a scalar or a vector-list object."""
        x, y = self._v
        if hasattr(rhs, "__getitem__"):
            xx, yy, = rhs
            return Vector2.from_floats(x/xx, y/yy)
        else:
            return Vector2.from_floats(self._x/rhs, self._y/rhs)
            
            
    def __idiv__(self, rhs):
        """Divides this vector with a scalar or a vector-list object."""
        if hasattr(rhs, "__getitem__"):
            xx, yy = rhs
            self._x /= xx
            self._y /= yy            
        else:
            self._x /= rhs
            self._y /= rhs        
        return self
       
       
    def __neg__(self):
        """Return the negation of this vector."""
        x, y = self._v
        return Vector2.from_floats(-x, -y)
    
    def __pos__(self):
        
        return self.copy()
    
    def __nonzero__(self):
        
        x, y = self._v
        return x and y
    
    def __call__(self, keys):
        """Used to swizzle a vector.
        keys -- A string containing a list of component names
        i.e. vec = Vector(1, 2)
        vec('yx') --> (2, 1)
        
        """        
        
        ord_x = ord('x')
        _v = self._v
        return tuple( _v[ord(c) - ord_x] for c in keys )


    def as_tuple(self):
        """Converts this vector to a tuple."""
        return tuple(self._v)


    def get_length(self):
        """Returns the length of this vector."""
        x, y = self._v
        return sqrt(x*x +y*y)
    get_magnitude = get_length
        
        
    def normalise(self):
        """Normalises this vector."""
        x, y = self._v
        l = sqrt(x*x +y*y)
        try:
            _v = self._v
            _v[0] /= l
            _v[1] /= l
        except ZeroDivisionError:
            _v[0] = 0.
            _v[1] = 0.
        return self
    normalize = normalise
    
    def get_normalised(self):
        x, y = self._v
        l = sqrt(x*x +y*y)
        return Vector2.from_floats(x/l, y/l)
    get_normalized = get_normalised
            
    def get_distance_to(self, p):
        """Returns the distance to a point.
        
        p -- A Vector2 or list-like object with at least 2 values."""
        x = self._x
        y = self._y
        xx, yy = p
        dx = xx-x
        dy = yy-y
        return sqrt( dx*dx + dy*dy )

if __name__ == "__main__":
    
    v1 = Vector2(1, 2)    
    print v1('yx')
    print Vector2.from_points((5,5), (10,10))
    