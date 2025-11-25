from colorama import Cursor, Style, Fore, init, Back
import sys
import os 
import pyttsx3
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1" # Hides the "Hello from pygame" text

import pygame
import time

from src.morseplayer import playmorsesound

init()

def tts_output(plain:str):
    """Sounds out plaintext in text-to-speech
    Args:
        plain (str): string to say in tts
    """

    engine = pyttsx3.init()

    engine.setProperty("rate", 200)
    engine.setProperty("volume", 0.9)
    engine = pyttsx3.init()

    print(Style.BRIGHT + "OUTPUTTING IN TTS:" + Style.RESET_ALL)
    print(highlighted(plain))

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

def highlighted(to_highlight:str) -> str:
    """Highlights the text to display via colorama"""
    return Fore.BLUE + Style.BRIGHT + Back.YELLOW + to_highlight + Style.RESET_ALL


def console_output(morse:list[list[str]], plain:str, audio:bool=False):
    """Outputs the morse code and plaintext string side by side, one at a time, on the console
    Args:
        morse (list[list[str]]): Morse code equivalent of plain. Every word in plain is mapped as a list of str
        plain (str): plaintext equivalent of morse
        audio (bool): For audio output alongside console output
    """

    def clear_line():
        """Clears the line wherever the cursor is on the terminal"""
        sys.stdout.write("\x1b[2K") 

    def morse_and_plain(morse:str, plain:str):
            """Helper function for outputing morse and plain alongisde each other"""

            sys.stdout.write(Cursor.UP(2))  # go up 2 lines
            # move to Morse line
            clear_line()
            sys.stdout.write(morse + "\n")

            # plain text line
            clear_line()
            sys.stdout.write(plain + "\n")
            sys.stdout.flush()
    
    global dot_sound, dash_sound

    BONUS_DELAY = 0.1
    if audio:
        ensure_mixer() # I genuinly dont know please


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
                    delay = dot_sound.get_length() 
                    dot_sound.play() if audio else None
                else:
                    delay = dash_sound.get_length()
                    dash_sound.play() if audio else None

                #! playmorsesound(dees) if audio else None


                # move to Morse line

                morse_and_plain(completed_morse + highlighted(this_morse),
                                completed_plain + highlighted(pchar))            

                time.sleep(delay + BONUS_DELAY) 

            completed_plain += pchar
            completed_morse += this_morse + " "
        
        # Space in between words
        completed_morse += " / " 
        completed_plain += " "

    # When finished, it should show the whole strings without any highlighting
    morse_and_plain(completed_morse, completed_plain)
    
    sys.stdout.write("\033[?25h") # show cursor 
    sys.stdout.flush()

def screen_output(morse:list[list[str]], audio:bool=False):
    """Outputs morse code by flashing it onto a screen
    Args:
        morse (list[list[str]]): Morse code. Every equivalent word is a list of equivalent character
            (i.e. dots and dashes)
        audio (bool): Sounds out beeps if True
    """
    
    # Create screen
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Screen output")


    clock = pygame.time.Clock()
    def wait_nonblocking(ms):
        """Nonblocking wait that keeps window responsive.
        Args:
            ms (int): Duration to wait for in milliseconds
        """

        # * I can't use waiting events like time.sleep or pygame.time.wait cuz those 
        # * completely block the screen, so I have to keep track of time and delay manually 

        start = pygame.time.get_ticks()

        while pygame.time.get_ticks() - start < ms:

            for event in pygame.event.get(): # * This keeps pygame from freezing, as it fetches all pending events 
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return False
                
            clock.tick(144) # * usually controls framerate, but used for not using more CPU time than needed

        return True 

    def fill(color:tuple[int, int, int]):
        screen.fill(color)
        pygame.display.flip() # updates window

    # Colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    FLASH_GAP_MS = 500

    fill(BLACK) # Initially black 

    def flash(delay_ms:int):
        """flashes the screen white for delay milliseconds"""
        fill(WHITE)
        if not wait_nonblocking(delay_ms):
            raise ValueError("User quit") 
        
        fill(BLACK)
        if not wait_nonblocking(FLASH_GAP_MS):
            raise ValueError("User quit") 

    if audio:
        ensure_mixer() # bugs if this isn't included


    for mword in morse:
        for mcode in mword:

            for dees in mcode:

                pygame.event.pump() # Keeps the game loop resposive, so the screen doesn't completely freeze

                if dees == '.':
                    delay = dot_sound.get_length() 
                    dot_sound.play() if audio else None
                else:
                    delay = dash_sound.get_length()
                    dash_sound.play() if audio else None


                delay_ms = int(delay * 1000)

                flash(delay_ms)



    pygame.quit()

def file_output(file_path:str, morse:str, plain:str):

    with open(file_path, 'w') as file:
        file.write(f"MORSE: {morse}\nPLAIN: {plain}") 

if __name__ == "__main__":
    # print(pygame.mixer.get_init())
    #* FOR TESTING
    file_output("test_output.txt", "skibidi", "ohio")
