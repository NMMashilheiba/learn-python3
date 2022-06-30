num1 = float(input("Enter 1st number: "))
operator = input("Enter an opeator: ")
num2 = float(input("Enter 2nd number: "))

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "/":
    print(num1 / num2)
elif operator == "*":
    print(num1 *num2)
else:
    print("Invalid operator!")


