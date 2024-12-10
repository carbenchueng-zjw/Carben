import numpy

def iou(arr1,arr2):
    area1 = (arr1[2]-arr1[0]) *((arr1[3]-arr1[1]))
    area2 = (arr2[2]-arr2[0]) *((arr2[3]-arr2[1]))
    x1 = numpy.maximum(arr1[0],arr2[0])
    y1 = numpy.maximum(arr1[1],arr2[1])
    x2 = numpy.minimum(arr1[2],arr2[2])
    y2 = numpy.minimum(arr1[3],arr2[3])

    w = numpy.maximum(0,x2-x1)
    h = numpy.maximum(0,y2-y1)
    inv = w*h
    iou1 = inv/(area1+area2 - inv)
    return iou1
