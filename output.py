opcodes = ["load", "store", "loadI", "add", "sub", "mult", "lshift", "rshift", "output", "nop"]
grammar = ["MEMOP", "LOADI", "ARITHOP", "OUTPUT", "NOP", "CONSTANT", "REGISTER", "COMMA", "INTO", "ENDFILE", "NEWLINE"]

import scanner
def get_next_token(line):
    if scanner.eof == True:
        return (9, "")
    else:
        token = scanner.scan_word(line)
        return(token)

def print_tokens(file):
    line = scanner.scan_line(file)
    scanner.line_count += 1
    token = (0, "")
    while token != ((9, "")):
        token = get_next_token(line)
        print(str(scanner.line_count) + ": " + str(format_token(token)))
        if token[0] == 10:
            scanner.line_count += 1
            scanner.line_index = 0
            line = scanner.scan_line(file)
# def print_tokens(file):
#     line = scanner.scan_line(file)
#     # if the line is the end of file print out the token
#     if scanner.EOF == True:
#         print(str(scanner.line_count) + ": " + str(format_token(line)))

#     # keep reading words until end of file
#     while scanner.EOF == False:
#         token = scanner.scan_word(line)

#         #skip the rest of the line if there is an error or a comment
#         if token[0] == -1:
#             print(str(scanner.line_count) + ": " + str(format_token((10, 0))))
#             scanner.line_count += 1
#             scanner.line_index = 0
#             line = scanner.scan_line(file)
#             # check if the new line is the end of file
#             if scanner.EOF == True:
#                 print(str(scanner.line_count) + ": " + str(format_token(line)))
        
#         else:
#             print(str(scanner.line_count) + ": " + str(format_token(token)))
#             # check for new line
#             if token[0] == 10:
#                 scanner.line_count += 1
#                 scanner.line_index = 0
#                 line = scanner.scan_line(file)

#                 # check if the new line is the end of file
#                 if scanner.EOF == True:
#                     print(str(scanner.line_count) + ": " + str(format_token(line)))

def format_token(token: tuple):
    '''
    Formats the token to be printed in the format:
    < grammar, "lexeme" >
    '''
    grammar_idx, lexeme_idx = token
    # opcode grammars
    if grammar_idx >=0 and grammar_idx <= 4:
        return f'< {grammar[grammar_idx]}, "{opcodes[lexeme_idx]}" >'
    # constant grammar
    elif grammar_idx == 5:
        return f'< {grammar[grammar_idx]}, "{lexeme_idx}" >'
    # register grammar
    elif grammar_idx == 6:
        return f'< {grammar[grammar_idx]}, "r{lexeme_idx}" >'
    # comma grammar
    elif grammar_idx == 7:
        return f'< {grammar[grammar_idx]}, "{lexeme_idx}" >'
    # into grammar
    elif grammar_idx == 8:
        return f'< {grammar[grammar_idx]}, "{lexeme_idx}" >'
    # end of file grammar
    elif grammar_idx == 9:
        return f'< {grammar[grammar_idx]}, "" >'
    # new line grammar
    elif grammar_idx == 10:
        return f'< {grammar[grammar_idx]}, "\\n" >'
        
        
    

    

