import mido
from mido import Message

outport = mido.open_output('Base2 MIDI 1')
inport = mido.open_input('Base2 MIDI 1')

for msg in inport:
    msgout = msg
    if hasattr(msg, 'note'):
        msgout.note = msgout.note+4
        outport(msgout)
