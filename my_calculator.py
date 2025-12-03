from decimal import Decimal

print("Welcome to my calculator")

repeat = "yes"
while repeat.lower() == "yes":
    # cycle while

    a = Decimal(input("Put your first number: "))
    b = Decimal(input("Put your second number: "))
    # input

    print("Choose your operation:")
    print("1 - addition")
    print("2 - subtraction")
    print("3 - multiplication")
    print("4 - division")
    # your choice, what you want to do

    choice = float(input("Choose your operation: "))

    def validate_numbers(a, b):
        return isinstance(a, Decimal) and isinstance(b, Decimal)
        # control date type = isinstance

    def add(a, b):
        return a + b

    def subtract(a, b):
        return a - b

    def multiply(a, b):
        return a * b

    def divide(a, b):
        return "Cannot be divided by 0" \
            if b == 0 \
            else round(a / b, 2)

    operations = {
        1: add,
        2: subtract,
        3: multiply,
        4: divide
    }

    if choice in operations:
        #you choice operations
        if not validate_numbers(a, b):
            print("You entered an invalid format, please enter a number:")
            # here control validate number
        else:
            result = operations[choice](a, b)
            print("Result:", result)
            # result
    else:
        print("Invalid choice")
        # invalid choice

    repeat = input("Do you want to continue? [yes/anything]: ")
    # finish cycle while