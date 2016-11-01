# chordspeak
Speak a chord, get MIDI out. A project by Peter Nyboer, Kensaku Komatsu, and Alana Stevenson for the MIDI Hackathon at Google, 10/28/16 and 10/29/16.

##Basic Idea
Using a microphone, speak a chord name and any modifiers (like sharp, transpose, diminshed, expand, octave), and a chord is calculated generated and sent out a MIDI port either as a chord or as arpeggiation. A C.H.I.P. computer is used as a device to serve a web-based interface for speech-to-text, parse the resulting string for musical commands, then generate MIDI output to a synthesizer over USB MIDI.

Run the program on C.H.I.P. from the `server/`
```
python server.py
```

##Setup
We are using Python to create MIDI generation functions and send calls to the Web Speech API to convert speech to text.

###General
There are several dependencies that are satisfied with [this setup script](https://github.com/nyboer/newchipsetup/blob/master/dev.sh). This may be a bit more than you need, but it will make the rest of the installation and any future work easier. 

###MIDI
The [mido](https://github.com/olemb/mido) python library seems to work well for MIDI i/o. The [documentation](https://mido.readthedocs.io/en/latest/) is clear and the API is easy to understand. To install mido, just use these simple commands:
```
sudo pip install mido
sudo apt-get install librtmidi-dev libportmidi-dev
```
(I'm not entirely sure that `librtmidi-dev` is needed, but I'm too lazy to fully investigate.)

###Server
The Flask server has some dependencies as well:
```
sudo pip install Flask
sudo pip install flask-cors
sudo pip install google-api-python-client
sudo pip install pyopenssl
```

##About The Files In This Repository

###server

####midiout.py
A python module that creates a Chord object that can be modified and played as MIDI by some simple functions. These functions are designed to be executed by voice control.

####server.py
The main script that:
 * serves a web page to processes speech commands (from `static`)
 * parses strings from the speech-to-text results (`def parser()`)
 * executes functions from midiout module (`midiout.py`)
 * outputs MIDI notes (`midiout.py`)

There is also a `keys/` directory that has self-signed keys for running the Flask server with https. The `testscript.py` was used to test out and develop the command parsing function.

####static/speech.html
Provides an interface to Web Speech API for speech to text conversion.

###Example Code

####midi
Used to test out and make sure the mido library worked as expected on the C.H.I.P.

####speech2text
Used to test Google Cloud Speech API with python. In the end, however, we just used the browser integration for this.

####testwav
In testing the Speech API, we created some test sound files of speech so we had a consistent source in an otherwise noisy area. Originally stereo 44.1K WAV, we had to convert them to RAW. The `sox` command was helpful:
```
sudo apt-get install sox
sox C.wav --channels=1 --bits=16 --rate=16000 --encoding=signed-integer --endian=little C.raw
```

