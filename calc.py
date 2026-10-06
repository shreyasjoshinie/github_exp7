

while True:
    a=5
    b=10
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = 5

    if choice == '1':
        result = a + b
        print(f"The result of addition is: {result}")
    elif choice == '2':
        result = a - b
        print(f"The result of subtraction is: {result}")
    elif choice == '3':
        result = a * b
        print(f"The result of multiplication is: {result}")
    elif choice == '4':
        if b != 0:
            result = a / b
            print(f"The result of division is: {result}")
        else:
            print("Error! Division by zero.")
    elif choice == '5':
        print("Exiting the calculator.")
        break
    else:
        print("Invalid input. Please try again.")   