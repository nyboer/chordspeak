from flask import Flask, request, send_from_directory
from flask_cors import CORS, cross_origin
from string import Template

'''app = Flask(__name__, static_url_path='/public')'''
app = Flask(__name__, static_url_path='')
CORS(app)

@app.route("/")
def index():
    return app.send_static_file('index.html')


@app.route("/chord/")
def chord():
    chord = request.args.get('transcript')
    confidence = request.args.get('confidence')

    '''do midi staff with chord request'''
    t = Template("chord request='${chord}' (${confidence})")

    str = t.substitute({"chord": chord, "confidence": confidence})
    print("========================================")
    print(str)
    print("========================================")

    return "ok"

if __name__ == "__main__":
    app.run()
