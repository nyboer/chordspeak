from flask import Flask, request, send_from_directory
from flask_cors import CORS, cross_origin
from string import Template

import json
import re

'''app = Flask(__name__, static_url_path='/public')'''
app = Flask(__name__, static_url_path='')
CORS(app)
pattern = r"^[abcdefgABCDEFG]$"

def parser(str):
    chords = str.split(" ")
    idx = 0
    ret = {"notes": []}

    for chord in chords:
        note = ""
        if(chord == "major"
                or chord == "minor"
                or chord == "diminished"
                or chord == "dominant"
                or chord == "half"
                ):
            # parsing notes
            _l = chords[idx - 1]
            if(_l == "sharp" or _l == "flat"):
                note = chords[idx - 2].lower() + " " + _l.lower()
            elif re.match(pattern, _l):
                note = _l.lower()

            # parsing major, minor, etc.
            params = []
            if(len(chords) > (idx + 1) and chords[idx + 1] == "seventh"):
                chord += " seventh"
            elif chord == "half" and chords[idx + 1] == "diminished" and chords[idx + 2] == "seventh":
                chord = "half diminished seventh"

            params.append(chord)

            # parsing pitch, augumented
            seq = [1,2,3,4]
            for num in seq:
                if(len(chords) > (idx + num)):
                    if(chords[idx + num] == "pitch" or chords[idx + num] == "augmented"):
                        params.append(chords[idx + num])

            if(note != ""):
                ret["notes"].append({
                    "note": note,
                    "params": params
                })

        if(chord == "transpose"):
            ret["transpose"] = chords[idx + 1]
        if(chord == "octave"):
            ret["octave"] = chords[idx + 1]
        if(chord == "arpeggiate"):
            ret["arpeggiate"] = True
        if(chord == "play"):
            ret["play"] = True

        idx += 1



    return ret

@app.route("/")
def index():
    return app.send_static_file('index.html')


@app.route("/chord/")
def chord():
    chords = request.args.get('transcript')
    confidence = request.args.get('confidence')

    '''do midi stuff with chord request'''
    t = Template("request='${chords}' (${confidence})")

    str = t.substitute({"chords": chords, "confidence": confidence})
    print("========================================")
    print(str)
    print("========================================")

    resp = parser(chords)

    print json.dumps(resp, indent=4, sort_keys=True)

    return json.dumps(resp)

if __name__ == "__main__":
    app.run()
