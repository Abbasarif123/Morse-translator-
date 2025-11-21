from translator import morsetotext,texttomorse
from morsedictionary import morsedictionary,textdictionary
from morseplayer import playmorsesound
from textplayer import playtextspeech
import pyttsx3

def main():
    print("PYTHON MORSE CODE TRANSLATOR")
    while True:
        print("Options:")
        print("1. Translate Text to Morse Code")
        print("2. Translate Morse Code to Text")
        print("3. Exit")

        option = input().strip()
        match option:
            case "1":
                print("enter text input:")
                textinput = input().strip()
                result = texttomorse(textinput)
                print(result)
                print("Do you want to play this as a sound \U0001F3B5?: Y for yes, N for no")
                soundinput = input()
                match soundinput:
                    case 'Y':
                        playmorsesound(result)
                    case 'N':
                        print("Gotcha \U0001f44d")
            case "2":
                print("enter morse input:")
                morseinput = input().strip()
                textresult = morsetotext(morseinput)
                print(textresult)
                print("Do you want to play this as a sound \U0001F3B5?: Y for yes, N for no")
                textchoice = input()
                match textchoice:
                    case 'Y':
                        playtextspeech(textresult)
                    case 'N':
                        print("Gotcha \U0001f44d")

            case "3":
                print("THANK YOU FOR USING THIS TOOL \U0001F44B")
                break
            case _:
                print("ENTER VALID INPUT \U0001F620")


main()