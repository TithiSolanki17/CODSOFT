print("<SIMPLE CALCULATOR>")

print("(+) Addition")
print("(-) Subtraction")
print("(*) Multiplication")
print("(/) Division")
print("(%) Mod")


while True:
    x = int(input("Enter first number:"))
    y = int(input("Enter second number:"))
    op = input("Enter an operator:")

    if op == '+':
        result = x + y
    elif op == '-':
        result = x - y 
    elif op == '*':
        result = x * y
    elif op == '/':
        result = x / y
    elif op == '%':
        result = x % y
    else:
        print("INVALID INPUT!...")

    print(x, ' ', op, ' ', y, '= ',result)

    ch = input("Want to Perform Another Calculation or Terminate? _Y/N_:")
    if ch == 'n' or ch == 'N':
        print("THANK YOU!")
        break

