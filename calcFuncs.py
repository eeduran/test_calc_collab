
#Edgar 
#[x] Menu function
#[x] Addition function
#[x] Division function
#[x] Write function to loop the program.

#addition
def addition(num1, num2):
    sum = num1 + num2
    return sum
#division
def division(num1, num2):
    result = num1 / num2
    return result

#Amine
#[] Multiplication function
def multiplication(num1, num2):
    return num1 * num2
#[] Write function to check if result is odd or even

###########HP
#[] Subtraction function
def subtraction(num1, num2):
    return num1 - num2

#[] Write function to loop the program.
def calculator():
    num1 = float(input("Enter first number: "))
    print("'+'\n'-'\n'*'\n'/'")
    operator_str = input("Choose your operation: ")
    should_continue = True
    result = 0.0
    
    while should_continue:
        num2 = float(input("Enter the next number: "))
        if operator_str == '+':
            result = addition(num1, num2)
        elif operator_str == '-':
            result = subtraction(num1, num2)
        elif operator_str == '*':
            result = multiplication(num1, num2)
        elif operator_str == '/':
            result = division(num1, num2)
        else:
            print("Invalid choice!")
        print(f"{num1} {operator_str} {num2} = {result}")
     #Once the program ends, ask user if they want to run the program again (Y/N)
        run_again = input("Do you want to have a new calculation? (y/n): ").lower()
       
        if run_again == 'y':   #If user enters Y, run the program again
            calculator()
        else:  #If user enters N, end the program
            should_continue = False

#menu

# def menu(operator_str):
#     num1 = int(input("Enter first number: "))
#     num2 = int(input("Enter second number: "))
#     if operator_str == "+":
#         print(addition(num1, num2))
#     elif operator_str == "-":
#         print(subtraction(num1, num2))
#     elif operator_str == "*":
#         print(multiplication(num1, num2))
#     elif operator_str == "/":
#         print(division(num1, num2))
#     else:
#         print("Invalid choice!")
