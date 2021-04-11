result = float(input("Введите первое число "))

while True:
    operation = input("Введите знак и второе число ")
    if (operation[0] == "="):
        print(f"Result: {result}")

    else:
        if (operation[0] == "+"):
            result += float(operation[1:])

        elif (operation[0] == "-"):
            result -= float(operation[1:])

        elif (operation[0] == "*"):
            result *= float(operation[1:])

        elif (operation[0] == "/"):
            result /= float(operation[1:])

        elif ((operation[0] == "*") & (operation[1] == "*")):
            result **= float(operation[3])

        else:
            print("Выбрана неверная операция!")