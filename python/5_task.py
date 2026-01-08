#write a program to calculate GST tax amount from given bill amount and tax rate 

bill_amount = 0
tax_rate=0

bill_amount=input("enter the bill_amount")
tax_rate=input("enter the tax_rate")

bill_amount=float(bill_amount)
tax_rate=float(tax_rate)

gst_amount=(bill_amount*tax_rate)/100

print("gst tax amount is:",gst_amount)

