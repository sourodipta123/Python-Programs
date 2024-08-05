#Print Fabonnaci Series

n=int(input("Enter the maximum value: "))
x=0
y=1
z=0
for i in range(1,n+1):
    print(z)
    x=y
    y=z
    z=x+y