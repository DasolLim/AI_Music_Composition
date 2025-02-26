import os
from pypianoroll import read, to_pretty_midi
from pydub import AudioSegment, playback
import soundfile as sf
import numpy as np
import pretty_midi

# define sample rate for better audio quality
sample_rate = 44100

# find the most recent MIDI file in the directory
midi_files = [f for f in os.listdir() if f.endswith(".mid")]
if not midi_files:
    raise FileNotFoundError("No MIDI files found in the directory.")

# get the most recently created/modified MIDI file
latest_midi = max(midi_files, key=os.path.getctime)
original_file_name = os.path.splitext(latest_midi)[0]  # Remove .mid extension

print(f"Processing most recent MIDI file: {latest_midi}")
