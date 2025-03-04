
#[x] Menu function
#[x] Addition function
#[x] Division function
#[x] Write function to loop the program.
#[x] Multiplication function
#[x] Subtraction function
#[x] Write function to loop the program.
#[] Write function to check if result is odd or even

# menu function
def menu():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    operator_str = input("Enter operation (+, -, *, /): ")
    if operator_str == "+":
        result = addition(num1, num2)
        return result
    elif operator_str == "-":
         result = subtraction(num1, num2)
         return result
    elif operator_str == "*":
         result = multiplication(num1, num2)
         return result
    elif operator_str == "/":
         result = division(num1, num2)
         return result
    else:
         print("Invalid choice!")

#addition
def addition(num1, num2):
    return num1 + num2
#division
def division(num1, num2):
    return num1 / num2

def multiplication(num1, num2):
    return num1 * num2

def subtraction(num1, num2):
    return num1 - num2

# Function to loop the program by asking user if they want to continue after menu finishes if yes, continue, if no, exit.
def run_again():
     while True:
         answer = input("Do you want to continue? (y/n): ")
         if answer == "y" or answer == "Y":
             result = menu()
             print(result)
             odd_or_even(result)
             continue
         elif answer == "n" or answer == "N":
             print("Goodbye!")
             break
         else:
             print("Invalid choice!")
             continue
# Function to check if result is odd or even
def odd_or_even(result):
    if result % 2 == 0:
        print("The result is even.")
    else:
        print("The result is odd.")