'''
write a program to accept 2 number from user. and accept choice for operations.
operations will be addition, subtraction, multiplication, division
do operation and display result as per user choice about operation using if elif else statements.

'''

number_1 =int(input("ENTER THE NUM 1 IS :-"))
number_2 = int(input("ENTER THE NUM 2 IS :-"))

choice =int(input("ENTER THE YOUR CHOICE NUMBER IS :-"))

if choice == 1:
    print("Result=", number_1+number_2)

elif choice == 2:
    print("Result=", number_1-number_2)

elif choice == 3:
    print("Result=", number_1*number_2)

elif choice == 4:
    print("Result=",number_1/number_2)

else:
    print("INVALID CHOICE ")
