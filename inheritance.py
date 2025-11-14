from abc import ABC, abstractmethod

class Animal(ABC):
    
    @abstractmethod
    def make_sound(self):
        pass
    
    @abstractmethod
    def bark(self):
        pass
    
class Dog(Animal):
    
    def make_sound(self):
        return "Bow Bow"
    
    def bark(self):
        return "kow kow kow"
    
    
class GoldenRetriever(Dog):
    
    def make_sound(self): # method overriding, based on the object on which method has called it will excute the respective method.
        return "Golden Retriever bow bow."
    
    
if __name__ == "__main__":
    
    animal_obj = GoldenRetriever()
    print(animal_obj.make_sound())
    print(animal_obj.bark())