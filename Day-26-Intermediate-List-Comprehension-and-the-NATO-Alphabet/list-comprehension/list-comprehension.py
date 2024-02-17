# Square Numbers
"""numbers = [1, 2, 3, 4, 5]
square_numbers = [n*n for n in numbers]

print(square_numbers)"""

# Even Number Filter
"""numbers = input().split(",")
even_numbers = [int(number) for number in numbers if int(number) % 2 == 0]

print(even_numbers)"""

# Data Overlap
with open("numbers-1.txt") as f:
    numbers_1 = [int(line) for line in f.readlines()]

with open("numbers-2.txt") as f:
    numbers_2 = [int(line) for line in f.readlines()]

common_numbers = [number for number in numbers_1 if number in numbers_2]

print(common_numbers)