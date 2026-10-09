from abc import ABC, abstractmethod
import math
class Shape():
    @abstractmethod
    def calculate_perimeter():
        pass

    @abstractmethod
    def calculate_area():
        pass

class Circle(Shape):
    def __init__(self, radius, perimeter=0, area=0):
        self.perimeter= perimeter
        self.area= area
        self.radius=radius
        super().__init__()


    def calculate_perimeter(self, ):
        self.perimeter=2*math.pi*self.radius
        print(self.perimeter)


    def calculate_area(self, ):
        self.area=math.pi*self.radius**2
        print(self.area)


class Square(Shape):
    def __init__(self, side, perimeter=0, area=0):
        self.perimeter= perimeter
        self.area= area
        self.side= side
        super().__init__()

    def calculate_perimeter(self):
        self.perimeter=4*self.side
        print(self.perimeter)

    
    def calculate_area(self):
        self.area=self.side*self.side
        print(self.area)



class Rectangle(Shape):
    def __init__(self, base, height, perimeter=0, area=0):
        self.perimeter= perimeter
        self.area= area
        self.base=base
        self.height=height
        super().__init__()


    def calculate_perimeter(self):
        self.perimeter=2*(self.base+self.height)
        print(self.perimeter)

    
    def calculate_area(self):
        self.area=self.base*self.height
        print(self.area)


circle1=Circle(5)
square1=Square(8)
rectangle1=Rectangle(5, 15)

circle1.calculate_area()
circle1.calculate_perimeter()

square1.calculate_area()
square1.calculate_perimeter()

rectangle1.calculate_area()
rectangle1.calculate_perimeter()