import math

class Sphere:
    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass

    def get_radius(self):
        return self.radius

    def get_mass(self):
        return self.mass

    def get_volume(self):
        v = (4 / 3) * math.pi * (self.radius ** 3)
        return round(v, 5)

    def get_surface_area(self):
        s = 4 * math.pi * (self.radius ** 2)
        return round(s, 5)

    def get_density(self):
        v = (4 / 3) * math.pi * (self.radius ** 3)
        d = self.mass / v
        return round(d, 5)