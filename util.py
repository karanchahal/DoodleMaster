import numpy as np
from PIL import Image
from scipy import misc
from xml.etree import ElementTree as ET
from xml.dom import minidom
import bcolz
import imageio

# function to view np array in cmd
def cmd_image_visualizer(x):
    height = x.shape[0]
    width = x.shape[1]
    for i in range(height):
        for j in range(width):
            print(str(x[i][j]) + "\t" ,end='')
        print('',end='\n')

def displayImage(x):
    height = x.shape[0]
    width = x.shape[1]
    img = Image.fromarray(x.reshape(height,width))
    img.show()

def brightenImage(img,brightness,size):
    filename = 'tmp.png'
    img = img.resize((256,256),Image.BILINEAR)
    img = img.point(lambda x : 0 if x< 28 else (255 if x+brightness>255 else x+brightness))
    
    img.save(filename)
    img = imageio.imread(filename,pilmode='L').astype(int)

    return img


def shuffle(a,b):
    assert len(a) == len(b)
    p = np.random.permutation(len(a))
    return a[p], b[p]


def shuffle_one(a):
    p = np.random.permutation(len(a))
    return a[p]

def writeToFile(filepath,x):
    with open(filepath,'w') as f:
        f.write(x)
        f.close()



def appendToFile(filepath):
    return open(filepath,'r')


def appendElementToXML(filepath, label,root,xml =None):
    ET.register_namespace('android',"http://schemas.android.com/apk/res/android")

    ImageView_Layout = ET.Element("LinearLayout", {"android:layout_width": "match_parent",
                                "android:layout_height": "wrap_content",
                                "android:background": "@drawable/border",
                                "android:layout_margin":"10dp",
                                "android:orientation":"vertical"})
                                
    image = ET.Element("ImageView", {"android:layout_width": "match_parent",
                                "android:layout_height": "220dp",
                                "android:src": "@drawable/digital",
                                "android:padding":"10dp"})
                                                            
    line = ET.Element("LinearLayout", {"android:layout_width": "match_parent",
                                "android:layout_height": "1dp",
                                "android:background": "#000"})
                                
    caption = ET.Element("TextView", {"android:layout_width": "match_parent",
                                "android:layout_height": "wrap_content",
                                "android:text": "@string/image_caption",
                                "android:textColor":"#000",
                                "android:textSize":"20sp",
                                "android:gravity":"center",
                                "android:padding":"10dp"})

    ImageView_Layout.append(image)
    ImageView_Layout.append(line)
    ImageView_Layout.append(caption)


    TextView_Layout = ET.Element("LinearLayout", {"android:layout_width": "match_parent",
                                "android:layout_height": "wrap_content",
                                "android:paddingLeft": "20dp",
                                "android:paddingRight":"20dp",
                                "android:orientation":"vertical"})

    title = ET.Element("TextView", {"android:layout_width": "match_parent",
                                "android:layout_height": "wrap_content",
                                "android:text": "@string/tv_title",
                                "android:textSize":"25sp",
                                "android:textColor":"#000"})

    author = ET.Element("TextView", {"android:layout_width": "match_parent",
                                "android:layout_height": "wrap_content",
                                "android:text": "@string/author",
                                "android:textSize":"18sp"})

    content = ET.Element("TextView", {"android:layout_width": "match_parent",
                                "android:layout_height": "wrap_content",
                                "android:text": "@string/content",
                                "android:textSize":"18sp",
                                "android:layout_marginTop":"5dp"})

    # appending each data to textView
    TextView_Layout.append(title)
    TextView_Layout.append(author)
    TextView_Layout.append(content)

    
    # Append the new "data" elements to the root element of the XML document
    if(label == 0):
        root.append(TextView_Layout)    
    elif (label == 1):
        root.append(ImageView_Layout)
    
    if(xml != None):
        root.append(xml)

    # Now we have a new well-formed XML document. It is not very nicely formatted...
    #indent(root)
    return root
    #     roughString = ET.tostring(root, 'utf-8')
    #    # print(type(out))
        

    #     # ...so we'll use minidom to make the output a little prettier
        
        
        

    #     #print(reparsed.toprettyxml())    


def getView(label):
    View = ""
    if(label == 0):
        View = '<TextView \
        android:layout_width="match_parent" \
        android:layout_height="wrap_content" \
        android:text="Welcome to" \
        android:textSize="25sp" \
        android:gravity="center_horizontal" \
        android:textColor="@color/textColor" \
        android:id="@+id/hsbc_tv"/>'
    
    elif(label == 1):
        View = '<ImageView \
        android:layout_width="match_parent" \
        android:layout_height="100dp" \
        android:src="@drawable/HSBC_logo" \
        android:layout_gravity="center_horizontal" \
        android:id="@+id/hsbc_logo"/>'     
    return View        



# loads the dataset from .npy files
def load_data(data_list,DATA_HOME_DIR):
    classes = {}

    for data in data_list:
        key = data[:-4] # trimming file name to <> from <>.npy
        classes[key] = np.load(DATA_HOME_DIR +  data) # loading numpy array

    return classes


def doOverlap(l1x,l1y,r1x,r1y,l2x,l2y,r2x,r2y):

    if (r1y < l2y or l1y > r2y or r1x < l2x or l1x > r2x):
        return False

    return True


def initNumpy(shape):
     return np.empty(shape).astype('float32')

def appendNumpy(X,x):
    return np.concatenate((X,x))



def save_array(fname, arr):
    c=bcolz.carray(arr, rootdir=fname, mode='w')
    c.flush()


def load_array(fname):
    return bcolz.open(fname)[:]
#def get
