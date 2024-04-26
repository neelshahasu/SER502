def parse_program(tokens):
    program = []
    current_token_index = 0

    while current_token_index < len(tokens):
        statement, current_token_index = parse_statement(tokens, current_token_index)
        program.append(statement)

    return program

def parse_statement(tokens, current_token_index):
    current_token = tokens[current_token_index]

    if current_token[0] == 'KEYWORD':
        if current_token[1] == 'if':
            return parse_conditional_statement(tokens, current_token_index)
        elif current_token[1] == 'for':
            return parse_loop_statement(tokens, current_token_index)
        elif current_token[1] == 'while':
            return parse_loop_statement(tokens, current_token_index)
        elif current_token[1] == 'print':
            return parse_print_statement(tokens, current_token_index)
    else:
        return parse_assignment_statement(tokens, current_token_index)

def parse_assignment_statement(tokens, current_token_index):
    identifier_token = tokens[current_token_index]
    if identifier_token[0] != 'IDENTIFIER':
        raise SyntaxError('Expected identifier')
    
    # Check for the assignment operator
    assignment_token = tokens[current_token_index + 1]
    if assignment_token[0] != 'OPERATOR' or assignment_token[1] != '=':
        raise SyntaxError('Expected assignment operator')

    # Parse the expression
    expression, next_token_index = parse_expression(tokens, current_token_index + 2)

    return ('assignment', identifier_token[1], expression), next_token_index

def parse_conditional_statement(tokens, current_token_index):
    # Parse the condition
    condition, next_token_index = parse_expression(tokens, current_token_index + 1)

    # Skip the colon token
    next_token_index += 1

    # Parse the statement in the if block
    if_statement, next_token_index = parse_statement(tokens, next_token_index)

    # Skip the else keyword
    next_token_index += 1

    # Parse the statement in the else block
    else_statement, next_token_index = parse_statement(tokens, next_token_index)

    return ('conditional', condition, if_statement, else_statement), next_token_index

def parse_loop_statement(tokens, current_token_index):
    loop_token = tokens[current_token_index]

    if loop_token[1] == 'for':
        return parse_for_loop(tokens, current_token_index)
    elif loop_token[1] == 'while':
        return parse_while_loop(tokens, current_token_index)

def parse_for_loop(tokens, current_token_index):
    # Implement parsing for traditional for loop
    pass

def parse_while_loop(tokens, current_token_index):
    # Implement parsing for while loop
    pass


def parse_print_statement(tokens, current_token_index):
    # Parse the expression to be printed
    expression, next_token_index = parse_expression(tokens, current_token_index + 1)
    return ('print', expression), next_token_index


def parse_expression(tokens, current_token_index):
    current_token = tokens[current_token_index]

    # Check the token type to determine the type of expression
    if current_token[0] == 'BOOLEAN':
        return ('boolean', current_token[1]), current_token_index + 1
    elif current_token[0] == 'INTEGER':
        return ('integer', int(current_token[1])), current_token_index + 1
    elif current_token[0] == 'STRING':
        return ('string', current_token[1]), current_token_index + 1
    elif current_token[0] == 'IDENTIFIER':
        # Handle identifiers
        return ('identifier', current_token[1]), current_token_index + 1
    elif current_token[0] == 'OPERATOR':
        # Handle operators
        return ('operator', current_token[1]), current_token_index + 1
    elif current_token[0] == 'KEYWORD':
        # Handle keywords
        return ('keyword', current_token[1]), current_token_index + 1
    elif current_token[0] == 'NEWLINE':
        # Skip newline tokens
        return None, current_token_index + 1
    else:
        raise SyntaxError('Unexpected token: {}'.format(current_token))
