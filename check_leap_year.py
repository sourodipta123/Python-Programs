#Check whether a year is a leap year or not 

y = int(input("Enter the year: "))
if (y%4==0 and y%100!=0) or (y%400==0):
    print("Leap Year")
else:
    print("Not a Leap Year ")