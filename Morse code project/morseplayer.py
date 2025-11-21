
import time
import pygame
import numpy as np


frequency = 750
samplerate = 44100
pygame.mixer.init(frequency=samplerate, size=-16, channels=1,buffer=512)

#everything in sound declaration here is in miliseconds
dot_sound_duration = 100
dash_sound_duration = 4*dot_sound_duration
morsedotdash_pause_duration = dot_sound_duration
intermorseletter_duration = dash_sound_duration
intermorseword_duration = 8*dot_sound_duration

def createsound(frequency, duration_miliseconds): #setting up the sounds themselves here
    duration_seconds = duration_miliseconds/1000.0
    number_of_samples = int(samplerate*duration_seconds)
    timeaxis = np.linspace(0, duration_seconds, number_of_samples, endpoint=False)
    wave = np.sin(2*np.pi*frequency*timeaxis)
    wave = (wave * 32767).astype(np.int16)

    #duplicating my mono wave since it expects a stereo wave
    if pygame.mixer.get_init()[2] == 2:
        wave = np.column_stack((wave, wave))
    #######


    sound = pygame.sndarray.make_sound(wave)
    return sound

dotsound = createsound(frequency,dot_sound_duration)
dashsound = createsound(frequency,dash_sound_duration)

def playmorsesound(morsecode):
    print("Playing your morse code \U0001F3B6 \U0001f4bf \U0001F3B6")
    for element in morsecode:
        match element:
            case '.':
                dotsound.play()
                pygame.time.wait(dot_sound_duration+morsedotdash_pause_duration)
            case '-':
                dashsound.play()
                pygame.time.wait(dash_sound_duration+morsedotdash_pause_duration)
            case ' ':
                pygame.time.wait(intermorseletter_duration-morsedotdash_pause_duration)
            case '/':
                pygame.time.wait(intermorseword_duration-intermorseletter_duration)

