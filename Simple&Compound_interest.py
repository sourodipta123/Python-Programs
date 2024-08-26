p=int(input("Enter the Principle: "))
r=int(input("Enter the Rate: "))
t=int(input("Enter the Time: "))

#Simple Interest calculating
si=(p*r*t)/100

#Compound Interest calculating
a=p*(1+r/100)**t
ci=a-p

print("The Simple Interest is : ",si)
print("The Compound Interest is: ",ci)
