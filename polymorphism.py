from abc import ABC, abstractmethod


class Shape(ABC):
    
    def area(self):
        pass
    
    def perimeter(self):
        pass
    

class Circle(Shape):
    
    def __init__(self,radius):
        self._radius = radius
    
    def area(self):
        return 3.14 * (self._radius * self._radius)
    
    def perimeter(self):
        return 2 * 3.14 * self._radius
    
    
class Rectangle(Shape):
    
    def __init__(self, length, width):
        self._width = width
        self._length = length
        
    def area(self):
        return self._length * self._width
    
    def perimeter(self):
        return 2 * (self._length + self._width)
    
    
def print_area(shape : Shape): # objects of different superclasses are treated as a object of a common superclass.
    print(shape.area())
    
    
def print_perimeter(shape : Shape):
    print(shape.perimeter())
    
    
    
if __name__ == "__main__":
    
    rectangle_obj = Rectangle(5,8)
    circle_obj = Circle(7)
    print_area(rectangle_obj)
    print_area(circle_obj)
    print_perimeter(rectangle_obj)
    print_perimeter(circle_obj)
    
    
    
    