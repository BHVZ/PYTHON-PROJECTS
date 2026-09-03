print("SIMPLE CALCULATOR")
a = float(input("ENTER A NUMBER: "))
operator = input("ENTER OPERATOR (+, -, *, /): ")
b = float(input("ENTER ANOTHER NUMBER: "))
if operator == '+':
    result = a + b
elif operator == '-':
    result = a - b
elif operator == '*':
    result = a * b
elif operator == '/':
    if b == 0:
        result = "CANNOT DIVIDE BY ZERO"
    else:
        result = a / b
else:
    result = "INVALID OPERATOR"
print("RESULT: ",result)

