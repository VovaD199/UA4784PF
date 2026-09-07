from random import randint

class Polygon:
    def __init__(self, vertices: list):
        self.vertices = vertices

    def square(self):
        """Square of the polygon calculation"""
        pass


class Rectangle(Polygon):
    def is_valid(self) -> bool:
        if len(self.vertices) != 4:
            return False

        x_values, y_values = self._get_coordinate_values()

        if len(x_values) != 2 or len(y_values) != 2:
            return False

        expected_vertices = {
            (x,y)
            for x in x_values
            for y in y_values
        }

        return set(self.vertices) == expected_vertices

    def _get_coordinate_values(self):
        x_values = {point[0] for point in self.vertices}
        y_values = {point[1] for point in self.vertices}
        return x_values, y_values

    def square(self) -> float:
        x_values, y_values = self._get_coordinate_values()
        width = max(x_values) - min(x_values)
        height = max(y_values) - min(y_values)

        return width * height


if __name__ == "__main__":
    while True:
        choice = input("Choose the variant:"
                       "\n1. Random dots for rectangle"
                       "\n2. Own dots for rectangle by coordinates"
                       "\n0. Exit"
                       "\n\n Your choice: ")
        match choice:
            case "1":
                while True:
                    x1, x2 = randint(1, 100), randint(1, 100)
                    y1, y2 = randint(1, 100), randint(1, 100)
                    if x1 != x2 and y1 != y2:
                        dots = [(x1, y1), (x1, y2), (x2, y2), (x2, y1)]
                        rectangle = Rectangle(dots)
                        print("Rectangle validation...", end=" ")
                        if rectangle.is_valid():
                            print("True")
                            print(f"Random dots: {dots}")
                            print(f"The square of rectangle is: {rectangle.square()}")
                        print("============\n")
                        break

            case "2":
                vertices = input("Enter coordinates for axis-aligned rectangle (e.g., 0,0 0,2 4,2 4,0: ")
                dots = [
                    tuple(map(int, pair.split(",")))
                    for pair in vertices.split()
                ]
                rectangle = Rectangle(dots)
                print("Rectangle validation...", end=" ")
                if rectangle.is_valid():
                    print("True")
                    print(f"The square of rectangle is: {rectangle.square()}")
                else:
                    print("False"
                          "\nWrite a right coordinate")
                print("============\n")

            case "0":
                break

            case _:
                print("Invalid choice")
