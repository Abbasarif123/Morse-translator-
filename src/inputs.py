import argparse
import sys
import questionary
import os

def setup_parser():
    """Sets up the argument parser and returns the parsed arguments
    
    Returns:
        args: The parsed arguments
    """

    parser = argparse.ArgumentParser(
        epilog="If no arguments given, enters interactive mode."
    )


    parser.add_argument("text", nargs='?', help="The text to translate to morse or plain.") # The actual text to translate
    parser.add_argument("-i", "--interactive-mode", action="store_true")
    # Input group

    input_group = parser.add_mutually_exclusive_group() # Only one but not both

    input_group.add_argument("-fi", "--file-input", metavar="filepath", 
                        type=str, required=False, help="Translate text in the file")

    input_group.add_argument("-ci", "--console-input", action="store_true", 
                        help="Translates text given with the command")
    # Output group
    output_group = parser.add_mutually_exclusive_group()
    output_group.add_argument("-co", "--console-output", action="store_true", 
                        help="Displays translated morse code and plaintext within the console")

    output_group.add_argument("-so", "--screen-output", action="store_true", 
                        help="Displays translated morse code via a screen")

    parser.add_argument("-fo", "--file-output", metavar="filepath",
                        type=str, required=False, help="Output text and morse code into an existing .txt file")
    
    parser.add_argument("-ao", "--audio-ouput", action="store_true",
                        help="Sound out audio alongside screen or console output", dest="audio")

    return parser.parse_args()

    # If filepath is given, so read file   

def read_from_file(filepath:str) -> str:
    
    with open(filepath) as file:
        text = file.read().strip()
    return text

def file_exists(filepath:str) -> bool:
    return os.path.exists(filepath)

def interactive_mode() -> dict[str, str]:
    """Shows options and asks user to fill out options one by one
    Raises:
        FileNotFoundError: If input file isn't found
        ValueError: If user quits inbetween inputs"""
    options = { 'text': None, 
                'interactive_mode': True,
                'file_input': None,
                'console_output': False,
                'screen_output': False,
                'file_output': None,
                'audio': False}
    
    # *  INPUT CHOICE
    input_choice = questionary.select(
        "How do you want to input your text?",
        choices=["Console input", "File contents"]
    ).ask()
    
    if input_choice is None:
        raise ValueError("User did not enter input choice")

    # * INPUTS
    if input_choice == "File contents": # * IF FILE:

        options['file_input'] = questionary.path(
            "Whats the path to the file?"
        ).ask()


        if not file_exists(options['file_input']):
            raise FileNotFoundError(f"File {options['file_input']} not found")

    else: #* IF CONSOLE
        options['text'] = questionary.text(
            "Enter your text to translate:"
        ).ask()

        if options['text'] is None:
            raise ValueError("User did not input text")

    # * OUTPUTS
    output_choice = questionary.select(
        "How would you like your outputs?",
        choices=["Screen", "Console","File", "Screen+File", "Console+File"]
    ).ask()

    if output_choice is None:
        raise ValueError("User did not input output choice")

    options["console_output"] = "Console" in output_choice
    options["screen_output"] = "Screen" in output_choice

    if "File" in output_choice:
        options['file_output'] = questionary.path(
            "Which file to write to? (THIS WILL OVERWRITE THE FILE, BE CAREFUL)"
        ).ask()
        

    options['audio'] = questionary.confirm(
        "Would you like audio too?"
    ).ask()

    return options

def get_options() -> dict:
    """From the parsed arguments, gets the options for the program to run
    Returns:
        dict: options for the program. includes the text to translate
        
    Raises:
        FileNotFoundError: If file does not exist or permissions restrict access"""

    args = setup_parser()

    if len(sys.argv) == 1 or args.interactive_mode:
        options = interactive_mode()
        print("INTERACTIVE:", options)
    else:
        options = vars(args)
        print("ARGS:", options)


    if options['file_input'] and not os.access(options['file_input'], os.R_OK):
        raise FileNotFoundError(f"File: {options['file_input']} has insufficient read permissions")

    if options['file_input']:
        options[ 'text' ] = read_from_file(options['file_input'])

    if file_exists(options['file_output']) and not os.access(options['file_output'], os.W_OK):
        raise FileNotFoundError(f"File: {options['file_output']} has insufficient write permissions")

    return options

if __name__ == "__main__":
    get_options()