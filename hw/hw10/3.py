#basic subclasses adam and eve

class Human:
    def __init__(self,name:str="Abra Cadabra"):
        self.name = name
class Man(Human):
    def __init__(self,name:str="Adam"):
        super().__init__(name)
class Woman(Human):
    def __init__(self,name:str="Eve"):
        super().__init__(name)
def God():
    return [Man(),Woman()]
