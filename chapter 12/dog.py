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
    
def print_dog(dog):
    print(dog.name+"'s",'age is', dog.age,'and weight is', dog.weight)
codie= Dog('Codie', 12, 38)
jackson= Dog('Jackson', 9, 12)
print_dog(codie)
codie.bark()
print_dog(jackson)
jackson.bark()
