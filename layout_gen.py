from scipy import misc
import util
from xml.etree import ElementTree as ET
from xml.dom import minidom
from bs4 import BeautifulSoup as bs
import math


elements = []
h = 0
w = 0
main_html = '<!DOCTYPE html><html lang="en"><head><title>Output</title><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><link rel="shortcut icon" href="assets/img/favicons/favicon.ico"><script src="assets/js/reload.js"></script><link rel="stylesheet" href="main.css" /></head><body>'


def getClean(margin_top):
    margin_top = math.floor(margin_top)
    ones = margin_top%10

    if(margin_top >= 10):

        if(ones > 5):
            margin_top = (margin_top - margin_top%10) +10
        else:
            margin_top = (margin_top- margin_top%10)
    
    return margin_top

def init(element_type,coords,W,H,id_):
  
    x_min = coords[0]
    x_max = coords[2]
    y_min = coords[1]
    y_max = coords[3]

    x_percent = 100*float(x_min/W)
    y_percent = 100*float(y_min/H)

    h_percent = float((y_max - y_min)/H)*100
    w_percent = float((x_max - x_min)/W)*100

    x_percent = getClean(x_percent)
    y_percent = getClean(y_percent)
    h_percent = getClean(h_percent)
    w_percent = getClean(w_percent)


    print('Height', h_percent)
    print('Width', w_percent)
    

    elements.append([element_type,x_percent,y_percent,w_percent,h_percent,id_])

def Button(i,margin_top,x,y,w,h,id):
    html = '<button class="red-button" style="margin-top:'  + str(margin_top)+ 'vh">Button Label</button>'
    return html

def ButtonXml(i,margin_top,x,y,w,h,id):
    print(margin_top)
    Button_Layout = ET.Element("Button",{"android:layout_width":"match_parent",
                    "android:layout_height":"60dp",
                    "android:layout_marginTop":str(margin_top*7.1) + "dp",
                    "android:textSize":"30sp",
                    "android:background":"@color/primary",
                    "android:text":"Button Label",
                    "android:id":"@+id/" + id,
                    "android:layout_marginLeft":"8dp",
                    "android:layout_marginRight":"8dp",
                    "android:textAllCaps":"false",
                    "android:typeface":"serif",
                    "android:textColor":"#FFF"})
    return Button_Layout

def TextView(i,margin_top,x,y,w,h,id):

    print('Height is ' + str(h))
    html1 = '<div class="main-heading" style="margin-top:' + str(margin_top)+ 'vh;">Sub Heading</div>'
    
    html2 = '<div class="sub-heading" style="margin-top:' + str(margin_top)+ 'vh;"> Sub Sub Heading . Used for explaining the topic in detail</div>'
       
    html = '<div class="main-heading" style="font-size:3em;text-align:center;margin-top:' + str(margin_top)+ 'vh;">Heading</div>'
    if(h > 27):
        return html
    elif(h > 11):
        return html1
    else:
        return html2

def TextViewXml(i,margin_top,x,y,w,h,id):
   
    LargeText = ET.Element("TextView", {"android:layout_width": "match_parent",
                                "android:layout_height": "wrap_content",
                                "android:paddingTop": "5dp",
                                "android:paddingBottom":"5dp",
                                "android:id":"id",
                                "android:text":"Heading",
                                "android:layout_marginTop":str(margin_top*7.1) + "dp",
                                "android:gravity":"center",
                                "android:textColor":"#000",
                                "android:textSize":"50sp"})


    MediumText = ET.Element("TextView", {"android:layout_width": "match_parent",
                                "android:layout_height": "wrap_content",
                                "android:paddingTop": "5dp",
                                "android:paddingBottom":"5dp",
                                "android:id":"id",
                                "android:text":"Sub Heading",
                                "android:layout_marginTop":str(margin_top*7.1) + "dp",
                                "android:textColor":"#000",
                                "android:textSize":"30sp"})

    SmallText = ET.Element("TextView", {"android:layout_width": "match_parent",
                                "android:layout_height": "wrap_content",
                                "android:paddingTop": "5dp",
                                "android:paddingBottom":"5dp",
                                "android:id":"vertical",
                                "android:text":"Sub Sub Heading. Used for explaining the text in detail.",
                                "android:layout_marginTop":str(margin_top*7.1) + "dp",
                                "android:style":"italic"})

    if(h > 27):
        return LargeText
    elif(h > 11):
        return MediumText
    else:
        return SmallText


def EditText(i,margin_top,x,y,w,h,id):
    html = '<div style="fontSize: "1.5em";margin-top' + str(margin_top)+ 'vh" class="sub-heading">Placeholder</div> <input type="password" name="answer" style="width:90vw;"/>'
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
            "android:background":"@drawable/sign_up_cell_border",
            "android:hint":"Placeholdera"})
    return EditText_Layout

def Header(i,margin_top,x,y,w,h,id):
    html = '<div class="heading"> <div class="page-type"> HEADER </div> </div> <div class="loadingbar"></div> <div class="container">'
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

        print('Old', margin_top)

        margin_top  = getClean(margin_top)

        print('New margin',margin_top)
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

    soup=bs(htmlfinal)                
    prettyHTML=soup.prettify()   

    util.writeToFile('./output/output.html',prettyHTML)
    reparsed = minidom.parseString(roughString)
    # Commented out for Android XML code
    #util.writeToFile(filepath,reparsed.toprettyxml())
