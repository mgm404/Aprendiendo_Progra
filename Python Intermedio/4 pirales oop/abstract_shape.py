from abc import ABC, abstractmethod
import math
class Shape(ABC):
    @abstractmethod
    def calculate_perimeter(self):
        pass

    @abstractmethod
    def calculate_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius=radius
        super().__init__()


    def calculate_perimeter(self):
        perimeter=2*math.pi*self.radius
        return perimeter


    def calculate_area(self):
        area=math.pi*self.radius**2
        return area


class Square(Shape):
    def __init__(self, side):
        self.side= side
        super().__init__()

    def calculate_perimeter(self):
        perimeter=4*self.side
        return perimeter

    
    def calculate_area(self):
        area=self.side*self.side
        return area



class Rectangle(Shape):
    def __init__(self, base, height):
        self.base=base
        self.height=height
        super().__init__()


    def calculate_perimeter(self):
        perimeter=2*(self.base+self.height)
        return perimeter

    
    def calculate_area(self):
        area=self.base*self.height
        return area


circle1=Circle(5)
square1=Square(8)
rectangle1=Rectangle(5, 15)

print(circle1.calculate_area())
print(circle1.calculate_perimeter())

print(square1.calculate_area())
print(square1.calculate_perimeter())

print(rectangle1.calculate_area())
print(rectangle1.calculate_perimeter())