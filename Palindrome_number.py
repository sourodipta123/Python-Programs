n=int(input("Enter a number: "))
i=n
rev=0
while i>0:
    rev=(rev*10)+(i%10)
    i=int(i/10)
if rev==n:
    print(n,'is a Palindrome number')
else:
    print(n,'is not a palindrome number')