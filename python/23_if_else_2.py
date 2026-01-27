# write a program to find out whether given year is millennium year or not. using if else decision making statements.

year = int(input("Enter the year: "))

if year <= 0:
    print("Invalid input")
elif year % 1000 == 0:
    print(f"{year} is a millennium year.")
else:
    print(f"{year} is NOT a millennium year.")

print("Good bye....")
