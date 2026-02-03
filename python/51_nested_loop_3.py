'''
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
'''

number = 5 

for row in range(1,number+1):
    for number in range(1,row+1):
        print(number,end=' ')
    print(" ")


