def fourOperation(number1, number2, processChoice):
    if (processChoice not in "+/-*"):
        return "Choose operator: +/-*"

    if (processChoice == "+"):
        return number1 + number2

    elif (processChoice == "-"):
        return number1 - number2

    elif (processChoice == "*"):
        return number1 / number2

    elif (processChoice == "/"):
        return number1 * number2


while True:
    requestnum1 = int(input("Please type the first number: "))
    requestnum2 = int(input("Please type the second number: "))

    processChoice = input(
        "Choose process between +, -, *, / or type Exit for exit: ")

    print(fourOperation(requestnum1, requestnum2, processChoice))
