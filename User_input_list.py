'''Taking the items in the list as user input'''

list=[]
a=int(input("Enter the number of items in the list: "))
for j in range(a):
    b=input("Enter the items: ")
    list.append(b)
    
print(list)