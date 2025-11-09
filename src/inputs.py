import argparse
import questionary
import pathlib

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
    output_group.add_argument("-co", "--console-outut", action="store_true", 
                        help="Displays translated morse code and plaintext within the console")

    output_group.add_argument("-so", "--screen-outut", action="store_true", 
                        help="Displays translated morse code via a screen")

    parser.add_argument("-ao", "--audio-ouput", action="store_true",
                        help="Sound out audio alongside screen or console output", dest="audio")

    return parser.parse_args()

    # If filepath is given, so read file   

def interactive_mode():
    input_choice = questionary.select(
        "How do you want to input your text?",
        choices=["Console input", "File contents"]
    ).ask()


def get_options() -> tuple[str, dict]:
    """From the parsed arguments, gets the text to translate
    
    Returns:
        str: text to translate
        
    Raises:
        FileNotFoundError: If file does not exist or permissions restrict access"""
    args = setup_parser()

    if args.fi:
        filepath = pathlib.Path(args.text)

        if not filepath.exists():
            raise FileNotFoundError(f"ERROR: {filepath} does not exist")          


        try:
            with open(filepath) as file:
                contents = file.read()
                contents = contents.strip()
                return contents, {}
        except PermissionError:
            raise FileNotFoundError(f"ERROR: {filepath} does not have read permissions, or is a directory")          

    # If the text given is actually what to translate or -ci is switched
    return args.text