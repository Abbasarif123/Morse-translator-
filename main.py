from src.inputs import *
from src.outputs import *
from src.translator import translate

# ! SPACE BETWEEN CHARACTERS
# ! SLASH BETWEEN WORDS
# TODO: ADDD METAVAR TO FI

def polish_morse(morse:str) -> list[list[str]]:
    morse_words = morse.split("/")
    morse_letters = [word.strip().split() for word in morse_words]

    return morse_letters

# def translate(blind:str):

#     return [["....", ".", ".-..", ".-..", "---"], [".--", "---", ".-.", ".-..", "-.."]], "Hello World"

def write_to_file(file_path:str, morse:str, plain:str):
    raise NotImplementedError

def main():

    options = get_options()

    blind_text = options['text']
    morse, plain = translate(blind_text) 
    morse = polish_morse(morse)

    if options["screen_output"]:
        screen_output(morse, plain, options["audio"])
    else:
        console_output(morse, plain, options["audio"])
    
    if options["file_output"]:
        write_to_file(options["file_output"], "---", plain)

if __name__ == "__main__":
    main()