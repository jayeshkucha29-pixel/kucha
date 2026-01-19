# Create a list of 10 numbers and find the sum using built-in functions.

numbers = [1,2,3,4,5,6,7,8,9,10]

total = sum(numbers)

print("list of numbers ",numbers)
print("sum of numbers",total)

#Given a list of numbers, find the maximum and minimum values.

numbers = [1,2,3,4,5,6,7]


maximum = max(numbers)
minimum = min(numbers)

print("list of the numbers",numbers)
print("maximum number of",maximum)
print("minimum number of",minimum)


#Create a tuple of 5 elements and find its length.

tuple=(11,22,33,44,55,66,77,88,0.3)

length = len(tuple)

print("tuple:",tuple)
print("length of tuple :",length)

#Reverse a list using slicing (no loop).

list = (11,22,33,44,55)

reversed_list = list[::-1]

print("original list :",list)
print("reveresed list",reversed_list)

#Count how many times a specific value appears in a list using built-in methods.

list = [2,3,4,2,5,6,2,3]

count = list.count(6)

print(count)

# calendar

import calendar

year = int(input("enter the year: "))
month = int(input("enter the month: "))

cal = calendar.monthcalendar(year,month)

print("mon,tu,we,th,fr,sa,su")
for week in cal:
    for day in week:
        if day == 0:
            print(" ", end=" ")
        else:
            print(f"{day:2}", end=" ")
        print()
        
