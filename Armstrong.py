#Program to check armstrong number

num=int(input("Enter a number: "))
count=0
for i in str(num):
    count+= int(i)**3
if num == count:
    print("Armstrong")
else:
    print("Not Armstrong")