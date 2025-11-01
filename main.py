from src.inputs import get_input
from src.outputs import write_to_console
# import simpleaudio as sa

# dot_sound = sa.WaveObject.from_wave_file("assets/dot.wav")
# dash_sound = sa.WaveObject.from_wave_file("assets/dash.wav")

# def play_dot():
#     dot_sound.play()

# def play_dash():
#     dash_sound.play()

def main():
    # text = get_input()
    # TODO: Add translation functions here
    # *: Morse code data should be list of morse code strings. 
    # Every item in the list would be mapped to each character in the string
    # TODO: Add file output + pretty CLI output
    # print(text)
    
    morse = ["....", ".", ".-..", ".-..", "---", ".......", ".--", "---", ".-.", ".-..", "-.."]
    plain = "Hello World"

    write_to_console(morse, plain)


if __name__ == "__main__":
    main()