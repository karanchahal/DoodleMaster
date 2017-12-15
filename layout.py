from scipy import misc
import util
from xml.etree import ElementTree as ET
from xml.dom import minidom
from bs4 import BeautifulSoup as bs
import math
from random import randint

elements = []
h = 0
w = 0
main_html = '<!DOCTYPE html><html lang="en"><head><title>Output</title><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><link rel="shortcut icon" href="assets/img/favicons/favicon.ico"><script src="assets/js/reload.js"></script><link rel="stylesheet" href="main.css" /></head><body>'
colors = ['red','green','blue','black','pink']


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

    print('X',x_percent)
    print('Y',y_percent)
    print('Height', h_percent)
    print('Width', w_percent)
    

    elements.append([element_type,x_percent,y_percent,w_percent,h_percent,id_])

def div(margin_top,h,w):
    hv

#create a tree
def build():
    global elements,main_html
    
    class_id = {}

    elementy = sorted(elements,key=lambda element: element[2])
    htmlfinal = main_html
    #html and css
    for i in range(len(elementy)):
        e = elementy[i]
       
        element_type = e[0]
        x = e[1]
        y = e[2]
        w = e[3]
        h = e[4]
        id_ = e[5]
        randomColor = randint(0,len(colors) -1 )
        if id_ not in class_id:
            color = colors[randomColor]
            class_id[id_] = color
        else:
            color = class_id[_id]
            
        html = '<div id= "' + str(id_) + '"style="height:' + str(h) + 'vh;width:' + str(w) + 'vw;position:absolute;top:' + str(y) + 'vh;left:' + str(x) + 'vw;background-color:' + str(color) + '"></div>'
        htmlfinal = htmlfinal + html
    
    

    soup=bs(htmlfinal)                
    prettyHTML=soup.prettify()   
    util.writeToFile('./output.html',prettyHTML)