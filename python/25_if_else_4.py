# write a program to find out which is cheaper approach to buy IPhone 17 pro max.  consider use is going usa should he buy iphone from usa or from india. 


india = int(input("ENETER THE INDIA IPHONE 17 PRO MAX PRICE"))
usa = int(input("ENTER THE USA IPHONE 17 PRO MAX PRICE"))

ans = usa * 38.5/100
total = usa+ans

if india<total:
    print("purchase from india is better than usa :",usa)

else:
    print("purchase from usa is better than india :",total)




