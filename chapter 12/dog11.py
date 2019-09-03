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
    def walk(self):
        print(self.name, 'is walking')
# all dogs should walk unless is_working = True.
    def __str__(self):
        return "I'm a dog named " + self.name
# all ServiceDog objects are Dog objects
#not all Dogs are Service Dogs.
class ServiceDog(Dog):
    def __init__(self, name, age, weight, handler):
        Dog.__init__(self, name, age, weight)
        self.handler = handler
        self.is_working = False

    def walk(self):
        if self.is_working:
            print(self.name,'is helping its handler',
                  self.handler, 'walk')
        else:
            Dog.walk(self)


    def bark(self):
        if self.is_working:
            print(self.name, 'says, "I can\'t bark, I\'m working"')
        else:
            Dog.bark(self)

class Frisbee:
    def __init__(self, color):
        self.color = color

    def __str__(self):
        return "I'm a " + self.color + ' frisbee'
#FrisbeeDog is a Dog but not a ServiceDog
class FrisbeeDog(Dog):
    def __init__(self, name, age, weight):
        Dog.__init__(self, name, age, weight)
        self.frisbee = None

    def bark(self):
        if self.frisbee != None:
            print(self.name,
                        'says, "I can\'t bark, I have a frisbee in my mouth"')
        else:
            Dog.bark(self)
    def walk(self):
        if self.frisbee != None:
            print(self.name, 'says, "I can\'t walk, I\'m playing Frisbee!"')
        else:
            Dog.walk(self)

    def catch(self, frisbee):
        self.frisbee = frisbee
        print(self.name, 'caught a', frisbee.color, 'frisbee')

    def give(self):
        if self.frisbee != None:
            frisbee = self.frisbee
            self.frisbee = None
            print(self.name, 'gives back', frisbee.color, 'frisbee')
            return frisbee
        else:
            print(self.name, "doesn't have a frisbee")
            return None

    def __str__(self):
        str = "I'm a dog named " + self.name
        if self.frisbee != None:
            str = str + ' and I have a frisbee'
        return str
class Hotel:
    def __init__(self, name):
        self.name = name
        self.kennel = {}
        #instead of 2 lists, we are going to use a dictionary.

    def check_in(self, dog):
        if isinstance(dog, Dog):
             self.kennel[dog.name] = dog
             print(dog.name, 'is checked into', self.name)
        else:
             print('Sorry. You are not a dog. Only dogs are allowed in', self.name)

    def check_out(self, name):
        if name in self.kennel:
            dog = self.kennel[name]
            print(dog.name, 'is checked out of', self.name)
            del self.kennel[dog.name]
            return dog
        else:
            print('Sorry,', name, 'is not boarding at', self.name)
            return None
    def barktime(self):
        for dog_name in self.kennel:
            dog = self.kennel[dog_name]
            dog.bark()
# only checked-in dogs will have a bark-time.
class Cat():
    def __init__(self, name):
        self.name = name

    def meow(self):
        print(self.name, 'Says, "Meow"')

def test_code():
    codie = Dog('Codie', 12, 38)
    jackson = Dog('Jackson', 9, 12)
    rody = ServiceDog('Rody', 8, 38, 'Joseph')
    frisbee = Frisbee('red')
    dude =  FrisbeeDog('Dude', 5, 20)
    dude.catch(frisbee)

    codie.walk()
    jackson.walk()
    rody.walk()
    dude.walk()

test_code()
