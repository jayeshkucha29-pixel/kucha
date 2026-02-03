# write a program to figure out whether given number  is armstrong number or not

num = int(input("Enter a amstrong number : "))
temp = num
sum = 0

digits = len(str(num))  

while temp > 0:
    rem = temp % 10
    sum = sum + (rem ** digits)
    temp = temp // 10

if sum == num:
    print(num, "is an Armstrong number")
else:
    print(num, "is NOT an Armstrong number")