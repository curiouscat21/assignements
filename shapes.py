class Shape:
    def __init__(self):
        self.units = "meters"

    def area(self):
        pass

    def perimeter(self):
        pass

    def display(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        x = 3.14 * (self.radius ** 2)
        return x

    def perimeter(self):
        p = 2 * 3.14 * self.radius
        return p

    def display(self):
        print(f'The area of circle is {Circle.area(self)} Meters')
        print(f'The circumference of circle is {Circle.perimeter(self)} Meters')


class Square(Shape):
    def __init__(self, sides):
        self.sides = sides

    def area(self):
        x = self.sides ** 2
        return x

    def perimeter(self):
        p = 4 * self.sides
        return p

    def display(self):
        print(f'The area of square is {Square.area(self)} Meters')
        print(f'The perimeter of square is {Square.perimeter(self)} Meters')


class Rectangle(Shape):
    def __init__(self, l, w):
        self.l = l
        self.w = w

    def area(self):
        x = self.l * self.w
        return x

    def perimeter(self):
        p = 2 * (self.l + self.w)
        return p

    def display(self):
        print(f'The area of rectangle is {Rectangle.area(self)} Meters')
        print(f'The perimeter of rectangle is {Rectangle.perimeter(self)} Meters')





circle = Circle(9)
square = Square(11)
rectangle = Rectangle(5, 7)



circle.display()
square.display()
rectangle.display()


