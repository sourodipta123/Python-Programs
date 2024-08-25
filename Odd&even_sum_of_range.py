#Sum of Even and Odd numbers of a range
n=int(input("Enter the range: "))
even=0
odd=0
for i in range(1,n+1):
    if i%2==0:
        even=even+i
    else:
        odd=odd+i
print("The sum of all odd numbers in the range is:",odd)
print("The sum of all even numbers in the range is:",even)