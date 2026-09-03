num1 = float(input("input first number: "))

op = input("input operator (+, -, *, /): ")

num2 = float(input("input second nuber: "))

if op == "+":
    result = num1 + num2
elif op == "-":
    result = num1 - num2
elif op == "*":
    result = num1 * num2
elif op == "/":
    result = num1 / num2
else:
    result = "no valid operator entered"

print(result)

