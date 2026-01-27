'''
 write a program to find out elder brother from given two brother's age. 
'''

age1 = int(input("Enter the age of first brother: "))
age2 = int(input("Enter the age of second brother: "))

if age1 > age2:
    print("first brother is elder")
elif age1 > age2:
    print("second brother is elder")

else:
    print("both brother are of same age")
    