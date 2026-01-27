'''
write a program to accept month number from user and display how many days month has. (use logical operator or)
    input : 1 output : this month has 31 days 
    input : 4 output : this month has 30 days 
'''

month = int(input("Enter the month is : "))

if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12 :
    print("this month is 31 days")

elif month == 2 or month == 4 or month == 6 or month == 9 or month == 11 :
    print("this month is 30 days")

elif month == 2:
    print("this month is 28 or 29 days")

else :
    print("THIS MONTH NUMBER IS NOT VALIAD Plz NUMBER IS 1-12 :")

    print("GOOD BYE")
    