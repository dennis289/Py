# Using a class to calculate the area of a rectangle
class Rectangle:
        def __init__(self,length,width):
                self.length= length
                self.width= width
        def area (self):
                area= self.length*self.width
                print("The area is:",area)
        def perimeter (self):
                perimeter= (self.length+self.width)*2
                print("The perimeter is:",perimeter)
# Prompting the user to enter the values
len=int(input("Enter the length: "))
wid= int(input("Enter the width: "))
rectangle=Rectangle(len, wid)
rectangle.area()
rectangle.perimeter()