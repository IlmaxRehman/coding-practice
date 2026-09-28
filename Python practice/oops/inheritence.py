class Animal:
    def __init__(self,name):
        self.name = name

    def info(self):
        print("Animal name :", self.name)


class cat(Animal):
    def sound(self):
        print(self.name, "meows")

c = cat("shiro")

c.info()
c.sound()

#when child dont have __init__ we did not need super() but when both chid and parent has init we need to super function, so that child csn hve its own verson and parent version also.

class dog(Animal):
    def __init__(self,name,breed):
        #call constructior based on MRO
        super().__init__(name)
        self.breed = breed

    def details(self):
        print(self.name,"is a",self.breed)

d= dog("pilu","stray")
d.info()
d.details()

#method overriding

class bird(Animal):
    def sound(self):
        print("sounds chichichichii")

b = bird()
c.info()
b.sound()