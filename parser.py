import scanner

opcodes = ["load", "store", "loadI", "add", "sub", "mult", "lshift", "rshift", "output", "nop"]
grammar = ["MEMOP", "LOADI", "ARITHOP", "OUTPUT", "NOP", "CONSTANT", "REGISTER", "COMMA", "INTO", "ENDFILE", "NEWLINE"]
line = ""

def next_token(file):
    '''
    Returns the next token from the input file.
    '''
    global line
    if line == "" or scanner.next_line == True:
        scanner.line_count += 1
        scanner.line_index = 0
        scanner.next_line = False
        line = scanner.scan_line(file)
    
    if scanner.eof == True:
        return (9, "")
    
    token = scanner.scan_word(line)
    
    return token
    
def parse(file):
    word = next_token(file)
    while word[0] != 9:
        if word[0] == 0:
            finish_memop(file)
        elif word[0] == 1:
            finish_loadi(file)
        elif word[0] == 2:
            finish_arithop(file)
        elif word[0] == 3:
            finish_output(file)
        elif word[0] == 4:
            finish_nop(file)
        else:
            print("ERROR")
        word = next_token(file)

def finish_memop(file):
    '''
    Finish parsing a MEMOP.
    '''
    word = next_token(file)
    if word[0] != 6:
        print("ERROR")
    else:
        word = next_token(file)
        if word[0] != 8:
            print("ERROR")
        else:
            word = next_token(file)
            if word[0] != 6:
                print("ERROR")
            else:
                word = next_token(file)
                if word[0] == 10:
                    print("done")
                else:
                    print("Error")

def finish_loadi(file):
    '''
    Finish parsing a LOADI.
    '''
    word = next_token(file)
    if word[0] != 5:
        print("ERROR")
    else:
        word = next_token(file)
        if word[0] != 8:
            print("ERROR")
        else:
            word = next_token(file)
            if word[0] != 6:
                print("ERROR")
            else:
                word = next_token(file)
                if word[0] == 10:
                    print("done")
                else:
                    print("Error")

def finish_arithop(file):
    '''
    Finish parsing an ARITHOP.
    '''
    word = next_token(file)
    if word[0] != 6:
        print("ERROR")
    else:
        word = next_token(file)
        if word[0] != 7:
            print("ERROR")
        else:
            word = next_token(file)
            if word[0] != 6:
                print("ERROR")
            else:
                word = next_token(file)
                if word[0] != 8:
                    print("ERROR")
                else:
                    word = next_token(file)
                    if word[0] != 6:
                        print("ERROR")
                    else:
                        word = next_token(file)
                        if word[0] == 10:
                            print("done")
                        else:
                            print("Error")

def finish_output(file):
    '''
    Finish parsing an OUTPUT.
    '''
    word = next_token(file)
    if word[0] != 5:
        print("ERROR")
    else:
        word = next_token(file)
        if word[0] == 10:
            print("done")
        else:
            print("Error")


def finish_nop(file):
    '''
    Finish parsing a NOP.
    '''
    word = next_token(file)
    if word[0] == 10:
        print("done")
    else:
        print("Error")

            