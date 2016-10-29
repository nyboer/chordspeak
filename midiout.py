
#!/usr/bin/env python
"""
Send random notes to the output port.
"""

import sys
import time
import random
import mido
from mido import Message

if len(sys.argv) > 1:
    portname = sys.argv[1]
else:
    # portname = 'Base2 MIDI 1'  # Use default port
    portname = 'MicroBrute MIDI 1'

chords = {
    'pitch':[0],
    'augmented':[0,4,8],
    'major':[0,4,7],
    'minor':[0,3,7],
    'diminished':[0,3,6],
    'major seventh':[0,4,7,11], # major, major seventh
    'dominant seventh':[0,4,7,10], #major, minor seventh
    'minor seventh':[0,3,7,10], #minor, minor seventh
    'half diminished seventh':[0,3,6,10], #diminished(flat 3,flat 5), minor seventh
    'diminished seventh':[0,3,6,9], #Diminished, diminished seventh
       }

note_names = {
    'b sharp': 0,
    'c': 0,
    'c sharp': 1,
    'd flat': 1,
    'd': 2,
    'd sharp': 3,
    'e flat': 3,
    'e': 4,
    'e sharp': 5,
    'f flat': 4,
    'f': 5,
    'f sharp': 6,
    'g flat': 6,
    'g': 7,
    'g sharp': 8,
    'a flat': 8,
    'a': 9,
    'a sharp': 10,
    'b flat': 10,
    'b': 11,
    'c flat': 11,
}


class Chord(object):
    pass

chord = Chord()
chord.notename = 'C'
chord.octave = 3
chord.default = [0,4,7]
chord.name = 'major'
chord.out = [36,39,43]
chord.beat = 1.0 # seconds
chord.arp = True

def bpm(b):
    chord.beat = 60000/b

def getchord(notename=chord.notename, chordname=chord.name, octave=chord.octave):
    chord.notename = notename
    chord.name = chordname
    chord.octave = octave
    chord.default = chords[name]
    chord.out = chords[name]
    notenum = note_names[note]
    transpose = (octave*12)+notenum
    for i in range(0,len(chord.default)):
        #print(i,chord.out[i])
        noteout = chord.default[i]+transpose
        if noteout >= 0
            chord.out[i] = chord.default[i]+transpose
    print chord.out
    return chord.out

try:
    with mido.open_output(portname, autoreset=True) as port:
        print('Using {}'.format(port))
        while True:
            if chord.arp == False:
                print('no arp>>>>>')
                for n in chord.out:
                    print(n)
                    on = Message('note_on', note=n)
                    port.send(on)
                time.sleep(chord.beat/2)
                for n in chord.out:
                    off = Message('note_off', note=n)
                    port.send(off)
                time.sleep(chord.beat/2)
            elif chord.arp == True:
                print('arp ++++++')
                for n in chord.out:
                    noteout = n+24
                    rest = 0.2
                    dur = (chord.beat/2)-rest
                    on = Message('note_on', note=noteout)
                    port.send(on)
                    time.sleep(dur)
                    off = Message('note_off', note=noteout)
                    port.send(off)
                    time.sleep(rest)

except KeyboardInterrupt:
    pass

print()
