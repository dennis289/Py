# Using a class to calculate the area of a circle
class Circle:
    def __init__(self,radius):
        self.radius= radius
    def area(self):
        area_1=3.142*self.radius**2
        return area_1
    def perimeter(self):
        perimeter=2*3.142 *self.radius
        return perimeter
# Getting the input from the user
circe= Circle(7)
print(circe.area())
print(circe.perimeter())



