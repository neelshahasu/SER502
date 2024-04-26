import re

# Define token types
token_types = [
    ('BOOLEAN', r'True|False'),
    ('INTEGER', r'\d+'),
    ('STRING', r'"([^"\\]|\\.)*"'),
    ('OPERATOR', r'\+|\-|\*|\/|\=|\=\=|\!\=|\<|\>|\<=|\>=|and|or|not|\?|\:|\(|\)|\{|\}|\;'),
    ('IDENTIFIER', r'[a-zA-Z_]\w*'),
    ('KEYWORD', r'if|else|for|while|print'),
    ('NEWLINE', r'\n')
]

# Combine the regular expressions into a single regex
regex = re.compile('|'.join(f'(?P<{name}>{pattern})' for name, pattern in token_types))

def lexer(code):
    tokens = []
    line_num = 1
    position = 0

    while position < len(code):
        match = regex.match(code, position)
        if match:
            for name, value in match.groupdict().items():
                if value:
                    tokens.append((name, value, line_num))
            position = match.end()
        else:
            # If no match is found, increment position
            if code[position] == '\n':
                line_num += 1
            position += 1
    
    return tokens

# Test the lexer with some code
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

tokens = lexer(code)
for token in tokens:
    print(token)
