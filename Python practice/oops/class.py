class cat: #creates a class name cat
    species = "Persian" #class attribute , it will be shared at all instances of a class

    def __init__(self, name,age): #init is the constructor method use to initialize the object , self refers to the current object, allowing each object to store its own data
        self.name = name
        self.age = age

#creating object of a class
cat1 = cat("ginger",5)
cat2 = cat("memo",4)
print(cat1.name)
print(cat2.species)
print(cat1.age)