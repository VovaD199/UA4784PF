#10.3.2
class Hooman:
    def __init__(self,name:str="Abra Cadabra"):
        assert name.strip(), "The name should be at least something and not just blank string or spaces..."
        #could also be achieved with len check
        self.name = name

    def Greet(self):
        print(f"Hello, dear hooman {self.name}!")

    @classmethod
    def GeneralInfo(cls):
        print(f"This {cls.__name__} belongs to Homosapiens")

    @staticmethod
    def PointOfLife():
        print("42")

if __name__ == "__main__":
    hooman = Hooman("Solid Snake")
    hooman.Greet()
    hooman.GeneralInfo()
    hooman.PointOfLife()
    Hooman.PointOfLife()
