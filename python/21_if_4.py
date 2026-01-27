# write a program to accept length and width of two different farm from user. and find out & display which farm is bigger 

length1 =float(input("Enter length of 1 farm: "))
width1 =float(input("Enter width of 1 farm: "))

total1 = length1*width1

length2=float(input("Enter length of 2 farm: "))
width2 =float(input("Enter width of 2 farm: "))

total2 = length2*width2

print(total1)
print(total2)

if total1>total2:
    print("First farm is bigger")
if total1<total2:
    print("second farm is bigger")
if total1==total2:
    print("Both farms are same")

print("good by")