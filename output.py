opcodes = ["load", "store", "loadI", "add", "sub", "mult", "lshift", "rshift", "output", "nop"]
grammar = ["MEMOP", "LOADI", "ARITHOP", "OUTPUT", "NOP", "CONSTANT", "REGISTER", "COMMA", "INTO", "ENDFILE", "NEWLINE"]

import scanner
def print_tokens(file):
    line = scanner.scan_line(file)
    # if the line is the end of file print out the token
    if scanner.EOF == True:
        print(str(scanner.line_count) + ": " + str(format_token(line)))

    # keep reading words until end of file
    while scanner.EOF == False:
        token = scanner.scan_word(line)

        #skip the line if there is an error
        if token[0] == -1:
            scanner.line_count += 1
            scanner.line_index = 0
            line = scanner.scan_line(file)
        
        else:
            print(str(scanner.line_count) + ": " + str(format_token(token)))
            if token[0] == 10:
                scanner.line_count += 1
                scanner.line_index = 0
                line = scanner.scan_line(file)
                if scanner.EOF == True:
                    print(str(scanner.line_count) + ": " + str(format_token(line)))


def format_token(token: tuple):
    grammar_idx, lexeme_idx = token
    if grammar_idx != 5 and grammar_idx != 6:
        if grammar_idx <= 4:
            return f'< {grammar[grammar_idx]}, {opcodes[lexeme_idx]} >'
        elif grammar_idx == 7:
            return f'< {grammar[grammar_idx]}, "," >'
        elif grammar_idx == 8:
            return f'< {grammar[grammar_idx]}, "=>" >'
        elif grammar_idx == 9:
            return f'< {grammar[grammar_idx]}, "" >'
        elif grammar_idx == 10:
            return f'< {grammar[grammar_idx]}, "\\n" >'
        
        
    

    

