
#Edgar 
#[x] Menu function
#[x] Addition function
#[x] Division function

#HP
#[] Subtraction function
#[] Write function to loop the program. 
    #Once the program ends, ask user if they want to run the program again (Y/N)
    #If user enters Y, run the program again
    #If user enters N, end the program

#Amine
#[] Multiplication function
#[] Write function to check if result is odd or even

#menu
def menu(operator_str):
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    if operator_str == "+":
        print(addition(num1, num2))
    elif operator_str == "-":
        print(subtraction(num1, num2))
    elif operator_str == "*":
        print(multiplication(num1, num2))
    elif operator_str == "/":
        print(division(num1, num2))
    else:
        print("Invalid choice!")

#addition
def addition(num1, num2):
    sum = num1 + num2
    return sum
#division
def division(num1, num2):
    result = num1 / num2
    return result
#subtraction
    
#multiplication

    
