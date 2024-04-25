def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    if y==0:
        return "Cannot divide by zero"
    else:
        return x / y
    
def get_valid_number(prompt):
    while True:
        try:
            return float(input(prompt))   
        except ValueError:
            print("Invalid input. Please enter a valid number.")
             
             
def get_valid_operation():
    while True:
        operation =input("Enter operation (+, -, *,/): ")
        if operation in('+','-','*','/'):
            return operation 
        else:
            print("Invalid operation. Please choose from '+' , '-' , '*','/'.")
            

print("Welcome to Simple Calculator!")
while True:
    num1 = get_valid_number("Enter First number: ")
    num2 = get_valid_number("Enter Second number: ")
    operation = get_valid_operation()
    
    
    if operation == '+':
        print("Result:",add(num1,num2))
    elif operation == '-':
        print("Result:",subtract(num1,num2))
    elif operation == '*':
        print("Result:",multiply(num1,num2))
    elif operation == '/':
        print("Result:",divide(num1,num2))    
        
    
    choice = input("Do you want to perform another calculation? (yes/no): ")
    if choice.lower() != 'yes':
        print("Thank you for using Simple Calculator.")
        break            