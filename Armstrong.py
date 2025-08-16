n=int (input("Enter a number: "))
sum=0
num=n
l=len(str(n))
while(num>0):
    rem=num%10
    sum=sum+rem**l
    num=num//10

if n==sum:
    print("Armstrong")
else:
    print("Not a Armstrong")