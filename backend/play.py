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

# load the MIDI file into a multitrack object
multitrack = read(latest_midi)

# convert the multitrack MIDI to PrettyMIDI format
pm = to_pretty_midi(multitrack)

# create a new PrettyMIDI object to store processed notes
new_pm = pretty_midi.PrettyMIDI()

# define legato overlap duration
legato_overlap = 0.02  # Small overlap for smooth transitions
