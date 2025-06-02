"""
1. Prompt User for Pattern Size
2. Draw the Pattern using While Loops and nested For Loops
"""

sizePattern = int(input("Enter the size of the pattern:"))

row = 1

while row <= sizePattern:
  for square in range (1, sizePattern + 1):  
    print("*", end="")
  print()
  row += 1