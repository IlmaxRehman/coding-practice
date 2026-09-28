from abc import ABC, abstractmethod

class Greet(ABC):
    @abstractmethod
    def say_hello(self):
        pass #abstract method 

class English(Greet):
    def say_hello(self):
        return "hello!"

    def word(self):
        return "how are youu" # concrete method

g = English()
print(g.say_hello())