# chordspeak
Speak a chord, get MIDI out.

##Basic Idea
Using a microphone, speak a chord name and any modifiers (like sharp, transpose, diminshed, expand, octave), and a chord is calculated generated and sent out a MIDI port either as a chord or as arpeggiation. A C.H.I.P. computer is used as a device to serve a web-based interface for speech-to-text, parse the resulting string for musical commands, then generate MIDI output to a synthesizer over USB MIDI.


##Setup
We are using Python to create MIDI generation functions and send calls to the Google Voice API to convert speech to text.

###MIDI
The [mido](https://github.com/olemb/mido) python library seems to work well for MIDI i/o. The [documentation](https://mido.readthedocs.io/en/latest/) is clear and the API is easy to understand. To install it for C.H.I.P., you'll need some development tools installed (check out this [script](https://github.com/nyboer/newchipsetup/blob/master/dev.sh), which may be a bit more than you need, but it satisfies the dependencies). Then, just use these simple commands:
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
```

##About The Files In This Repository


###Example Code

####midi
Used to test out and make sure the mido library worked as expected on the C.H.I.P.

####speech2text
Used to test Google Voice API with python. In the end, however, we just used the browser integration for this.

####testwav
In testing the Google Voice API, we created some test sound files of speech so we had a consistent source in an otherwise noisy area. Originally stereo 44.1K WAV, we had to convert them to RAW. The `sox` command was helpful:
```
sudo apt-get install sox
sox C.wav --channels=1 --bits=16 --rate=16000 --encoding=signed-integer --endian=little C.raw
```

