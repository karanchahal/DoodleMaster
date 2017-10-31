

from flask import Flask,render_template,send_from_directory,request
app = Flask(__name__, static_folder=".././doodlecollector/build/", template_folder=".././doodlecollector/build/")
import base64


@app.route('/static/<path:path>')
def send_static(path):
    print(path)
    return send_from_directory('.././doodlecollector/build/static/', path)

@app.route("/getImg",methods=['POST'])
def hello_world():
    #doodle = request.files['doodle']
    doodle = request.form['doodle'][22:]
    fh = open("imageToSave.png", "wb")
    fh.write(base64.urlsafe_b64decode(doodle))
    fh.close()

    return render_template("index.html")


@app.route("/")
def index():
    print('hey')
    return render_template("index.html")

if __name__ == '__main__':
    app.run()
