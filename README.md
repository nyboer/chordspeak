# chordspeak
Speak a chord, get MIDI out.
##Basic Idea
Using a microphone, speak a chord name and any modifiers (like sharp, transpose, diminshed, expand, octave), and a chord is calculated generated and sent out a MIDI port either as a chord or as arpeggiation. 

##Setup
We are using Python to create MIDI generation functions and send calls to the Google Voice API to convert speech to text. 

The [mido](https://github.com/olemb/mido) python library seems to work well for MIDI i/o. The [documentation](https://mido.readthedocs.io/en/latest/) is clear and the API is easy to understand. To install it for C.H.I.P., you'll need some development tools installed (check out this [script](https://github.com/nyboer/newchipsetup/blob/master/dev.sh), which may be a bit more than you need, but it satisfies the dependencies) just use these simple commands:
```
sudo pip install mido
sudo apt-get install librtmidi-dev libportmidi-dev
```
I'm not entirely sure that `librtmidi-dev` is needed, but I'm too lazy to fully investigate.

