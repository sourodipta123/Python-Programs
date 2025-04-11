n1=int(input("Enter first number: "))
n2=int(input("Enter Second number: "))
greatest=0
lcm=0
if n1>n2:
    greatest=n1
else:
    greatest=n2
while True: 
    if (greatest %n1==0) and (greatest %n2==0):
        lcm=greatest 
        break
    greatest=greatest+1
    
print("The LCM is: ",lcm)