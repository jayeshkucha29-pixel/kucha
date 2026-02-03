# 100  95  90  85  80  75  70  65  60  ..... 0

num = 100

while num >=0:
    print(num,end=' ')
    num = num - 5

print("GOOD BYE")

# 1    8   27   125  ....... 1000

num = 1
print(num,end=' ')

while num<=9:
    num = num + 1
    print(num*num*num,end=' ')

print("JAY RAMDEVPIR")

# 1    -8   27  -64  .....    1000

num = 1
sign = 1

while num <=10:
    print(sign * (num*num*num),end=' ')
    sign = -sign
    num = num + 1

print("JAY RAMDEV PIR")



# 0    1   1   2   3   5   8   13  .... 100

num1 = 0
num2 = 1

while num1 <100:
    print(num1,end=' ')
    num3 = num1 + num2
    num1 = num2
    num2 = num3


   