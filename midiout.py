
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

class Chord(object):
    pass

chord = Chord()
chord.default =[0,4,7]
chord.out = [36,39,43]
chord.beat = 1.0 # seconds
chord.arp = True

def bpm(b):
    chord.beat = 60000/b

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
