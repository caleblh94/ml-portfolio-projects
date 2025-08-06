def calculator():
    num1 = float(input("enter first number: "))
    num2 = float(input("enter second number: "))
    op = input("enter operation (+,-,*,/): ")

    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            print("error cannot divide by zero.")
            return
    else:
        print("invalid operation")
        return

    print(f"Result: {result}")
    
if __name__ == "__main__":
    calculator()