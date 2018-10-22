class Person:

    aas = 0

    def __init__(self, name):

        self.name = name
        self.age = 23

        Person.aas += 1

    def say_hi(self):
        print('Hello, my name is', self.name, 'and', self.age)

    def how_many(self):
        print(Person.aas)


p = Person('Mukhlis')
p.say_hi()
p.how_many()
