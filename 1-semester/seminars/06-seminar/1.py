# 1
class Vector:
    def __init__(self, x, y = None, z = None):
        if type(x) is str and y is None and z is None:
            cleaned = x.replace("{", "").replace("}", "").replace(" ", "").split(",")
            self.x = float(cleaned[0])
            self.y = float(cleaned[1])
            self.z = float(cleaned[2])
        else:
            self.x = x
            self.y = y
            self.z = z

        assert type(self.x) in (int, float)
        assert type(self.y) in (int, float)
        assert type(self.z) in (int, float)

    def __abs__(self):
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)


    def __mul__(self, other):
        if type(other) in (int, float):
            return Vector(self.x * other, self.y * other, self.z * other)
        return self.x * other.x + self.y * other.y + self.z * other.z

    