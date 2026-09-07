class Polygon:  
    def __init__(self, sides: int):  
        self.sides = sides  

    def display_info(self) -> None:  
        print(f"This is a polygon with {self.sides} sides")  


class Rectangle(Polygon):  
    def __init__(self, length: float, width: float):  
        if length <= 0 or width <= 0:  
            raise ValueError("Length and width must be positive.")  

        super().__init__(4)  
        self.length = length  
        self.width = width  

    def area(self) -> float:  
        """Return the area of the rectangle."""  
        return self.length * self.width  



rect = Rectangle(5, 10)
print("Task 1 - Rectangle area:", rect.area())
rect.display_info()
