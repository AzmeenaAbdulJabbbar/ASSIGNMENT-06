class Engine:
    def start(self):
        return "Engine is starting"

class Car:
    def __init__(self, brand, engine):
        self.brand = brand
        self.engine = engine 

    def start_car(self):
        return f"{self.brand} car is ready. {self.engine.start()}"