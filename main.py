from lexer import lexer
from myparser import parse_program

# Sample code for testing
code = """
a = True
b = 10
c = "Hello, world!"

if b > 5:
    print("b is greater than 5")
else:
    print("b is less than or equal to 5")

for i = 1; i < 5; i++:
    print(i)

while b > 0:
    print(b)
    b -= 1

for i in range(1, 5):
    print(i)

print(a)
print(b)
print(c)
"""

# Tokenize the code
tokens = lexer(code)

# Parse the program
parsed_program = parse_program(tokens)

# Print the parsed program
print(parsed_program)
