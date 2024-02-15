# the volume of a cylinder
def cy_volume(radius, height):
    volume= 3.142*radius**2 * height
    print("volume = ",volume) # (return volume )can also be used here 
    # when getting the dimentions from the user, we use:
radius=int(input("Enter radius"))
height= int(input("enter height "))
cy_volume(radius, height)
