def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero"

def main():
    print("Welcome to the Simple Calculator!")
    print("Select an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1/2/3/4): ")

    # Get numbers from the user
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input! Please enter numerical values.")
        return

    if choice == "1":
        result = add(num1, num2)
        op = "+"
    elif choice == "2":
        result = subtract(num1, num2)
        op = "-"
    elif choice == "3":
        result = multiply(num1, num2)
        op = "*"
    elif choice == "4":
        result = divide(num1, num2)
        op = "/"
    else:
        print("Invalid choice!")
        return

    print(f"{num1} {op} {num2} = {result}")

if __name__ == '__main__':
    main()
