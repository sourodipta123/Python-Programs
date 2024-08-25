# Reversing a number
n=int(input("Enter a number: "))
i=n
rev=0
while i>0:
    rev=(rev*10)+(i%10)
    i=int(i/10)
print("The reverse of the number",n,"is:",rev)