#python support compile time polymorphism using efault arguments *args and *kwargs , this is because moethod resolution happends during runtime.
#*args- it allows funtion to accept any number of position arguments. it acts like a tuple inside a function.

#**kwargs - it allows function to accept any number of keyword argumnts i.e. key = value pair. it act like a dictionary insiide a function.

class Calculator:
    def multiply(self, a=1,b=1,*args):
        result = a*b
        for num in args:
            result *=num
        return result

calc = Calculator()
print(calc.multiply(4))
print(calc.multiply(4,5))
print(calc.multiply(3,5,7,2))
print(calc.multiply(1,3,4,5,7,7))

class Animal:
    def sound(self):
        return "some kind of sound they make."

class cat(Animal):
    def sound(self):
        return "meow"

class dog(Animal):
    def sound(self):
        return "bark" 

animals = [dog(), cat(), Animal()]

for animal in animals:
    print(animal.sound())