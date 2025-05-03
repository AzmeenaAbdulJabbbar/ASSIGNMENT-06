class Dog:
    def __init__(self, name, breed):
        self.name = name  # Dog ka name
        self.breed = breed  # Dog ka breed

    def bark(self):
        print(f"{self.name} the {self.breed} says Woof!")
