import sys
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
    '''
    Parses the input file.
    '''
    error = False
    k_operations = 0
    word = next_token(file)
    while word[0] != 9:
        if word[0] == 0:
            error = finish_memop(file)
            if error:
                print("here1")
                break
            k_operations += 1
        elif word[0] == 1:
            error = finish_loadi(file)
            if error:
                print("here2")
                break
            k_operations += 1
        elif word[0] == 2:
            error = finish_arithop(file)
            if error:
                print("here3")
                break
            k_operations += 1
        elif word[0] == 3:
            error = finish_output(file)
            if error:
                print("here4")
                break
            k_operations += 1
        elif word[0] == 4:
            error = finish_nop(file)
            if error:
                print("here5")
                break
            k_operations += 1
        elif word[0] == 10:
            word = next_token(file)
            continue
        else:
            print("ERROR")
        word = next_token(file)
    if error == False:
        print(f"Parse succeeded. Processed {k_operations} operations.")

def finish_memop(file):
    '''
    Finish parsing a MEMOP.
    return True if there is an error, False otherwise
    '''
    word = next_token(file)
    if word[0] != 6:
        print(f"Missing first source register in {opcodes[word[1]]}", file = sys.stderr)
        return True
    else:
        word = next_token(file)
        if word[0] != 8:
            return True
        else:
            word = next_token(file)
            if word[0] != 6:
                return True
            else:
                word = next_token(file)
                if word[0] == 10:
                    return False
                else:
                    print("Error")

def finish_loadi(file):
    '''
    Finish parsing a LOADI.
    '''
    word = next_token(file)
    if word[0] != 5:
        return True
    else:
        word = next_token(file)
        if word[0] != 8:
            return True
        else:
            word = next_token(file)
            if word[0] != 6:
                return True
            else:
                word = next_token(file)
                if word[0] == 10:
                    return False
                else:
                    return True

def finish_arithop(file):
    '''
    Finish parsing an ARITHOP.
    '''
    word = next_token(file)
    error = False
    if word[0] != 6:
        error = True
    else:
        word = next_token(file)
        if word[0] != 7:
            return True
        else:
            word = next_token(file)
            if word[0] != 6:
                print("ERROR")
                return True
            else:
                word = next_token(file)
                if word[0] != 8:
                    print("ERROR")
                    return True
                else:
                    word = next_token(file)
                    if word[0] != 6:
                        print("ERROR")
                        return True
                    else:
                        word = next_token(file)
                        if word[0] == 10:
                            print("done")
                            return False
                        else:
                            print("Error")
                            return True

def finish_output(file):
    '''
    Finish parsing an OUTPUT.
    '''
    word = next_token(file)
    if word[0] != 5:
        print("ERROR")
        return True
    else:
        word = next_token(file)
        if word[0] == 10:
            return False
        else:
            print("Error")
            return True


def finish_nop(file):
    '''
    Finish parsing a NOP.
    '''
    word = next_token(file)
    if word[0] == 10:
        return False
    else:
        print("Error")
        return True

            