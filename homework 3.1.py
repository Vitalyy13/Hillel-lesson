num1 = float(input("Введіть перше число: "))
num2 = float(input("Введіть друге число: "))
operation = input("Введіть дію (+, -, *, /): ")

if operation == '+':
    result = num1 + num2
    print(result)
elif operation == '-':
    result = num1 - num2
    print(result)
elif operation == '*':
    result = num1 * num2
    print(result)
elif operation == '/':
    if num2 == 0:
        print("Помилка: ділити на нуль не можна!")
    else:
        result = num1 / num2
        print(result)
else:
    print("Невідома дія! Використовуйте лише +, -, * або /.")
