'''
 Write a program that takes a 5 subject marks from user. calculate total and Percentage  and prints the grade using the following conditions:

| Percentage | Grade |
| ---------- | ----- |
| 90-100     | A+    |
| 80-89      | A     |
| 70-79      | B     |
| 60-69      | C     |
| 50-59      | D     |
| below 50   | Need to improve  |
----------------------------------------
'''

sub1=int(input("ENTER THE SUBJECT 1 MARKS :-"))
sub2=int(input("ENTER THE SUBJECT 2 MARKS :-"))
sub3=int(input("ENTER THE SUBJECT 3 MARKS :-"))
sub4=int(input("ENTER THE SUBJECT 4 MARKS :-"))
sub5=int(input("ENTER THE SUBJECT 5 MARKS :-"))

totla=sub1+sub2+sub3+sub4+sub5
per=totla/5

print("totla is all subject is ",totla )
print("percentage is ",per )

if per >=90 and per <=100:
    print("GRADE : A+")

elif per >=80 and per <=89:
    print("GRADE : A")

elif per >=70 and per <=79:
    print("GRADE : B")

elif per >=60 and per <=69:
    print("GRADE : C")

elif per >=50 and per <=59:
    print("GRADE : D")

else:
    print("below 50 : Need to improve : ")
