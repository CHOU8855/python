class Parrot:

    species = 'bird'


    def __init__(self, name, age, personality, color, class_time):
        self.name = name
        self.age = age
        self.personality = personality
        self.color = color
        self.class_time = class_time



blu = Parrot('Blu',10,'bubbly','red','4 months')
woo = Parrot('Woo',15,'timid','rainbow','2 years')


print('Blu is a {}'.format(blu.species))
print('Woo is a {}'.format(woo.species))


print('Blu is {}'.format(blu.age))
print('Woo is {}'.format(woo.age))

print('Blus personality is {}'.format(blu.personality))
print('Woos personality is {}'.format(woo.personality))

print('Blus color is {}'.format(blu.color))
print('Woos color is {}'.format(woo.color))

print('Blu has been with the class for {}'.format(blu.class_time))
print('Woo has been with the class for {}'.format(woo.class_time))