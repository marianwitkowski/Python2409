
# Magiczne metody
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add_vector(self, v1):
        return Vector(self.x+v1.x, self.y+v1.y)

    def __str__(self):
        return f"[{self.x}, {self.y}]"

    def __add__(self, other):
        if type(other) is Vector:
            return Vector(self.x+other.x, self.y+other.y)
        if type(other) in [int, float]:
            return Vector(self.x+other, self.y+other)
        raise TypeError("Niepoprawny typ argumentu")

    def __eq__(self, other):
        return self.x==other.x and self.y==other.y

    def get_x(self):
        return (self.x, self.y)

    XY = property(get_x)


# Klasa statyczna
class Utils:

    @staticmethod
    def get_host():
        return "192.168.0.1:1234"

print(Utils.get_host())

vector1 = Vector(2,3)
print(vector1)
print(vector1.XY)
vector2 = Vector(-1, 1)
print(vector2)
vector3 = vector1.add_vector(vector2)
print(vector3)

vector3 = vector1 + vector2
print(vector3)

print(vector1 + 5)
#print(vector1 + (1,1) )

vector1 = Vector(2,2)
vector2 = Vector(2,2)
print(vector1==vector2)

vector2 = Vector(-2,2)
print(vector1==vector2)