class Dog:
    def __init__(self,name,age,coat_colour):
        self.name=name
        self.age=age
        self.coat_colour=coat_colour
    def description(self):
        print(f"{self.name}is{self.age} years old.")

    def get_info(self):
        print(f"{self.name}has a {self.coat_colour} coat.")

class Jacky(Dog):
    def __init__(self,name,age,coat_colour, toy):
        super().__init__(name,age,coat_colour)
        self.toy=toy
    def description(self):
        super().description()
        print(f"{self.name} play with {self.toy}.")
    def get_info(self):
        super().get_info()
        print(f"{self.name} is a jacky")
class Bulldog(Dog):
    def __init__(self,name,age,coat_colour, Weight):
        super().__init__(name,age,coat_colour)
        self.Weight=Weight
    def description(self):
        super().description()
        print(f"{self.name} weight {self.Weight}.")
    def get_info(self):
        super().get_info()
        print(f"{self.name} is a Bulldog")
dog1 = Dog("buddy",5,"brown")
dog1.description()
dog1.get_info()

dog2 = Jacky("oscar",3,"white","tennis")
dog2.description()
dog2.get_info()

dog3 = Bulldog("daisy",7,"brindlr",50)
dog3.description()
dog3.get_info()