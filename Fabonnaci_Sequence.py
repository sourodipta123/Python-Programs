#Print Fabonnaci Series

n=int(input("Enter the maximum value: "))
x=0
y=1
z=0
for i in range(n):
    print(z)
    x=y
    y=z
    z=x+y