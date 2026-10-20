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


# 1.1
def center_of_mass(points):
    x_sum = 0
    y_sum = 0
    z_sum = 0
    for p in points:
        x_sum += p.x
        y_sum += p.y
        z_sum += p.z

    n = len(points)
    return Vector(x_sum / n, y_sum / n, z_sum / n)

points = [
    Vector("{0, 0, 0}"),
    Vector("{2, 3, 4}"),
    Vector("{-1, 5, 2}"),
    Vector("{10, -2, 8}"),
    Vector("{4, 4, 4}")
]
print(center_of_mass(points).x, center_of_mass(points).y, center_of_mass(points).z)


# 1.2
def triangle_area(a, b, c):
    ab = abs(b - a)
    ac = abs(c - a)
    bc = abs(c - b)
    p = (ab + ac + bc) / 2
    return (p * (p - ab) * (p - ac) * (p - bc)) ** 0.5

def max_triangle_area(points):
    max_area = 0
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            for k in range(j + 1, len(points)):
                area = triangle_area(points[i], points[j], points[k])
                if area > max_area:
                    max_area = area
    return max_area

points = [
    Vector("{0, 0, 0}"),
    Vector("{2, 3, 4}"),
    Vector("{-1, 5, 2}"),
    Vector("{10, -2, 8}"),
    Vector("{4, 4, 4}")
]
print(max_triangle_area(points))