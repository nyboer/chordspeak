
#!/usr/bin/env python
"""
Send random notes to the output port.
"""

from __future__ import print_function
import sys
import time
import random
import mido
from mido import Message


if len(sys.argv) > 1:
    portname = sys.argv[1]
else:
    portname = 'Base2 MIDI 1'  # Use default port

# A pentatonic scale
notes = [36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60]

try:
    with mido.open_output(portname, autoreset=True) as port:
        print('Using {}'.format(port))
        while True:
            note = random.choice(notes)

            on = Message('note_on', note=note)
            print('Sending {}'.format(on))
            port.send(on)
            time.sleep(0.2)

            off = Message('note_off', note=note)
            print('Sending {}'.format(off))
            port.send(off)
            time.sleep(0.2)
except KeyboardInterrupt:
    pass

print()
