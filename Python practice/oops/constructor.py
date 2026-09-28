# __new__ method is used to create a new instance of class, it allocates memory and return the new object
#it is useful while creating immutable objects

class ClassName:
    def __new__(cls,parameters):
        instance = super(ClassName,cls).__new__(cls)
        return instance

#constructors are special methods use to initilize the objects when they are created befoe class

#types of contructors
#1- default constructor -> does not take any parameter other than self

class Cat:
    def __init__(self):
        self.name = "shiro"
        self.color = "white"
        self.age = 5
cat = Cat()
print(cat.name)
print(cat.color)
print(cat.age)

#2- parameterized constructor -> accepts arguments to initilize the object's attribute
