class Human:
    def __init__(self, name):
        self.name = name
        
class Man(Human):
    pass

class Woman(Human):
    pass

def God():
    adam = Man("Adam")
    eva = Woman("Eva")
    return [adam, eva]