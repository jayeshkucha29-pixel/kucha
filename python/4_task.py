#write a program to findout simple interest of given amount rate and year 

amount = 0
rate = 0
year = 0

amount=input("Enter the amount:")
rate=input("Enter the rate:")
year=input("Enter the year:")

amount=float(amount)
rate=float(rate)
year=float(year)

si=(amount*rate*year)/100

print("simple interest is ",si)