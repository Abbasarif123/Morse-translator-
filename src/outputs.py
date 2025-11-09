from colorama import Cursor, Style, Fore, init, Back
import sys
import os 
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1" # Hides the "Hello from pygame" text

import pygame
import time

init()

#* NOTE: ANSI ESCAPE CODES:
#* Starts from \x1b, tells the console to do other things than output text
#* For example: \x1b[3A moves up 3 lines 

def ensure_mixer():
    if not pygame.mixer.get_init():
        pygame.mixer.init()

ensure_mixer()
dot_sound = pygame.mixer.Sound("assets/dot.wav")
dash_sound = pygame.mixer.Sound("assets/dash.wav")

def clear_line():
    """Clears the line wherever the cursor is on the terminal"""
    sys.stdout.write("\x1b[2K") 

def highlighted(to_highlight:str) -> str:
    """Highlights the text to display via colorama"""
    return Fore.BLUE + Style.BRIGHT + Back.YELLOW + to_highlight + Style.RESET_ALL

def console_output(morse:list[str], plain:str, audio:bool=False):
    global dot_sound, dash_sound

    if audio:
        ensure_mixer() # I genuinly dont know please

    def morse_and_plain(morse:str, plain:str):
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

    for mchar, pchar in zip(morse, plain):

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
            sys.stdout.write(Cursor.UP(2))  # go up 2 lines

            morse_and_plain(completed_morse + highlighted(this_morse),
                            completed_plain + highlighted(pchar))            

            time.sleep(delay + 0.3) 

        completed_plain += pchar
        completed_morse += this_morse

        # When finished, it should show the whole strings without any highlighting
        sys.stdout.write(Cursor.UP(2))  # go up 2 lines
        morse_and_plain(completed_morse, completed_plain)
    
    sys.stdout.write("\033[?25h") # show cursor (not really needed i guess)
    sys.stdout.flush()

def screen_output():#morse:list[str], plain:str, audio:bool=False):
    # Create screen
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Demo")

    # Colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    def fill(color:tuple[int, int, int]):
        screen.fill(color)
        pygame.display.flip() # updates window

    fill(BLACK)
    time.sleep(2)
    fill(WHITE)
    time.sleep(2)

if __name__ == "__main__":
    # print(pygame.mixer.get_init())
    #* FOR TESTING
    pygame.init()
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False 
    
        screen_output()