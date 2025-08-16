n=int(input("Enter Number: "))
st=str(n)   # converting to string 
l=len(st)   # length of string 
num=n
fh=1        # Initialization of fh=1

first_half=0  #first half of the number 
second_half=0  #second half of the number 

i=l//2    #Spliting the number into halfs

for j in range(1,i+1):
    fh=fh*10

#Value after splitting 
first_half=num//fh
second_half =num%fh

#checking Armstrong or not
sum=first_half + second_half 
sq=sum**2
if n==sq:
    print ("Tech Number ")
else:
    print ("Not a Tech number")