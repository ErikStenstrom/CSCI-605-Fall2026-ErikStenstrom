print("Welcome to the Simple Calculator!")
while True:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    num3 = 0

    print("Select an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    operation = input("Enter the operation number : ")
    if(operation == '1'):
        num3 = num1 + num2
        print("Result:" , num1, "+" ,num2 , "=" ,num3)
    elif(operation == '2'):
        num3 = num1 - num2
        print("Result:" , num1, "-" ,num2 , "=" ,num3)
    elif(operation == '3'):
        num3 = num1 * num2
        print("Result:" , num1, "*" ,num2 , "=" ,num3)
    elif(operation == '4'):
        if(num2 != 0):
            num3 = num1 / num2
            print("Result:" , num1, "/" ,num2 , "=" ,num3)
        else:
            print("Error: Division by zero is not allowed.")
            break
    again = input("Do you want to perform another calculation? (yes/no): ")
    if (again == "no"):
        break
print("Goodbye!")