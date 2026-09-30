#instead of static keyword python has class variable and instance variable, it does'nt require static keyword as any variable declared inside a class automatically becomes a class(static) variable

#class variable - it belongs to the class itself rather than any specific object.

class Student:
    school ="abc" # class variable

s1 = Student()
s2 = Student()

print(s1.school)
print(s2.school)

#instance variable - it belongs to the specific object , each object maintain its specific body
class Cat:
    def __init__(self, name):
        self.name = name #instance variable

c1 = Cat("shiro")
c2 = Cat("ginger")

print(c1.name)
print(c2.name)
