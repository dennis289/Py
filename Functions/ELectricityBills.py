# Using defined functions to calculate a customers electric bill
def electric_bill(id, cN, Uc):
    if Uc <=199:
        bill=Uc*1.20
    elif Uc >=200  and Uc< 400:
        bill= Uc*1.50
    elif Uc >=400  and Uc< 600:
        bill= Uc*1.50
    elif Uc >= 600:
        bill= Uc*1.50
    print ("Your electricity bill is", bill)
# Users input on the customer name, units consumed and their identification
id=int(input("Enter your Id "))
cN=str(input("enter customer name "))
Uc=float(input("Enter the units consumed "))
# Calling the defined function with the parameters
electric_bill(id, cN, Uc)
