class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        else:
            raise TypeError("Can only add Vector objects")


# Create Vector objects
v1 = Vector(3, 4)
v2 = Vector(2, 1)

# Use the + operator for vector addition
v3 = v1 + v2

print(v3.x, v3.y)  # Output: 5 5
