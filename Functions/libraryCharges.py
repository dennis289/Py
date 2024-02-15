# importing date and time from the python library
from datetime import datetime
# A program to calculate the charges for the books borrowed in a library
def libCharges (bookId, dateDue, returnDate):
    time= returnDate-dateDue
    if time < 7 :
        charge= 20
    elif time >= 8 and time <14:
        charge= 50
    elif time >=15:
        charge= 100
        print('Your charges as upto now is: ',charge)
# Getting the input from users
bookId= int(input("Enter your book ID"))
dateDue= str(input("Enter when your book is due (YYYY-MM-DD): "))
returnDate=str(input("Enter when your book should be returned (YYYY-MM-DD) :"))
dateDue=datetime.strptime(dateDue,'%Y-%m-%d')
returnDate=datetime.strptime(returnDate,'%Y-%m-%d')
libCharges (bookId, dateDue, returnDate)