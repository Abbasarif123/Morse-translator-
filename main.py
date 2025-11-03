from src.inputs import get_input
from src.outputs import write_to_console

def main():
    # text = get_input()
    # TODO: Add translation functions here
    # *: Morse code data should be list of morse code strings. 
    # Every item in the list would be mapped to each character in the string
    # TODO: Add file output
    # print(text)
    
    morse = ["....", ".", ".-..", ".-..", "---", ".......", ".--", "---", ".-.", ".-..", "-.."]
    plain = "Hello World"

    write_to_console(morse, plain)


if __name__ == "__main__":
    main()