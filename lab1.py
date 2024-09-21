import sys
import output, parser

def print_help():
    print("""
        Valid command-line arguments:
        -h                : Show this help message.
        -s <name>         : prints tokens in token stream
        -p <name>         : invokes parser and reports on success or failure
        -r <name>         : prints human readable version of parser's IR
            """)

def main():
    argc = len(sys.argv)
    flag = sys.argv[1]

    if flag == '-h':
        print_help()
        return
    
    if argc == 2:
        flag = '-p'
        f_name = sys.argv[1]

    elif argc == 3:
        f_name = sys.argv[2]

    elif flag != '-s' and flag != '-p' and flag != '-r':
        print_help()
    
    if argc > 3:
        print('''ERROR: Multiple command line flags found.
              Try running with '-h' for help.''')
        f_name = sys.argv[argc-1]
    try:
        input_file = open(f_name,'r')
    except:
        print ("ERROR: Could not open file '"+f_name+"'. Exiting early.")
        exit(0)

    if flag == '-p':
        parser.parse(input_file, False)
        return

    elif flag == '-r':
        parser.parse(input_file, True)
        return

    elif flag == '-s': 
        output.print_tokens(input_file)

        return

if __name__ == "__main__":

    main()