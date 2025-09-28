#WAP to make a calculator using while loop.

num1 = int(input("Enter first number: "))
oper = input("Choose Operator (+, -, *, /). Enter '=' to get result: ")
res = num1

while oper != "=":
    num2 = int(input("Enter next number: "))

    if oper == "+":
        res += num2
    elif oper == "-":
        res -= num2
    elif oper == "*":
        res *= num2
    elif oper == "/":
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
            continue
        res /= num2
    else:
        print("Invalid operator!")

    print("Intermediate Result:", res)
    oper = input("Choose next Operator (+, -, *, /). Enter '=' to get result: ")

print("Final Result:", res)