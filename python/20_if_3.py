'''
write a program to convert 24 hours time into 12 hours format time and display it with AM PM message. 
        input : 15 hours 
        output  3 PM 

         input : 11 hours 
        output  11 AM 

        input : 25 hours 
        output  invalid input 
'''
hours = int(input("enter the hours"))

import sys
if hours>24:
    print("invalid input")
    sys.exit()

if hours<=12:
    print("time is ",hours,"AM")
if hours>12:
    print("time is ",hours-12,"PM")

