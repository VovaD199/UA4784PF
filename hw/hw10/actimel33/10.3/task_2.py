class Human:  
    """Represent a human being."""  

    def __init__(self, name: str):  
        self.name = name  

    def welcome(self) -> str:  
        return f"Welcome, {self.name}!"  

    @classmethod  
    def species(cls) -> str:  
        return "Homo sapiens"  

    @staticmethod  
    def arbitrary_message() -> str:  
        return "This is a static message"  



person = Human("Alice")
person.welcome()
print("Species:", Human.species())
print("Static message:", Human.arbitrary_message())
