import math

class Vector3D:
    def __init__(self, x = 0, y = 0, z = 0):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        """add two vectors"""
        return Vector3D(
            self.x + other.x,
            self.y + other.y,
            self.z + other.z
        )

    def magnitude(self):
        """Calculate length of vector"""
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)
    
    def __repr__(self):
        return f"Vector3D({self.x}, {self.y}, {self.z})"
    
    # def __sub__(self, other):
    #     """Subtract vectors: v1 - v2"""
    #     # YOUR CODE HERE
    #     pass

    # def dot(self, other):
    #     """Dot product: v1 · v2 = x1*x2 + y1*y2 + z1*z2"""
    #     # YOUR CODE HERE
    #     pass

    # def normalize(self):
    #     """Return unit vector (length = 1)"""
    #     # YOUR CODE HERE
    #     pass

# TEST IT NOW
if __name__ == "__main__":
    v1 = Vector3D(1, 2, 3)
    v2 = Vector3D(4, 5, 6)
    v3 = v1 + v2
    
    print(f"v1 = {v1}")
    print(f"v2 = {v2}")
    print(f"v1 + v2 = {v3}")
    print(f"Magnitude of v1: {v1.magnitude():.2f}")
    print("✅ Vector math works!")