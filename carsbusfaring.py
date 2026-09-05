class Car:
    def __init__(self, wheels_am, engine_hp):
        self.wheels = wheels_am
        self.engine = engine_hp

    def show_traits(self):
        print('Wheels(am):', self.wheels)
        print('Engine (hp):', self.engine)


class Kid(Car):


    def __init__(self, model, age, wheels_am, engine_hp):
        self.model = model
        self.age = age
        super().__init__(wheels_am, engine_hp)


    def show_traits(self):
        print('Model:', self.model)
        print('Age:', self.age)
        super().show_traits()

    def topspeed(self, topspeed):
        print(self.name, 'topseed is', topspeed)


childcar = Kid('Tesla', 10, 4, '250hp')


childcar.show_traits()




print('Is the mini car a subclass of the parent car/older model?', issubclass(Kid, Car))