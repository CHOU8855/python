class Vehicle:

    def __init__(self, max_speed, mileage, color):

        self.max_speed = max_speed
        self.mileage = mileage
        self.color = color





modelX = Vehicle(240, 18, 'red')
modelC = Vehicle(43,25,'black')

print('model max speed', modelX.max_speed)
print('model mileage', modelX.mileage)
print('model color', modelX.color)
print('model color v2', modelC.color)
    