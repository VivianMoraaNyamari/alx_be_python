"""
1. Prompt User for a Number(Save it in a variable name number)
2. Generate and Print the Multiplication Table(in the format: “X * Y = Z”, where X is the user’s number, Y is the current number in the loop, and Z is the product.)
"""

number = int(input("Enter a number to see its multiplication table:"))

for y in range(1,11):
    result = number * y
    print(f"{number} * {y} = {result} ")