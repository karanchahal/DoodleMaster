
from __future__ import division

from cython.parallel import parallel, prange
from libc.stdlib cimport abort, malloc, free

import numpy as np
cimport cython
cimport numpy as np

DTYPE = np.int

ctypedef np.int_t DTYPE_t

def say_hello_to(name):
    print("Hello %s!" % name)





@cython.boundscheck(False) # turn off bounds-checking for entire function
@cython.wraparound(False)  # turn off negative index wrapping for entire function
def findWhite(np.ndarray[DTYPE_t, ndim=2] img,int i,int j,mode):
    cdef int k = 0
    if(mode):
        for k in range(0,j):
            if img[i][k] > 0:
                return True
    else:
        for k in range(0,j):
            if img[k][i] > 0:
                return True
    
    return False

@cython.boundscheck(False) # turn off bounds-checking for entire function
@cython.wraparound(False)  # turn off negative index wrapping for entire function
def findMinPoint(np.ndarray[DTYPE_t, ndim=2] img,int min,int max,int inner_len,mode,int reverse):
    cdef int i = 0
    if(reverse):
        for i in range(min-1,max-1,-1):
            if(findWhite(img,i,inner_len,mode)):
                return i
    else:
        for i in range(min,max):
            if(findWhite(img,i,inner_len,mode)):
                return i
    return -1    

@cython.boundscheck(False) # turn off bounds-checking for entire function
@cython.wraparound(False)  # turn off negative index wrapping for entire function
def get_crop_area(np.ndarray[DTYPE_t, ndim=2] img):
    cdef int y_min = 0
    cdef int y_max = 0
    cdef int x_min = 0
    cdef int x_max = 0

    rows = img.shape[0]
    columns = img.shape[1]
    

    y_min = findMinPoint(img,0,rows,columns,1, 0)
    y_max = findMinPoint(img,rows,0,columns,1, 1)

    x_min = findMinPoint(img,0,columns,rows,0, 0)
    x_max = findMinPoint(img,columns,0,rows,0, 1)

    return y_min,y_max,x_min,x_max