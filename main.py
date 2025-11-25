from src.inputs import *
from src.outputs import *
from src.translator import translate, polish_morse
import sys

# ! SPACE BETWEEN CHARACTERS
# ! SLASH BETWEEN WORDS


# def translate(blind:str):

#     return [["....", ".", ".-..", ".-..", "---"], [".--", "---", ".-.", ".-..", "-.."]], "Hello World"


def main():

    try:
        options = get_options()
    except (ValueError, FileNotFoundError) as e:
        sys.exit("ERROR:" + str(e))

    blind_text = options['text']
    try:
        morse, plain = translate(blind_text) 
    except ValueError as e:
        sys.exit("ERROR:" + str(e))


    
    listed_morse = polish_morse(morse)

    if options["file_output"]:
        file_output(options["file_output"], morse, plain)

    if options["screen_output"]:
        screen_output(listed_morse, options["audio"])
    elif options["console_output"]:
        console_output(listed_morse, plain, options["audio"])
    elif options["text_to_speech"]:
        tts_output(plain)

if __name__ == "__main__":
    main()