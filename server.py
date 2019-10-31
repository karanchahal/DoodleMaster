from flask_socketio import SocketIO, send, emit
from flask import Flask,render_template,send_from_directory,request
from flask_cors import CORS
import base64
import pickle
from PIL import Image
from scipy import misc
from preprocessing import preprocess
import layout_gen
import os,time
import numpy as np
import h5py
import imageio
import torch
import torch.nn as nn
import torch.optim as optim
from torch.optim import lr_scheduler
from torch.autograd import Variable
import numpy as np
import torchvision
from torchvision import datasets, models, transforms
import time
import os
import torch.nn.functional as F
from classifier import YoloClassifier
import utils
import shutil
import numpy 

app = Flask(__name__, template_folder="frontend")
class_keys = ['Button','EditText','Header','ImageView','TextView']
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

app.config['SECRET_KEY'] = 'mysecret'
app.config["CACHE_TYPE"] = "null"

socketio = SocketIO(app)

def normalizing(X):
   return X/255

def load_checkpoint(model,filename='./weights/model.pth.tar'):
   checkpoint = torch.load(filename)
   model.load_state_dict(checkpoint['state_dict'])
   return model

class_size = 5
CORS(app)
@app.route('/css/<path:path>')
def send_css(path):
   return send_from_directory('frontend/css/', path)

model = None

@app.route('/js/<path:path>')
def sendjs(path):
   print(path[:-4])
   return send_from_directory('frontend/js/', path)

@app.route('/imgs/<path:path>')
def sendImg(path):
   print(path[:-4])
   return send_from_directory('frontend/imgs/', path)

@socketio.on('getImg')
def hello_world(payload):
   global model
   doodle = payload['doodle'][22:]
   coords = payload['coords']

   coords[0] = int(coords[0])
   coords[1] = int(coords[1])
   coords[2] = int(coords[2])
   coords[3] = int(coords[3])
   
   id_ = payload['id']
   pickle.dump(doodle,open('doodle.p','wb'))
   fh = open("imageToSave.png", "wb")
   fh.write(base64.urlsafe_b64decode(doodle))
   fh.close()
   #noo = numpy.array(Image.open('imageToSave.png',mode='r')).astype(int)
   #print(noo.shape)
   img,x,y = preprocess('./imageToSave.png',n=30,brightness=120,coords=coords)
   img = imageio.imread('tmp.png').astype('float32')
   img = np.stack((img,)*3)
   img = torch.Tensor(normalizing(img))
   img = img.view(1,3,256,256)
   img = Variable(img)
   # loading the trained model
   if model is None:
       model = YoloClassifier(utils.net('tiny_yolo',in_channels=3),class_size=class_size,batch_size=1)
       model = load_checkpoint(model)
   
   out = model(img)
   _, preds = torch.max(out.data, 1)
 
   preds = preds.numpy()
   preds = preds[0]
   print("\nI think it's a : " + str(class_keys[preds]))

   emit('message',{'message':str(class_keys[preds]) })
   buildLayout(coords,x,y,preds,id_)

def buildLayout(coords,x,y,label,id_):
   layout_gen.init(label,coords,x,y,id_)
   layout_gen.build()


@app.route("/")
def index():
   return render_template("index.html")


@socketio.on('clear')
def handleMessages(payload):
   layout_gen.elements = []


if __name__ == '__main__':
   socketio.run(app, host='0.0.0.0', debug = True, port = 5000)
