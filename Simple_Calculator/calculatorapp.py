def calculator():
    try:
        x = int(input("Enter the first number: "))
        operation = input("Choose the operation (+, -, *, /): ")
        y = int(input("Enter the second number: "))

        if operation == '+':
            answer = x + y
        elif operation == '-':
            answer = x - y
        elif operation == '*':
            answer = x * y
        elif operation == '/':
            if y != 0:
                answer = x / y
            else:
                answer = "Error! Division by zero."
        else:
            answer = "Invalid operation"

        print(f"The result is: {answer}")

    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    calculator()
