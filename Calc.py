input1 = input("Select Menu: 1. Add 2. Subtract 3. Multiply 4. Divide"+"\n")
a = int(input("Enter first Number:"))
b = int(input("Enter Second Number:"))
if(input1 == "1"):
    print("The Sum is :",a+b)
elif(input1 == "2"): 
    print("The Difference is :",a-b)
elif(input1 == "3"): 
    print("The multiplication is :",a*b)
else: 
    print("The division is :",a/b)



