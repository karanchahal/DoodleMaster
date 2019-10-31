import numpy as np
from PIL import Image
from scipy import misc
import glob,os
from math import floor
from util import cmd_image_visualizer, brightenImage
import re
import time
import imageio
# from hello import get_crop_area

curr_dir = os.getcwd()

def findWhite(img,i,j,mode):

    if(mode == 'rowmajor'):
        for k in range(0,j):
            if img[i][k] > 0:
                return True
    else:
        for k in range(0,j):
            if img[k][i] > 0:
                return True
    
    return False

def findMinPoint(img,min,max,inner_len,mode, reverse):
    
    if(reverse):
        for i in range(min-1,max-1,-1):
            if(findWhite(img,i,inner_len,mode)):
                return i
    else:
        for i in range(min,max):
            if(findWhite(img,i,inner_len,mode)):
                return i
    return 'No element found !!'    

def get_crop_area2(img):
    y_min = 0
    y_max = 0
    x_min = 0
    x_max = 0

    rows = img.shape[0]
    columns = img.shape[1]
    

    y_min = findMinPoint(img,0,rows,columns,'rowmajor', False)
    y_max = findMinPoint(img,rows,0,columns,'rowmajor', True)

    x_min = findMinPoint(img,0,columns,rows,'columnmajor', False)
    x_max = findMinPoint(img,columns,0,rows,'columnmajor', True)

    return y_min,y_max,x_min,x_max


def getSquareCoordinates(y_min,y_max,x_min,x_max):

    l = y_max - y_min
    b = x_max - x_min
    side = abs(l-b)
    if(l > b):
        k = side
        k = k/2
        x_max = x_max + k
        x_min = x_min - k

    if(b > l):
        k = side
        k = k/2
        y_max = y_max + k
        y_min = y_min - k
    
    side = l if l > b else b 
    return x_min,y_min,side

def getPadding(img, size, mode):
    rows = img.shape[0]
    columns = img.shape[1]
    if(mode=='Left'):
        padding = np.zeros((int(rows),int(size)), dtype=np.uint8)
        img = np.concatenate((padding,img),axis=1)
    if(mode=='Right'):
        padding = np.zeros((int(rows),int(size)), dtype=np.uint8)
        img = np.concatenate((img,padding),axis=1)
    if(mode=='Top'):
        padding = np.zeros((int(size),int(columns)), dtype=np.uint8)
        img = np.concatenate((padding,img),axis=0)
    if(mode=='Bottom'):
        padding = np.zeros((int(size),int(columns)), dtype=np.uint8)
        img = np.concatenate((img,padding),axis=0)
        
    return img

def centerImage(img,n):
    img = getPadding(img,n,'Left')
    img = getPadding(img,n,'Right')
    img = getPadding(img,n,'Top')
    img = getPadding(img,n,'Bottom')
    return img


def preprocess(image_path,n=80,brightness=100,size=(28,28),coords=[-1,-1,-1,-1]):
    #print('Processing: ' + image_path)

    start_time = time.time()
    img = imageio.imread(image_path, pilmode='L').astype(int)
    yz,xz = img.shape
    y_min,y_max,x_min,x_max = get_crop_area2(img)
   
    if(coords[0] != -1):
            x_min = coords[0]
            y_min = coords[1]
            x_max = coords[2]
            y_max = coords[3]
    
    

    # Cropping the image 
    img = img[y_min:y_max+1, x_min:x_max+1]
    #print('Cropped image time taken is --- %s seconds ---', (time.time() - start_time))
    start_time = time.time()
    rows = img.shape[0]
    columns = img.shape[1]
    # getting square coordinates
    x,y,side = getSquareCoordinates(0,rows,0,columns)
    
    #print('Square Coordinates time taken is --- %s seconds ---', (time.time() - start_time))
    start_time = time.time()
    # Doing the required padding for converting image to square
    if (x<0):
        size = abs(x)
        img = getPadding(img, size, 'Left')
    
    if(x+side>=columns):
        size = x + side - columns
        img = getPadding(img, size, 'Right')

    if(y<0):
        size = abs(y)
        img = getPadding(img, size, 'Top')

    if(y+side>=rows):
        size = y + side - rows
        img = getPadding(img, size, 'Bottom')    
    
    #print('Padding time taken is --- %s seconds ---', (time.time() - start_time))
    start_time = time.time()

    # Adding final padding to all sides
    final_img = centerImage(img,n)
    #print('Centering time taken is --- %s seconds ---', (time.time() - start_time))
    start_time = time.time()
    imageio.imwrite('tmp.png',final_img)
    final_img = Image.open('tmp.png')
    #print('Image Loading time taken is --- %s seconds ---', (time.time() - start_time))
    start_time = time.time()
    # cmd_image_visualizer(final_img)
    final_img = brightenImage(final_img,brightness,size=size)

    #print('Brightening time taken is --- %s seconds ---', (time.time() - start_time))
    start_time = time.time()
    return final_img,xz,yz
   
