class Circle:
    def __init__(self,radius):
        self.radius = radius
    def get_area(self):
        return 3.14 * (self.radius ** 2)

    def __sub__(self,other):
        radius_difference = abs(self.radius - other.radius)
        if radius_difference == 0:
            return Point(0,0)
        return radius_difference


class Point:
    def __init__(self,a,b):
        self.a = a
        self.b = b

circle_1 = Circle(20)
circle_2 = Circle(40)

print(circle_1 - circle_2)
print(circle_1.get_area())