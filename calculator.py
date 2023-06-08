# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y
# This function is to exit
def exit():
    return print("exited")

print("---------------Calculator---------------\n")
print("Select an operation")
print("1 - Add")
print("2 - Subtract")
print("3 - Multiply")
print("4 - Divide")
print("5 - Quit")

while True:
    # User Input
    operation = input("Enter your choice(1/2/3/4/5): ")

    #Excutes the calculation if the given operation is correct or else it throws some error
    if operation in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if operation == '1':
            print("------Addition------\n")
            print(num1, "+", num2, "=", add(num1, num2))
            print("--------------------\n")

        elif operation == '2':
            print("------Subtraction------\n")
            print(num1, "-", num2, "=", subtract(num1, num2))
            print("--------------------\n")

        elif operation == '3':
            print("------Multiplycation------\n")
            print(num1, "*", num2, "=", multiply(num1, num2))
            print("--------------------\n")

        elif operation == '4':
            print("------Division------\n")
            print(num1, "/", num2, "=", divide(num1, num2))
            print("--------------------\n")
    
        # check if user wants another calculation
        another_calculation = input("Let's do next calculation? (yes/no): ")
        # breaking the while loop if answer is no
        if another_calculation == "no":
          break
    elif operation in ('5') :
        exit()
        break
    else:
        print("Invaild Input")