# SIMPLE CALCULATOR

a = float(input("ENTER FIRST NUMBER: "))
op = input("ENTER OPERATOR (+, -, *, /, //, %, **): ")
b = float(input("ENTER SECOND NUMBER: "))

if op == "+":
    print("RESULT: ", a + b)
elif op == "-":
    print("RESULT: ", a - b)
elif op == "*":
    print("RESULT: ", a * b)
elif op == "/":
    print("RESULT: ", a / b)
elif op == "//":
    print("RESULT: ", a // b)
elif op == "%":
    print("RESULT: ", a % b)
elif op == "**":
    print("RESULT: ", a ** b)
else:
    print("INVALID OPERATOR")
