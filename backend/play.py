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

# process each instrument in the MIDI file
for instrument in pm.instruments:
    new_instrument = pretty_midi.Instrument(program=instrument.program)

    # sort notes by start time
    instrument.notes.sort(key=lambda note: note.start)

    i = 0  # note index

    while i < len(instrument.notes):
        chord_notes = []
        current_note = instrument.notes[i]

        # detect chords (group notes that start at the same time)
        while i < len(instrument.notes) and np.isclose(instrument.notes[i].start, current_note.start, atol=0.001):
            chord_notes.append(instrument.notes[i])
            i += 1

        # find when the next note or chord starts
        next_start_time = instrument.notes[i].start if i < len(instrument.notes) else None

        # apply legato while preserving full note length
        for note in chord_notes:
            new_start = max(0, note.start)  # keep original start time

            if next_start_time:
                new_end = next_start_time - legato_overlap  # allow a small overlap
                new_end = max(new_start + 0.2, new_end)  # ensure minimum length of 200ms
            else:
                new_end = note.end  # keep original end time for last note

            # make sure chords sustain fully until the next event
            if len(chord_notes) > 1:
                new_end = max(new_end, note.end)

            # shift notes up one octave if needed (recommended if using 8-bit soundfont)
            new_pitch = note.pitch + 12 if note.pitch + 12 <= 127 else 127  # Ensure max MIDI pitch value is not exceeded

            # Store the new adjusted note
            new_note = pretty_midi.Note(
                velocity=note.velocity,
                pitch=new_pitch, # or note.pitch for original pitch
                start=new_start,
                end=new_end
            )
            new_instrument.notes.append(new_note)

    new_pm.instruments.append(new_instrument)

# Now `new_pm` contains the **legato-processed MIDI** without notes cutting off too early.

# create another pretty_midi object for additional effects
processed_pm = pretty_midi.PrettyMIDI()
for instrument in new_pm.instruments:
    processed_instrument = pretty_midi.Instrument(program=instrument.program)
    
    # sort notes by start time again
    instrument.notes.sort(key=lambda note: note.start)

    last_start_time = -1
    chord_notes = []

    for note in instrument.notes:
        new_velocity = 20  # set all notes to a soft velocity (ppp)

        # introduce slight timing variation (-10ms to +10ms) for a more human feel
        time_variation = np.random.uniform(-0.01, 0.01)
        new_start = max(0, note.start + time_variation)
        new_end = max(new_start + 0.05, note.end + time_variation)

        # slightly delay notes in long chords (chords lasting ≥1 second) to create an arpeggio effect
        if chord_notes and all(n.end - n.start >= 1.0 for n in chord_notes):
            for j, chord_note in enumerate(chord_notes):
                time_offset = j * np.random.uniform(0.02, 0.04)  # add small delays between notes
                chord_note.start += time_offset
                chord_note.end = max(chord_note.start + 0.05, chord_note.end + time_offset)

        # create the new processed note
        new_note = pretty_midi.Note(
            velocity=20,  # keep dynamics soft, 0 for softest and 127 for hardest
            pitch=note.pitch,
            start=new_start,
            end=new_end
        )
        processed_instrument.notes.append(new_note)

    processed_pm.instruments.append(processed_instrument)
