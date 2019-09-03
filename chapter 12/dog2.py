# this is an introduction to object oriented programming OOP
# dog class  has some attributes (state) such as name, age, weight,and behavior ( or method) bark
class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        if self.weight > 29:
            print(self.name, 'says "WOOF WOOF"')
        else:
            print(self.name, 'says "woof woof')
    def human_years(self):
        human_age = self.age * 7
        return human_age

def print_dog(dog):
    print(dog.name+"'s",'age is', dog.age,'and weight is', dog.weight)
codie= Dog('Codie', 12, 38)
jackson= Dog('Jackson', 9, 12)
print_dog(codie)
print(codie.name+"'s in human years is", codie.human_years())
codie.bark()
print_dog(jackson)
print(jackson.name+"'s in human years is", jackson.human_years())
jackson.bark()
