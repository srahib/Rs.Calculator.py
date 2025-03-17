# Assigment: Make a calculator using python programing

def calculator (num1,num2,operation):
    if operation == "addition":
        return num1+num2
    elif operation == "subtraction":
        return num1-num2
    elif operation == "multiplication":
        return num1*num2
    elif operation == "division":
        if num2 == 0 :
            return 'Division by 0 is not allowed'
        return num1/num2
    else:
        "Invalid Operation"    
    
        
#main program
def main():
    print("Wellcome to a my python calculator")
    num1 = float(input("Enter your first number: "))
    num2 = float(input("Enter your second number: "))
    print ("Choose the operation to perform : Addition, Subtraction, Multiplication, Division")
    operation = input("Enter operation: ").strip().lower()
    result = calculator(num1, num2, operation)
    print (f"The result of {operation} is: {result}")

main()    
