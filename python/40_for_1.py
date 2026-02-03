#write a program to display only positive value from the numeric list using for loop
list = [12, -45, 7, -3, 89, -22, 0, 34, -9, 56,100,145,-5,500] #Array
#task count no of positive & negative values and display it after for loop finish
for item in list:
    if item>0:
        print(item,end=' ') # 12 -45 7 

print() #new line
print("Good bye")