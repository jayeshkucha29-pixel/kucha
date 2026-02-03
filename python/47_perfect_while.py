#write a program to figure out whether given number  is perfect num

num=int(input("Enter a number: "))
sum=0
i=1
while i<num:
    if num%i==0:
        sum=sum+i
    i=i+1   
if sum==num:
    print(f"{num} is a perfect number") 
else:
    print(f"{num} is not a perfect number")
    