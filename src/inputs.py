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

    input_group.add_argument("-fi", "--file-input", action="store_true", 
                        help="Translate text in the file")

    input_group.add_argument("-ci", "--console-input", action="store_true", 
                        help="Translates text given with the command")
    # Output group
    output_group = parser.add_mutually_exclusive_group()
    output_group.add_argument("-co", "--console-output", action="store_true", 
                        help="Displays translated morse code and plaintext within the console")

    output_group.add_argument("-so", "--screen-output", action="store_true", 
                        help="Displays translated morse code via a screen")

    parser.add_argument("-fo", "--file-output", metavar="filepath",
                        type=str, required=False)
    
    parser.add_argument("-ao", "--audio-ouput", action="store_true",
                        help="Sound out audio alongside screen or console output", dest="audio")

    return parser.parse_args()

    # If filepath is given, so read file   
# ! REFERENCE: {'text': 'yadaydya', 'interactive_mode': False, 'file_input': True, 'console_input': False, 'console_output': False, 'screen_output': False, 'audio': False}

def read_from_file(filepath:str) -> str:
    with open(filepath) as file:
        text = file.read().strip()
    return text

def interactive_mode() -> dict[str, str]:
    options = { 'text': None, 
                'interactive_mode': False,
                'file_input': False,
                "file_input_path": None,
                'console_output': False,
                'screen_output': False,
                'file_output': None,
                'audio': False}
    
    # *  INPUT CHOICE
    input_choice = questionary.select(
        "How do you want to input your text?",
        choices=["Console input", "File contents"]
    ).ask()
    
    # * INPUTS
    if input_choice == "File contents": # * IF FILE:
        options["file_input"] = True
    

        file_path = questionary.path(
            "Whats the path to the file?"
        ).ask()

        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File {file_path} not found")

        options['file_input_path'] = file_path   
        options['text'] = read_from_file(file_path)
    else: #* IF CONSOLE
        options['text'] = questionary.text(
            "Enter your text to translate:"
        ).ask()

    # * OUTPUTS
    output_choice = questionary.select(
        "How would you like your outputs?",
        choices=["Screen", "Console","File", "Screen+File", "Console+File"]
    ).ask()

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

#! REWORK THIS:
def get_options() -> dict[str, str|bool]:
    """From the parsed arguments, gets the options for the program to run
    Returns:
        dict: options for the program. includes the text to translate
        
    Raises:
        FileNotFoundError: If file does not exist or permissions restrict access"""
    args = setup_parser()
    if len(sys.argv) == 1 or args.i:
        options = interactive_mode()

    return {}

if __name__ == "__main__":
    args = setup_parser()
    print(vars(args))