from src.inputs import *
from src.outputs import *

# ! SPACE BETWEEN CHARACTERS
# ! SLASH BETWEEN WORDS

def translate(blind:str):
    return [["....", ".", ".-..", ".-..", "---"], [".--", "---", ".-.", ".-..", "-.."]],"Hello World"

def write_to_file(options["file_output"], morse, plain):
    raise NotImplementedError

def main():
    options = get_options()
    print(options)


    # TODO: Add translation functions here
    # *: Morse code data should be list of morse code strings. 
    # Every item in the list would be mapped to each character in the string
    # TODO: Add file output
    # print(text)
    
    blind_text = options['text']
    morse, plain = translate(blind_text) 


    if options["screen_output"]:
        screen_output(morse, plain, options["audio"])
    elif options["console_output"]:
        console_output(morse, plain, options["audio"])
    
    if options["file_output"]:
        write_to_file(options["file_output"], morse, plain)
    # console_output(morse, plain)
    # if options[ "screen_output" ]:
    #     screen_output(morse, plain, options["audio"])
    # elif options["console_output"]:
    #     console_output(morse, plain, options["audio"])

if __name__ == "__main__":
    main()