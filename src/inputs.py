import argparse
import sys
import pathlib

def setup_parser():
    """Sets up the argument parser and returns the parsed arguments
    
    Returns:
        args: The parsed arguments
    """
    parser = argparse.ArgumentParser()

    # CLI Input
    group = parser.add_mutually_exclusive_group() # Only one but not both

    group.add_argument("-fi", "--file-input", action="store_true", 
                        help="Translate text in the file", dest="fi")

    group.add_argument("-ci", "--console-input", action="store_true", 
                        help="Translates text given with the command", dest="ci")

    parser.add_argument("text") # The actual text to translate
    return parser.parse_args()

    # If filepath is given, so read file   

def get_input():
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
                return contents
        except PermissionError:
            raise FileNotFoundError(f"ERROR: {filepath} does not have read permissions, or is a directory")          

    # If the text given is actually what to translate or -ci is switched
    return args.text