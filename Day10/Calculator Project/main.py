import art
logo = art.logo
print(logo)


def add(n1, n2):
    return n1 + n2

add_func = add

# TODO: Write out the other 3  functions: substract, multiply, divide
def subtract(n1, n2):
    return n1 - n2
subtract_func = subtract

def divide(n1, n2):
    while (n1 != 0 and n2 != 0):
        return n1 / n2

divide_func = divide

def multiply(n1, n2):
    return  n1 * n2

multiply_func = multiply

# TODO : Add the 4 functions into a dictionary as values
# Dictionary keys: "+", "-", "*", "/"

computation = {
    "+": add_func,
    "-": subtract_func,
    "*": multiply_func,
    "/": divide_func
}

# TODO : Use the dictionary operations to perform calculations
# Multiply 4 by 8 using the dictionary

four_by_eight = computation["*"]
print(four_by_eight(4, 8))


# FUNCTIONALITY
def calculator():
    # 1 - Program asks the user to type the first number.
    first_number = float(input("Enter the first number : "))
    looper = True
    while looper :
        # 2 - Program asks the user to type a mathematical operator
        # (a choice of "+", "-", "*" or "/")
        operator = input("Choose an operator ('+', '-', '*' or '/') : ")
        # 3 - Program asks the user to type the second number.
        second_number = float(input("Enter the second number : "))

        # 4 - Program works out the result based on the chosen mathematical operator
        result = 0

        if operator == "+":
            result += (computation["+"](first_number, second_number))
        elif operator == "-":
            result += (computation["-"](first_number, second_number))
        elif operator == "*":
            result += (computation["*"](first_number, second_number))
        elif operator == "/":
            result += (computation["/"](first_number, second_number))
        else:
            print("Invalid operator")

        print(f"{first_number} {operator} {second_number} = {result}")

        # 5 - Program asks if the user wants to continue working with the previous result
        proceed = input(
                f"Would you like to continue computation with {result}?\n"
                f"Type 'y' to continue or 'n' start a new computation : ").lower()

        """
            # 6 -If yes, program loops to use the previous result as the first number 
            and then repeats the calculation process.
            """
        if proceed == "y":
            looper = True
            first_number = result
        elif proceed == "n":
            looper = False
            print("\n" * 20)
        else:
            print("Invalid input")


        print(f"{first_number} {operator} {second_number} = {result}")

print(calculator())






