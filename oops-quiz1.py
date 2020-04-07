class Piglet:
    years = 0
    def pig_years(self):
        return self.years * 18
piggy = Piglet()
print(piggy.pig_years())

piggy.years = 2
print(piggy.pig_years())

#OK, now it’s your turn! Have a go at writing methods for a class. Create a Dog class with dog_years based on the Piglet class shown before (one human year is about 7 dog years).

class Dog:
  years = 0
  def dog_years(self):
    return self.years * 7

fido=Dog()
fido.years=3
print(fido.dog_years())


#Constructors and other Special methods
class Apple:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor
siva = Apple("red", "sweet")
print(siva.flavor)


class Person:
    def __init__(self, name):
        self.name = ___
    def greeting(self):
        # Should return "hi, my name is " followed by the name of the Person.
        return ___

# Create a new instance with a name of your choice
some_person = ___
# Call the greeting method
print(some_person.___)


class Person:
    def __init__(self, name):
        self.name = name
    def greeting(self):
        # Should return "hi, my name is " followed by the name of the Person.
        return ("hi, my name is {}".format(self.name))

# Create a new instance with a name of your choice
some_person = Person("Siva")
# Call the greeting method
print(some_person.greeting())


#str method or string methods
class Apple:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor
    def __str__(self):
        return "This apple is {} and it flavor is {}".format(self.color, self.flavor)
arun = Apple("color", "flavor")
print(arun)


# dot strings

class Piglet:
    """Represents a piglet that can say their name."""
    years = 0
    name = ""
    def speak(self):
        """Outputs a message including the name of the piglet."""
        print("Oink! I'm{}! Oink!".format(Self.name))
    def pig_years(self):
        """Converts the current age to equivalent pig years."""
        return self.years * 18
help(speak)

def to_seconds(hours, minutes, seconds):
    """Returns the amount of seconds in the given hours, minutes and seconds."""
    return hours*3600+minutes*60+seconds

help(to_seconds)


class Person:
  def __init__(self, name):
    self.name = name
  def greeting(self):
    """Outputs a message with the name of the person"""
    print("Hello! My name is {name}.".format(name=self.name))

help(Person)
