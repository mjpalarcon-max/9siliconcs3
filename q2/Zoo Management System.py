class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        return self.name + " makes a sound."

    def eat(self):
        return self.name + " eats."

class Lion(Animal):
    def make_sound(self):
        return self.name + " roars loudly!"

    def eat(self):
        return self.name + " eats fresh meat."

class Elephant(Animal):
    def make_sound(self):
        return self.name + " trumpets!"

    def eat(self):
        return self.name + " eats grass and fruits."

class Monkey(Animal):
    def make_sound(self):
        return self.name + " chatters!"

    def eat(self):
        return self.name + " eats bananas."

lion = Lion("Simba")
elephant = Elephant("Dumbo")
monkey = Monkey("George")
animals = [lion, elephant, monkey]

for animal in animals:
    print(animal.make_sound())
    print(animal.eat())
    