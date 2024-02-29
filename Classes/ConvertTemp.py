# Class for converting degrees to farenheight and vice versa
class Temparature:
    def __init__(self,degree,farenheit) -> None:
        self.degree=degree
        self.farenheit=farenheit
    def Degreeconvert(self):
        degrees= self.farenheit/1.8+32
        print("the degree euivalent is:",degrees)
    def Farenheitconvert(self):
        farenheit= self.degree* 1.8 -32
        print("The farenheit equivalent is:",farenheit )
Degrees= float(input("Enter the degrees to be converted: "))
Farenheits= float(input("Enter the ferenheit measure to be converted: "))
temp= Temparature(Degrees,Farenheits)
temp.Degreeconvert()
temp.Farenheitconvert()