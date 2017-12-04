from scipy import misc
import util
from xml.etree import ElementTree as ET
from xml.dom import minidom
elements = []
h = 0
w = 0
main_html = '<!DOCTYPE html><html lang="en"><head><title>DevTips Starter Kit</title><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><link rel="shortcut icon" href="assets/img/favicons/favicon.ico"><script src="assets/js/reload.js"></script><link rel="stylesheet" href="main.css" /></head><body>'
def init(element_type,coords,W,H,id_):
  
    x_min = coords[0]
    x_max = coords[2]
    y_min = coords[1]
    y_max = coords[3]

    x_percent = 100*float(x_min/W)
    y_percent = 100*float(y_min/H)

    h_percent = float((y_max - y_min)/H)*100
    w_percent = float((x_max - x_min)/W)*100

    elements.append([element_type,x_percent,y_percent,w_percent,h_percent,id_])

def Button(i,margin_top,x,y,w,h,id):
    html = '<button class="red-button" style="margin-top:'  + str(margin_top)+ 'vh"> Insert Text Here </button>'
    return html

def ButtonXml(i,margin_top,x,y,w,h,id):
    print(margin_top)
    Button_Layout = ET.Element("Button",{"android:layout_width":"match_parent",
                    "android:layout_height":"60dp",
                    "android:layout_marginTop":str(margin_top*7.1) + "dp",
                    "android:textSize":"30sp",
                    "android:background":"@color/primary",
                    "android:text":"Log on",
                    "android:id":"@+id/" + id,
                    "android:layout_marginLeft":"8dp",
                    "android:layout_marginRight":"8dp",
                    "android:textAllCaps":"false",
                    "android:typeface":"serif",
                    "android:textColor":"#FFF"})
    return Button_Layout



def TextView(i,margin_top,x,y,w,h,id):

    html = "<div class='terms-conditions' style='margin-top:" + str(margin_top)+ "vh;height:" + str(h)+ "vh'> <div class='main-heading'>Terms and Conditions</div> <h2>The Blah</h2> Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum. Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum. <h2>The Blah</h2> Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum. Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum. <h2>The Blah</h2> Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum. </div>"
    return html

def TextViewXml(i,margin_top,x,y,w,h,id):
    TextView_Layout = ET.Element("LinearLayout", {"android:layout_width": "match_parent",
                                "android:layout_height": "wrap_content",
                                "android:paddingLeft": "20dp",
                                "android:paddingRight":"20dp",
                                "android:orientation":"vertical",
                                "android:layout_marginTop":str(margin_top*7.1) + "dp"})

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

    return TextView_Layout

def EditText(i,margin_top,x,y,w,h,id):
    html = '<div style="fontSize: "1.5em";margin-top' + str(margin_top)+ 'vh"> class="sub-heading">Memorable Answer</div> <input type="password" name="answer" style={{width:"90vw"}}/>'
    return html

def EditTextXml(i,margin_top,x,y,w,h,id):
    EditText_Layout = ET.Element("EditText",{
            "android:layout_width":"match_parent",
            "android:layout_height":"60dp",
            "android:paddingLeft":"8dp",
            "android:id":"@+id/" + id,
            "android:textSize":"20sp",
            "android:paddingRight":"10dp",
            "android:singleLine":"true",
            "android:layout_marginLeft":"8dp",
            "android:layout_marginRight":"8dp",
            "android:layout_marginTop":str(margin_top*7.1) + "dp",
            "android:background":"@drawable/sign_up_cell_border"})
    return EditText_Layout

def Header(i,margin_top,x,y,w,h,id):
    html = '<div class="header"> <div class="logo"><img src="assets/img/hsbc-logo.svg"></div> </div> <div class="heading"> <div class="page-type"> ACCOUNT LINKING </div> </div> <div class="loadingbar"></div> <div class="container">'
    return html


def HeaderXml(i,margin_top,x,y,w,h,id):
    Image_Layout = ET.Element("ImageView",{
        "android:layout_width":"match_parent",
        "android:layout_height":"50dp",
        "android:src":"@drawable/hsbc_logo" 
    })

    TextLayout = ET.Element("TextView",{
        "android:layout_width":"match_parent",
        "android:layout_height":"50dp",
        "android:text":"ACCOUNT LINKING",
        "android:textSize":"20dp",
        "android:typeface":"serif",
        "android:textColor":"@color/white",
        "android:background":"#3e5057",
        "android:gravity":"center"
    })
    return Image_Layout,TextLayout


