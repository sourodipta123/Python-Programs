n=int(input("Enter a number: "))
for j in range (1,n+1):
    if j*(j+1)==n:
        print ("Pronic number")
        break
else:
    print ("Not a Pronic number ")