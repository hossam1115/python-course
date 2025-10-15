def calculator(a, b, operation):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        return a / b
a = float(input("Enter first number: "))
operation = input("Enter operation (+, -, *, =,/): ")
b = float(input("Enter second number: "))
result = calculator(a, b, operation)
print(f"Result: {result}")