from math import sqrt


class Vector2D(tuple):
    def __new__(cls, x, y):
        return tuple.__new__(cls, (x, y))
    pass

    def normalized(self):
        if(self[0] != 0 and self[1] != 0):
        
            return Vector2D(self[0] / sqrt(self[0]*self[0]+self[1]*self[1]), self[1] / sqrt(self[0]*self[0]+self[1]*self[1]))
        else:
            return self
            