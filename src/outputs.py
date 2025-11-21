from colorama import Cursor, Style, Fore, init, Back
import sys
import os 
import pyttsx3
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1" # Hides the "Hello from pygame" text

import pygame
import time

init()

engine = pyttsx3.init()

engine.setProperty("rate", 200)
engine.setProperty("volume", 0.9)

def tts_output(plain):
    engine = pyttsx3.init()
    engine.say(plain)
    engine.runAndWait()



def ensure_mixer():
    if not pygame.mixer.get_init():
        pygame.mixer.init()

ensure_mixer()
dot_sound = pygame.mixer.Sound("assets/dot.wav")
dash_sound = pygame.mixer.Sound("assets/dash.wav")

#* NOTE: ANSI ESCAPE CODES:
#* Starts from \x1b, tells the console to do other things than output text
#* For example: \x1b[3A moves up 3 lines 

def clear_line():
    """Clears the line wherever the cursor is on the terminal"""
    sys.stdout.write("\x1b[2K") 

def highlighted(to_highlight:str) -> str:
    """Highlights the text to display via colorama"""
    return Fore.BLUE + Style.BRIGHT + Back.YELLOW + to_highlight + Style.RESET_ALL

def console_output(morse:list[list[str]], plain:str, audio:bool=False):
    global dot_sound, dash_sound

    if audio:
        ensure_mixer() # I genuinly dont know please

    def morse_and_plain(morse:str, plain:str):

            sys.stdout.write(Cursor.UP(2))  # go up 2 lines
            # move to Morse line
            clear_line()
            sys.stdout.write(morse + "\n")

            # plain text line
            clear_line()
            sys.stdout.write(plain + "\n")
            sys.stdout.flush()

    print("\n") # Basically to make space for the output to be on multiple lines

    completed_morse = ""
    completed_plain = ""

    sys.stdout.write("\033[?25l") # hide cursor
    sys.stdout.flush()

    for m_word, p_word in zip(morse, plain.split()):
        for mchar, pchar in zip(m_word, p_word):

            this_morse = ""
            for dees in mchar:
                this_morse += dees

                if dees == '.':
                    delay = dot_sound.get_length() #0.12 # Got delay timings via experimentation
                    dot_sound.play() if audio else None
                else:
                    delay = dash_sound.get_length()
                    dash_sound.play() if audio else None


                # move to Morse line

                morse_and_plain(completed_morse + highlighted(this_morse),
                                completed_plain + highlighted(pchar))            

                time.sleep(delay + 0.3) 

            completed_plain += pchar
            completed_morse += this_morse
        
        # Space in between words
        completed_morse += " / " 
        completed_plain += " "

    # When finished, it should show the whole strings without any highlighting
    morse_and_plain(completed_morse, completed_plain)
    
    sys.stdout.write("\033[?25h") # show cursor 
    sys.stdout.flush()

def screen_output(morse:list[list[str]], plain:str, audio:bool=False):
    
    # Initialize pygame cycle Create screen
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Screen output")

    def fill(color:tuple[int, int, int]):
        screen.fill(color)
        pygame.display.flip() # updates window

    # Colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    fill(WHITE) # Initially white

    def flash(delay:float|int):
        fill(BLACK)
        time.sleep(delay)
        fill(WHITE)

    if audio:
        ensure_mixer() # bugs if this isn't included

    for mword in morse:
        for mcode in mword:
            for dees in mcode:
                if dees == '.':
                    delay = dot_sound.get_length() #0.12 # Got delay timings via experimentation
                    dot_sound.play() if audio else None
                else:
                    delay = dash_sound.get_length()
                    dash_sound.play() if audio else None

                flash(delay)
            time.sleep(0.5)               


    pygame.quit()

if __name__ == "__main__":
    # print(pygame.mixer.get_init())
    #* FOR TESTING
    pass
