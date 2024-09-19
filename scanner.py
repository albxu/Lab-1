import sys

opcodes = ["load", "store", "loadI", "add", "sub", "mult", "lshift", "rshift", "output", "nop"]
syntactic_categories = ["MEMOP", "LOADI", "ARITHOP", "OUTPUT", "NOP", "CONSTANT", "REGISTER", "COMMA", "INTO", "EOF", "EOL"]
line_index = 0
EOF = False
line_count = 0
line_index = 0 


def scan_line(file):
    global EOF
    global line_count

    # Read the first line
    line = file.readline()

    # End of File
    if line == "":
        EOF = True
        return (9, "")
    
    line = line + '\n'
    
    return line

def scan_word(input_string):
    global line_index
    global line_count

    def next_char():
        global line_index
        line_index += 1
        return input_string[line_index - 1]

    # Read the first character
    c = next_char()

    # get rid of whitespace
    while c == ' ' or c == '\t':
        c = next_char()

    # nop opcode
    if c == 'n':
        c = next_char()
        if c == 'o':
            c = next_char()
            if c == 'p':
                c = next_char()
                if c == ' ':
                    return (4, 9)
                else:
                    opcode_whitespace_error("nop")
                    return (-1, 0)
            else:
                return "Error: Expected 'p' after 'no'"
        else:
            return "Error: Expected 'o' after 'n'"
    
    # lshift, load, and loadI opcodes
    if c == 'l':
        c = next_char()
        if c == 's':
            c = next_char()
            if c == 'h':
                c = next_char()
                if c == 'i':
                    c = next_char()
                    if c == 'f':
                        c = next_char()
                        if c == 't':
                            c = next_char()
                            if c == ' ':
                                return (2, 6)
                            else:
                                return "Error: Expected ' ' after 'lshift'"
                        else:
                            return "Error: Expected 'f' after 'lshi'"
                    else:
                        return "Error: Expected 'i' after 'l'"
                else:
                    return "Error: Expected 'h' after 'ls'"
            else:
                return "Error: Expected 's' after 'l'"
        elif c == 'o':
            c = next_char()
            if c == 'a':
                c = next_char()
                if c == 'd':
                    c = next_char()
                    if c == ' ':
                        return (0, 0)
                    if c == 'I':
                        return (1, 2)
                    else:
                        return "Error: Expected 'I' after 'load'"
                else:
                    return "Error: Expected 'd' after 'loa'"
            else:
                return "Error: Expected 'a' after 'l'"
        else:
            return "Error: Expected 's' after 'l'"
    
    elif c == 's':
        c = next_char()
        if c == 'u':
            c = next_char()
            if c == 'b':
                c = next_char()
                if c == ' ':
                    return (2, 4)
                else:
                    return "Error: Expected ' ' after 'sub'"
            else:
                return "Error: Expected 'b' after 'su'"
        if c == 't':
            c = next_char()
            if c == 'o':
                c = next_char()
                if c == 'r':
                    c = next_char()
                    if c == 'e':
                        c = next_char()
                        if c == ' ':
                            return (0, 1)
                        else:
                            return "Error: Expected ' ' after 'store'"
                    else:
                        return "Error: Expected 'e' after 'stor'"
                else:
                    return "Error: Expected 'r' after 'sto'"
            else:
                return "Error: Expected 't' after 'st'"
        else:
            return "Error: Expected 's' after 's'"
    
    # mult opcode
    elif c == 'm':
        c = next_char()
        if c == 'u':
            c = next_char()
            if c == 'l':
                c = next_char()
                if c == 't':
                    c = next_char()
                    if c == ' ':
                        return (2, 5)
                    else:
                        return "Error: Expected ' ' after 'mult'"
                else:
                    return "Error: Expected 't' after 'mul'"
            else:
                return "Error: Expected 'l' after 'mu'"
        else:
            return "Error: Expected 'u' after 'm'"
        
    # add opcode
    elif c == 'a':
        c = next_char()
        if c == 'd':
            c = next_char()
            if c == 'd':
                c = next_char()
                if c == ' ':
                    return (2, 3)
                else:
                    return "Error: Expected ' ' after 'add'"
            else:
                return "Error: Expected 'd' after 'ad'"
        else:
            return "Error: Expected 'd' after 'a'"
        
    # rshift opcode
    elif c == 'r':
        c = next_char()
        if c == 's':
            c = next_char()
            if c == 'h':
                c = next_char()
                if c == 'i':
                    c = next_char()
                    if c == 'f':
                        c = next_char()
                        if c == 't':
                            return (2, 7)
                        else:
                            return "Error: Expected 't' after 'rshi'"
                    else:
                        return "Error: Expected 'f' after 'rsh'"
                else:
                    return "Error: Expected 'i' after 'r'"
            else:
                return "Error: Expected 's' after 'r'"
        else:
            return "Error: Expected 's' after 'r'"

    # output opcode
    elif c == 'o':
        c = next_char()
        if c == 'u':
            c = next_char()
            if c == 't':
                c = next_char()
                if c == 'p':
                    c = next_char()
                    if c == 'u':
                        c = next_char()
                        if c == 't':
                            return (8, 3)
                        else:
                            return "Error: Expected 't' after 'outpu'"
                    else:
                        return "Error: Expected 'u' after 'outp'"
                else:
                    return "Error: Expected 'p' after 'out'"
            else:
                return "Error: Expected 't' after 'ou'"
        else:
            return "Error: Expected 'u' after 'o'"
    
    # handle new lines
    elif c == '\n' or c == '\r\n':
        return (10, 0)
    
    # handle comments
    elif c == '/':
        c = next_char()
        if c == '/':
            return None
        else:
            return "Error: Expected '/' after '/'"
        
    # handle constants
    if (c < '0' or c > '9'):
        return "Error: Expected a digit"
    else:
        n = 0
        while c >= '0' and c <= '9':
            t = int(c)
            c = next_char()
            n = n * 10 + t
        line_index -= 1
        return (5, n)
        
# handle error messages
# prints an error message based on given word
def opcode_whitespace_error(opcode: str):
    print("ERROR " + str(line_count) + ": " + "expected whitespace after opcode: " + opcode, file=sys.stderr)



