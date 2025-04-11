a=int(input("Enter a number: "))
if a==1 or a==0:
    print(a,"is neither prime nor composite")
elif a==2:
    print(a,"is Prime")
else:
    for i in range(2,a):
        if (a%i==0) :
            print(a,"is composite")
            break
    else:
         print(a,"is prime")
            