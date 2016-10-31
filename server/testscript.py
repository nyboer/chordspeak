
'''used to test the parsing function with some pre-baked phrases in testscript.txt'''

import httplib2
import urllib

endpoint="http://localhost:5000/chord/"
testscript="testscript.txt"

'''
dummy= {
 "transcript": "D minor play transpose 5 augmented",
 "confidence": 0.9
}
'''


file = open(testscript, 'r')

scripts = file.read().split("\n")
h = httplib2.Http(".cache")

for script in scripts:
    if len(script) != 0:
        dict = { "transcript": script, "confidence": 0.9 }
        '''condidence is just a dummy num'''
        data = urllib.urlencode(dict)
        print script
        resp, content = h.request(endpoint+"?"+data, "GET")
        print(content)
