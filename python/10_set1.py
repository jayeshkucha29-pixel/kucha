#write a program to convert given 3 digit amount into words
# input : 175 output : one seven five 

number = int(input("enter number 3 digit "))
first = number //100
second = (number// 10) %10
last = number %10

words = ['zero','one','two','three','four','five','six','seven','eight','nine']
print(words[first],words[second],words[last])

##write a program to convert given 3 digit amount into words
# input : 175 output : one hundred seventy five  

amount= input("Enter number(3 digit :)")
amount=int(amount)

first=amount // 10 // 10


middle=amount // 10 % 10

last=amount % 10

words = ['zero','one','two','three','four','five','six','seven','eight','nine']
words2= ['zero','ten','twenty','thirty','fourty','fifty','sixty','seventy','eightty','ninety']
words3=['zero','hundred','two_hundread','three_hunded','four_hundread','five_hundread','six_hundread','seven_hundread','eight_hundread','nine_hundread']
print(words3[first]," ",words2[middle]," ",words[last])