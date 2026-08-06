#10.3.1
class Polygon:
    def __init__(self,shape):
        self.shape = shape

    def GetShape(self):
        return self.shape

class Rectangle(Polygon):
    def __init__(self,side_a:float,side_b:float):
        super().__init__("Rectangle")
        assert side_a > 0, "rectangles with non positive side lenghts do not exist((("
        assert side_b > 0, "rectangles with non positive side lenghts do not exist((("
        self.side_a = side_a
        self.side_b = side_b

    #i assume by "finds the square of the rectangle"
    #it is meant to find the **area** of the rectangle, so here you go
    def GetArea(self)->float:
        return self.side_a*self.side_b

if __name__ == "__main__":
    rec = Rectangle(3.14,1.68)
    print(rec.GetArea())
    print(rec.GetShape())  #just tried inherited method call 
    #rec = Rectangle(-42,0) #assertion error due to wrong data