def ImageView(i,margin_top,x,y,w,h,id):
    html = '<img class="img-box" id=" '+ str(id)+'" src="assets/img/image.jpg" style="margin-top:' + str(margin_top)+ 'vh;height:' + str(h)+ 'vh">'
    return html

def ImageViewXml(i,margin_top,x,y,w,h,id):
    Image_Layout = ET.Element("ImageView",{"android:layout_width":"match_parent",
        "android:layout_height":str(h*7.1) + "dp",#change
        "android:layout_marginTop":str(margin_top*7.1) + "dp",
        "android:id":"@+id/" + id,
        "android:src":"@drawable/digital",
        "android:scaleType":"fitXY"})
    return Image_Layout
class_keys = ['Button','EditText','Header','ImageView','TextView']

#create a tree
def build():
    global elements,main_html
    doc = '<?xml version="1.0" ?> <LinearLayout android:id="@+id/activity_main" android:layout_height="match_parent" android:layout_width="match_parent" android:orientation="vertical" android:paddingBottom="@dimen/activity_vertical_margin" android:paddingLeft="@dimen/activity_horizontal_margin" android:paddingRight="@dimen/activity_horizontal_margin" android:paddingTop="@dimen/activity_vertical_margin" ns1:context="com.example.d4079125.myapplication.MainActivity" xmlns:android="http://schemas.android.com/apk/res/android" xmlns:ns1="http://schemas.android.com/tools"> </LinearLayout>'
    
    filepath = "../../AndroidStudioProjects/MyApplication/app/src/main/res/layout/activity_main.xml"
     
    doc = ET.ElementTree(ET.fromstring(doc))
    #file.close()
    root = doc.getroot()
    #elementz = sorted(elements,key=lambda element: element[3]*element[4])
    elementx = sorted(elements,key=lambda element: element[2] + element[4])
    tree = []
    htmlfinal = main_html
    #html and css
    for i in range(len(elementx)):
        e = elementx[i]
        print(e)
        margin_top = 0

        if i != 0:
            prev = elementx[i-1]
            margin_top = e[2] - (prev[2] + prev[4])
        else:
            margin_top = e[2]

        print(margin_top)
        element_type = e[0]
        x = e[1]
        y = e[2]
        w = e[3]
        h = e[4]
        id_ = e[5]
        html = ''
        if(element_type == 3):
            html = ImageView(i,margin_top,x,y,w,h,id_)
            xml = ImageViewXml(i,margin_top,x,y,w,h,id_)
            xmlFilePath = "../../AndroidStudioProjects/MyApplication/app/src/main/res/layout/activity_main.xml"
            root = util.appendElementToXML(xmlFilePath,10,root,xml)
        elif(element_type == 4):
            html = TextView(i,margin_top,x,y,w,h,id_)
            xml = TextViewXml(i,margin_top,x,y,w,h,id_)
            xmlFilePath = "../../AndroidStudioProjects/MyApplication/app/src/main/res/layout/activity_main.xml"
            root = util.appendElementToXML(xmlFilePath,10,root,xml)
        elif(element_type == 2):
            #djdj
            html = Header(i,margin_top,x,y,w,h,id_)
            xml1,xml2 = HeaderXml(i,margin_top,x,y,w,h,id_)
            xmlFilePath = "../../AndroidStudioProjects/MyApplication/app/src/main/res/layout/activity_main.xml"
            root = util.appendElementToXML(xmlFilePath,10,root,xml1)
            root = util.appendElementToXML(xmlFilePath,10,root,xml2)
        elif(element_type == 1):
            #ded
            html = EditText(i,margin_top,x,y,w,h,id_)
            xml = EditTextXml(i,margin_top,x,y,w,h,id_)
            xmlFilePath = "../../AndroidStudioProjects/MyApplication/app/src/main/res/layout/activity_main.xml"
            root = util.appendElementToXML(xmlFilePath,10,root,xml)
        elif(element_type == 0):
            #djdj
            html = Button(i,margin_top,x,y,w,h,id_)
            xml = ButtonXml(i,margin_top,x,y,w,h,id_)
            xmlFilePath = "../../AndroidStudioProjects/MyApplication/app/src/main/res/layout/activity_main.xml"
            root = util.appendElementToXML(xmlFilePath,10,root,xml)

        htmlfinal = htmlfinal + html
        
    roughString = ET.tostring(root, 'utf-8')
    util.writeToFile('./output.html',htmlfinal)
    reparsed = minidom.parseString(roughString)
    util.writeToFile(filepath,reparsed.toprettyxml())

# # init('ImageView',)
# init('ImageView',[587, 550, 1037, 782],1680,953)
# init('ImageView',[554, 203, 1052, 494],1680,953)

# build()
