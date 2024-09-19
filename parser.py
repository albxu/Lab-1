import scanner
def parse(file):
    line = scanner.scan_line(file)
    while scanner.EOF == False:
        token = scanner.scan_word(line)
        print("Line " + str(scanner.line_count) + ": " + str(token))
        if token[0] == 10:
            scanner.line_count += 1
            scanner.line_index = 0
            line = scanner.scan_line(file)