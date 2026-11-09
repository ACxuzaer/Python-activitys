
# Function Calculator Project

# Addition
def add(a, b):
    return a + b


# Subtraction
def subtract(a, b):
    return a - b


# Multiplication
def multiply(a, b):
    return a * b


# Division
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero!")
    return a / b


# Main Program
print("===== FUNCTION CALCULATOR =====")

print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

try:
    choice = int(input("Choose an operation (1-4): "))

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == 1:
        result = add(num1, num2)
        print("Result:", result)

    elif choice == 2:
        result = subtract(num1, num2)
        print("Result:", result)

    elif choice == 3:
        result = multiply(num1, num2)
        print("Result:", result)

    elif choice == 4:
        result = divide(num1, num2)
        print("Result:", result)

    else:
        print("Invalid operation! Please choose 1-4.")

except ZeroDivisionError as e:
    print("Error:", e)

except ValueError:
    print("Invalid input! Please enter numbers only.")

