from src.inputs import *
from src.outputs import *
import sys

def main():
    options = vars(setup_parser())

    if len(sys.argv) == 1 or options["interactive_mode"]:
        interactive_mode()
    # interactive_mode()
    # TODO: Add translation functions here
    # *: Morse code data should be list of morse code strings. 
    # Every item in the list would be mapped to each character in the string
    # TODO: Add file output
    # print(text)
    
    morse = [["....", ".", ".-..", ".-..", "---"], [".--", "---", ".-.", ".-..", "-.."]]
    plain = "Hello World"

    # console_output(morse, plain)
    if options[ "screen_output" ]:
        screen_output(morse, plain, options["audio"])
    elif options["console_output"]:
        console_output(morse, plain, options["audio"])

if __name__ == "__main__":
    main()