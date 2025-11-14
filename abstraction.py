from abc import ABC, abstractmethod

class Shape(ABC):
    
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass
    
class Rectangle(Shape):
    
    def __init__(self, length, width):
        self.__length = length
        self.__width = width
        
    def area(self):
        return self.__width * self.__length
    
    def perimeter(self):
        return 2 * (self.__width + self.__length)
    

if __name__ == "__main__":
    rectangle_obj = Rectangle(5,2)
    print(rectangle_obj)
    print(rectangle_obj.perimeter())
    print(rectangle_obj.area())
    