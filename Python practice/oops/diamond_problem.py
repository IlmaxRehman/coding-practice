# diamond problem is the case of inheritence when a class inherites from twodifferenn classes which shared the common superclass. This creates ambiguity in inheritence hierarchy.

class Shape:
    def display(self):
        print("class shape")

class Circle(Shape):
    def display(self):
        print("class circle")

class Square(Shape):
    def display(self):
        print("class square")

class cylinder(Circle,Square):
    pass

obj = cylinder()
obj.display()
 # it calls circle , because unlike java python resolve the multiple inheritence dispute usinf Method Resolution Order(MRO)

print(cylinder.mro())

