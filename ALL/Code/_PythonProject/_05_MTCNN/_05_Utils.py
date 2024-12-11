import numpy,torch


def IouPro(box, boxes, isMin=False):
    # 求框的面积
    arr = (box[2] - box[0]) * (box[3] - box[1])
    # print(arr)
    arres = (boxes[:, 2] - boxes[:, 0]) * (boxes[:, 3] - boxes[:, 1])

    x_1 = numpy.maximum(box[0], boxes[:, 0])
    y_1 = numpy.maximum(box[1], boxes[:, 1])
    x_2 = numpy.minimum(box[2], boxes[:, 2])
    y_2 = numpy.minimum(box[3], boxes[:, 3])

    w = numpy.maximum(0, x_2 - x_1)
    h = numpy.maximum(0, y_2 - y_1)

    inv = w * h
    if isMin:
        iou = numpy.true_divide(inv, numpy.minimum(arr + arres - inv))
    else:
        iou = numpy.true_divide(inv, (arr + arres - inv))

    return iou

# boex.shape（n , 5）

def Nms(boxes, thresh=0.3,isMin=False):
    if boxes.shape[0] == 0:
        return numpy.array(())
    _boxes = boxes[numpy.argsort(-boxes[:, 4])]

    # print(_boxes[0])
    # 最终输出所有的框
    r_boxes = []

    while _boxes.shape[0] > 1:
        a_box = _boxes[0]

        b_boxes = _boxes[1:]
        r_boxes.append(a_box)

        # 置信度最大的框和其他的框分别求iou
        iou = IouPro(a_box, b_boxes)
        # print(iou)
        #     # 去除和第一个box的iou小于阈值的框
        index = numpy.where(iou < thresh)
        #     # print(box_index)
        _boxes = b_boxes[index]
        # exit()
    if _boxes.shape[0] > 0:
        r_boxes.append(r_boxes[0])
    # print(numpy.stack(r_boxes))
    return numpy.stack(r_boxes)


# 扩充：找到中心点和最大边长，沿着最大变长两边扩充
def ConvertToSquare(bbox):  # 将长方形框补齐，变成正方形
    square_bbox = bbox.copy()

    if square_bbox.shape == 0:
        return numpy.array([])
    h = bbox[:, 3] - bbox[:, 1]
    w = bbox[:, 2] - bbox[:, 0]
    max_side = numpy.maximum(h, w)

    square_bbox[:, 0] = bbox[:, 0] + w * 0.5 - max_side * 0.5
    square_bbox[:, 1] = bbox[:, 1] + h * 0.5 - max_side * 0.5
    square_bbox[:, 2] = square_bbox[:, 0] + max_side
    square_bbox[:, 3] = square_bbox[:, 1] + max_side
    # print(type(square_bbox))
    return square_bbox


if __name__ == '__main__':
    box = numpy.array([1, 1, 11, 11])
    boxes = numpy.array([[1, 1, 10, 10], [11, 11, 25, 25]])
    iou = IouPro(box, boxes)
    print(iou)

    # boxes = numpy.array([[1, 1, 10, 10, 40], [1, 1, 9, 9, 10], [9, 8, 13, 20, 15], [6, 11, 18, 17, 13]])
    # box = Nms(boxes)
    #
    # print(box)
    # ConvertToSquare(boxes)
