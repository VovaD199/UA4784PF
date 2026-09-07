class polygon:
    def __init__(self, a, b):
        self.a = a
        self.b = b

class rectangle(polygon):
    def area(self):
        print(self.a * self.b)

rect = rectangle(5, 2)
rect.area()