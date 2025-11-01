from colorama import Cursor, Style, Fore, init
import sys
import time

init()

#* NOTE: ANSI ESCAPE CODES:
#* Starts from \x1b, tells the console to do other things than output text
#* For example: \x1b[3A moves up 3 lines 

def clear_line():
    """Clears the line wherever the cursor is on the terminal"""
    sys.stdout.write("\x1b[2K") 

def highlighted(to_highlight:str) -> str:
    """Highlights the text to display via colorama"""
    return Fore.BLUE + to_highlight + Style.RESET_ALL

def write_to_console(morse:list[str], plain:str):

    print("\n") # To retain the console command line

    completed_morse = ""
    completed_plain = ""
    sys.stdout.write("\033[?25l") # hide cursor
    sys.stdout.flush()

    for mchar, pchar in zip(morse, plain):

        this_morse = ""
        for dees in mchar:
            this_morse += dees

            if dees == '.':
                delay = 0.12 # Got delay timings via experimentation
            else:
                delay = 0.36


            # move to Morse line
            sys.stdout.write(Cursor.UP(2))  # go up 2 lines
            clear_line()
            sys.stdout.write(completed_morse + highlighted(this_morse)  + "\n")

            # plain text line
            clear_line()
            sys.stdout.write(completed_plain + highlighted(pchar) + "\n")
            sys.stdout.flush()

            time.sleep(delay) 

        completed_plain += pchar
        completed_morse += this_morse
    
    sys.stdout.write("\033[?25h") # show cursor
    sys.stdout.flush()