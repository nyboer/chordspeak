
#!/usr/bin/env python
"""
Send random notes to the output port.
"""

import sys
import time
import mido
from mido import Message

if len(sys.argv) > 1:
    portname = sys.argv[1]
else:
    # portname = 'Base2 MIDI 1'  # Use default port
    portname = 'MicroBrute MIDI 1'


port = mido.open_output(portname, autoreset=True)
class Chord(object):
    def __init__(self):
        self.notename = 'c'
        self.octave = 3
        self.default = [0,4,7]
        self.name = 'major'
        self.out = [36,39,43]
        self.beat = 1.0 # seconds
        self.arp = True
        self.chords = {
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
        self.note_names = {
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

    def bpm(self,b):
        self.beat = 60000/b

    def getchord(self,nn=None, chn=None, octv=None):
        if nn:
            self.notename = nn
        if chn:
            self.name = chn
        if octv:
            self.octave = octv
        self.default = self.chords[self.name]
        self.out = self.chords[self.name]
        notenum = self.note_names[self.notename]
        transpose = (self.octave*12)+notenum
        print('transpose: '+str(transpose))
        for i in range(0,len(self.default)):
            #print(i,self.out[i])
            noteout = self.default[i]+transpose
            if noteout >= 0:
                self.out[i] = self.default[i]+transpose
        print 'chord: '+str(self.out)
        return self.out

    def play(self):
        print('play chord>>>>>')
        for n in self.out:
            print(n)
            on = Message('note_on', note=n)
            port.send(on)
        time.sleep(self.beat/2)
        for n in self.out:
            off = Message('note_off', note=n)
            port.send(off)

    def arpeggiate(self):
        print('arp ++++++')
        for n in self.out:
            print('arp note: '+str(n))
            rest = 0.1
            dur = (self.beat/4)-rest
            on = Message('note_on', note=n)
            port.send(on)
            time.sleep(dur)
            off = Message('note_off', note=n)
            port.send(off)
            time.sleep(rest)


if __name__ == '__main__':
    try:
        print('Using {}'.format(port))
        chord = Chord()
        chord.getchord()
        chord.arpeggiate()
        chord.getchord('e','minor',4)
        chord.arpeggiate()
        chord.getchord('d','major')
        chord.arpeggiate()
        chord.getchord('f','diminished',2)
        chord.arpeggiate()
    except KeyboardInterrupt:
        pass
