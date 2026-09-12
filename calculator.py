# lates make a calculator

while True:
    try:
        num1 = int(input("please enter a number : "))
        num2 = int(input("please enter a second number : "))
        act = input("please enter an action : ")

        if act.strip() == "+":
            print(num1 + num2)
        elif act.strip() == "-":
            print(num1 - num2)
        elif act.strip() == "*":
            print(num1 * num2)
        elif act.strip() == "/":
            print(num1 / num2)
        elif act == "stop":
            break
    except ValueError:
        print("Error")
