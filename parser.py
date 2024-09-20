import scanner

def next_token(file):
    '''
    Returns the next token from the input file.
    '''
    line = scanner.scan_line(file)
    token = scanner.scan_word(line)
    return token