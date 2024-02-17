def main():
    num1 = float(input("What's the first number? "))
    while True:
        operation = input("\n+ , - , * , /\nPick an operation: ")
        num2 = float(input("\nWhat's the second number? "))
        result = calculator(num1, operation, num2)
        print(f"{num1} {operation} {num2} = {result}")
        if input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ") == 'y':
            num1 = result
        else:
            num1 = float(input("What's the first number? "))
            continue

def calculator(num1, operation, num2):
    match (operation):
        case "+":
            result = num1 + num2
        case "-":
            result = num1 - num2
        case "*":
            result = num1 * num2
        case "/":
            result = num1 / num2
        case _:
            raise Exception("Invalid Operation")
    return result


if __name__ == "__main__":
    main()