import pygame
from music21 import converter, note, chord
import numpy as np

# Initialize pygame mixer
freq = 44100  # Audio CD quality
bitsize = -16  # Unsigned 16 bit
channels = 2  # Stereo
buffer = 1024  # Number of samples
pygame.mixer.init(freq, bitsize, channels, buffer)

def play_music(midi_filename):
    """Stream MIDI file in a blocking manner."""
    clock = pygame.time.Clock()
    pygame.mixer.music.load(midi_filename)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        clock.tick(30)

if __name__ == "__main__":
    midi_filename = "piano_right.mid"

    try:
        play_music(midi_filename)
    except KeyboardInterrupt:
        pygame.mixer.music.fadeout(1000)
        pygame.mixer.music.stop()
        raise SystemExit