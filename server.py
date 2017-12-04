

from flask import Flask,render_template,send_from_directory,request
app = Flask(__name__, static_folder=".././doodlecollector/build/", template_folder=".././doodlecollector/build/")
import base64
import pickle
from scipy import misc
from preprocessing import preprocess
from flask_cors import CORS
import json
app = Flask(__name__)
CORS(app)

@app.route('/static/<path:path>')
def send_static(path):
    print(path)
    return send_from_directory('.././doodlecollector/build/static/', path)

@app.route("/getImg",methods=['POST'])
def hello_world():
    from flask import jsonify
    print(request)
    req= request.json
    print(req)
    req = req.data
    doodle = req['doodle'][22:]
    coords = req['coords']

    #doodle = request.files['doodle']
    #print(request.data)
    # print(request.form['coords'])
    # doodle = request.form['doodle'][22:]
    pickle.dump(doodle,open('doodle.p','wb'))
    fh = open("imageToSave.png", "wb")
    fh.write(base64.urlsafe_b64decode(doodle))
    fh.close()
    img = preprocess('./imageToSave.png',n=80,brightness=120)
    #misc.imshow(img)
    return jsonify(**request.json)


@app.route("/")
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run()
