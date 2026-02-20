#5th class 3rd activity calculator
def add(x ,y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y 

def divide(x, y):
    return x / y

num1 = int(input("Enter number i"))
num2 = int(input("Enter number ii"))

print("Sum :", add(num1, num2))
print("Difference :", subtract(num1, num2))
print("Product :", multiply(num1, num2))
print ("Quotient :", divide(num1, num2))