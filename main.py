from src.inputs import *
from src.outputs import console_output

def main():
    options = setup_parser()
    print(vars(options))
    # interactive_mode()
    # TODO: Add translation functions here
    # *: Morse code data should be list of morse code strings. 
    # Every item in the list would be mapped to each character in the string
    # TODO: Add file output
    # print(text)
    
    morse = ["....", ".", ".-..", ".-..", "---", ".......", ".--", "---", ".-.", ".-..", "-.."]
    plain = "Hello World"

    # console_output(morse, plain)


if __name__ == "__main__":
    main()