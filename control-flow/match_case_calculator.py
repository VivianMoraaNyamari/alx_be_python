"""
1. Prompt for User Input for Two Numbers
2. Ask for the type of operation they’d like to perform
3. Perform the Calculation Using Match Case
4. Output the Result
"""

num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
operation = input("Choose the operation (+, -, *, /):")

match operation:
    case "+":
         print(f"The result is {num1 + num2}")
    case "-":
         print(f"The result of {num1-num2}")
    case "*":
         print(f"The result of {num1*num2}")
    case "/":
        if num2 == 0:
         print("Cannot divide by zero.")
        else:
         print(f"The result of {num1 / num2}") 
    case _:
        print("Cannot divide by zero.")
    
    