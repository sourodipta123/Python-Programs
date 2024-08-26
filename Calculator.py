# Calculator 
# Introduction information 
print('Enter + for Addition ')
print('Enter - for Subtraction ')
print('Enter × for Multiplication')
print('Enter ÷ for Division ')
print('Enter q of Q to quit the calculator \n')
# Initiating i=1
i=1
# loops started
# Checking the value of i and matching it with the condition 
while i>0:
# Using Functions
    def add():
        add=n1+n2
        print ("The sum is:",add)
    def sub():
        sub=n1-n2
        print ("The difference is:",sub)
    def mul():
        mul=n1*n2
        print("The product is:",mul)
    def div():
        div=n1/n2
        print("The quotient is:",div)
        
    #Input your choice of operator
    o=input("Enter your choice: ")
    
    # Condition to quit Calculator
    if o=='q' or o=='Q':
        print("Thank you")
        break
    
  # Input first numbet
    n1=int(input("Enter the first number: "))
  # Input second number
    n2=int(input("Enter the second number: "))
  
  #Conditions    
    if o=='+':
        add()
    elif o=='-':
        sub()
    elif o=='×':
        mul()
    elif o=='÷':
        div()
    else:
        print("Invalid Choice")
        
    