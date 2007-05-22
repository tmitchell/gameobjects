from math import *
from copy import copy
from util import format_number

class Color(object):    
    """Represents an red, green, blue color, with an alpha component."""
    
    __slots__ = ('_r', '_g', '_b', '_a')
    

    def __init__(self, *args):
        """If no arguements are given the color is set to 1, 1, 1, 1 (full white).
        If 3 or 4 arguements are given they should be the red, gree and blue values with an optional
        alpha value.
        
        """        
        
        if len(args) == 0:
            self._r = self._g = self._b = self._a = 1. # Full white
            
        elif len(args) == 3 or len(args)==4:            
            self._r = float(args[0])
            self._g = float(args[1])
            self._b = float(args[2])
            self._a = 1.
            if args == 4:
                self._a = args[3]
        else:
            raise TypeError("Color.__init__() takes 0, 3 or 4 arguments (%i given)"%len(args))

    @staticmethod
    def copy(col):
        c = Color.__new__(Color, object)
        c._r = col._r
        c._g = col._g
        c._b = col._b
        c._a = col._a
        return c
    
    @staticmethod
    def from_html(col_str, a=1.):
        
        if len(col_str) != 7 or col_str[0:1]!='#':
            raise ValueError("Requires a color encoded in a html style string: '%s' is invalid"%col_str)
        
        def twos(c):
            for i in (1, 3, 5):
                yield c[i:i+2]
        
        c = Color.__new__(Color, object)        
        try:
            c._r, c._g, c._b = [ (float(int(s, 16)) / 255.) for s in twos(col_str) ]
        except ValueError:
            raise ValueError("Color components should be encoded as 2 hex characters: '%s' is invalid"%col_str)
                
        c._a = float(a)
        return c
        

    def get_r(self):
        return self._r
    def set_r(self, x):
        self._r = float(r)
    r = property(get_r, set_r, None, "Red component.")
    
    def get_g(self):
        return self._g
    def set_g(self, g):
        self._g = float(g)
    g = property(get_g, set_g, None, "Alpha component.")
    
    def get_b(self):
        return self._b
    def set_b(self, b):
        self._b = float(b)
    b = property(get_b, set_b, None, "Blue component.")
    
    def get_a(self):
        return self._a
    def set_a(self, a):
        self._a = float(a)
    a = property(get_a, set_a, None, "Alpha component.")

     
    def set(self, r, g, b, a=None):
        """Sets the red, green, blue and (optionally) the alpha component."""        
        
        self._r = r
        self._g = g
        self._b = b
        if a is not None:
            self._a = a
        return self
        
    def __str__(self):
        
        return "( red %s, green %s, blue %s, alpha %s )" % (format_number(self._r), format_number(self._g), format_number(self._b), format_number(self._a))
        
    def __repr__(self):
        
        return "Color(%s, %s, %s, %s)" % (self._r, self._g, self._b, self._a)
        
    def __getitem__(self, index):
        
        try:
            return getattr(self,  self.__slots__[index])
        except IndexError:
            raise IndexError("Color objects have 4 values, index should be 0, 1, 2 or 3")
            
    def __setitem__(self, index, value):
        
        try:
            setattr(self, self.__slots__[index], float(value))
        except:
            raise IndexError("Color objects have 4 values, index should be 0, 1, 2 or 3")
        
    def help(self):
        
        return "This is a Color object, used to represent a color"\
                "\n\tIt has the value %s"%self
                
    def __len__(self):
        
        return 4
        
    def __iter__(self):
        
        yield self._r
        yield self._g
        yield self._b
        yield self._a
        
    def __add__(self, rhs):
             
        return Color(self._r+rhs[0], self._g+rhs[1], self._b+rhs[2], self._a)
            
    def _radd__(self, rhs):
        
        self._r += rhs[0]
        self._g += rhs[1]
        self._b += rhs[2]
        return self
        
    def __sub__(self, rhs):
        
        return Color(self._r-rhs[0], self._g-rhs[1], self._b-rhs[2], self._a)
        
    def __rsub__(self, rhs):
                
        self._r -= rhs[0]
        self._g -= rhs[1]
        self._b -= rhs[2]
        return self
        
    def __mul__(self, rhs):
        
        if hasattr(rhs,"__getitem__"):
            return Color(self._r*rhs[0], self._g*rhs[1], self._b*rhs[2], self._a)
        else:            
            return Color(self._r*rhs, self._g*rhs, self._b*rhs, self._a)
        
    def __rmul__(self, rhs):
        
        if hasattr(rhs,"__getitem__"):
            self._r *= rhs[0]
            self._g *= rhs[1]
            self._b *= rhs[2]
        else:
            self._r *= rhs
            self._g *= rhs
            self._b *= rhs
        return self
            
    def __div__(self, rhs):
        
        if hasattr(rhs,"__getitem__"):
            return Color(self._r/rhs[0], self._g/rhs[1], self._b/rhs[2], self._a)
        else:
            return Color(self._r/rhs, self._g/rhs, self._b/rhs, self._a)
        
    def __rdiv__(self, rhs):
        
        if hasattr(rhs,"__getitem__"):
            self._r /= rhs[0]
            self._g /= rhs[1]
            self._b /= rhs[2]
        else:
            self._r /= rhs
            self._g /= rhs
            self._b /= rhs
        return self
        
    def as_tuple(self):
        
        return (self._r, self._g, self._b, self._a)

    def __int__(self):
        
        c = copy(self).saturate()
        a = int(c.a*255.)
        r = int(c.r*255.)
        g = int(c.g*255.)
        b = int(c.b*255.)
        i = (a<<24)|(r<<16)|(g<<8)|b
        return i
        
    def as_tuple_rgb(self):
        
        return (self._r, self._g, self._b)

    def as_tuple_rgba(self):
        
        return (self._r, self._g, self._b, self._a)
        
    def as_html(self):
        
        c = copy(self).saturate() * 255.
        return "#%02X%02X%02X"%(c.r, c.g, c.b)
        
    def saturate(self, min_value=0., max_value=1.):
                
        self._r = max( min_value, min(max_value, self._r) )
        self._g = max( min_value, min(max_value, self._g) )
        self._b = max( min_value, min(max_value, self._b) )
        self._a = max( min_value, min(max_value, self._a) )
        return self
            

# Some pre-defined colors
class Palette:
    
    black =     Color(0, 0, 0)
    blue =      Color(0, 0, 1)
    green =     Color(0, 1, 0)
    cyan =      Color(0, 1, 1)
    red =       Color(1, 0, 0)
    magenta =   Color(1, 0, 1)
    yellow =    Color(1, 1, 0)
    white =     Color(1, 1, 1)

    grey25 =    Color(.25, .25, .25)
    grey50 =    Color(.5, .5, .5)
    grey75 =    Color(.75, .75, .75)


        
if __name__ == "__main__":
    

    c1 = Color(.5, .2, .8)
    print c1
    c1 += (.1, .1, .4)
    print c1
    print c1.as_html()
    print Color.from_html(c1.as_html())
    
    print "%x"%int(c1)

    
    #print (c1 * 255).saturate(0,255)
        
    