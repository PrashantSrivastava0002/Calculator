print("Select a operation to perform")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

operation = input()

if operation == "1":
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    print("The sum is " + str(float(num1)+float(num2)))

elif operation =="2":
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    print("The difference is " + str(float(num1)-float(num2)))

elif operation == "3":
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    print("The multiple is "+ str(float(num1)*float(num2)))
elif operation == "4":
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    print("The result is: "+ str(float(num1)/float(num2)))
else:
    print("Enter the valid code the code is invaid: ")