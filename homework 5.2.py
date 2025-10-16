while True:

    num1 = float(input("Введите первое число: "))
    operation = input("Введите операцию: (+, -, *, /) ").strip()
    num2 = float(input("Введите второе число: "))


    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 == 0.0:
            print("Ділити на нуль не можна")
            result = None
        else:
            result = num1 / num2
    else:
        print("Невідома операція")
        result = None
    if result is not None:
        print(f"Результат: {result:.2f}")
    cont = input("Продовжити? (y/yes або т/так): ")
    cont = cont.strip().lower()
    if cont in ('y', 'yes', 'т', 'так'):
        continue
    else:  # иначе
        print("Завершення роботи.")
        break





