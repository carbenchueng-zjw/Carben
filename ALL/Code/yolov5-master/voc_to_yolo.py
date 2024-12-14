# _*_ coding: utf-8 _*_
import xml.etree.ElementTree as ET, os

from torchvision.datasets.utils import list_files
from tqdm import tqdm
from os import getcwd

sets = ["train", "test", "val"]
# 这里要使用自己的类别
classes = ["aeroplane", "bicycle", "bird", "boat", "bottle", "bus", "car", "cat", "chair",
           "cow", "diningtable", "dog", "horse", "motorbike", "person", "pottedplant",
           "sheep", "sofa", "train", "tv/monitor"]


def convert(size, box):
    dw = 1. / (size[0])
    dh = 1. / (size[1])
    x = (box[0] + box[1]) / 2.0 - 1
    y = (box[2] + box[3]) / 2.0 - 1
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    x = round(x, 6)
    w = round(w, 6)
    y = round(y, 6)
    h = round(h, 6)
    return x, y, w, h


# 后面只用修改各个文件夹的位置
def convert_annotation(image_id):
    in_file = open(f"D:/2-Data/VOCtrainval_06-Nov-2007/VOCdevkit/VOC2007/Annotations/{image_id}.xml", encoding="utf-8")
    out_file = open(f"D:/2-Data/VOCtrainval_06-Nov-2007/VOCdevkit/VOC2007/labels/{image_id}.txt", "w",
                    encoding="utf-8")
    tree = ET.parse(in_file)
    root = tree.getroot()
    size = root.find("size")

    w = int(size.find("width").text)
    h = int(size.find("height").text)
    # print(h)
    # exit()
    for obj in root.iter("object"):
        difficult = obj.find("difficult").text
        cls = obj.find("name").text
        if cls not in classes or int(difficult) == 1:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find("bndbox")
        b = (float(xmlbox.find("xmin").text), float(xmlbox.find("xmax").text),
             float(xmlbox.find("ymin").text), float(xmlbox.find("ymax").text))
        b1, b2, b3, b4 = b
        if b2 > w:
            b2 = w
        if b4 > h:
            b4 = h
        b = (b1, b2, b3, b4)
        bb = convert((w, h), b)
        out_file.write(str(cls_id) + " " +
                       " ".join([str(a) for a in bb]) + "\n")


# 这一步生成的TXT文件写在data.yaml文件里
wd = getcwd()
for image_set in sets:
    if not os.path.exists(r"D:\2-Data\VOCtrainval_06-Nov-2007\VOCdevkit\VOC2007\labels"):
        os.makedirs(r"D:\2-Data\VOCtrainval_06-Nov-2007\VOCdevkit\VOC2007\labels")
    image_ids = open(f"D:/2-Data/VOCtrainval_06-Nov-2007/VOCdevkit/VOC2007/ImageSets/{image_set}.txt"
                     ).read().strip().split()
    list_file = open(f"D:/2-Data/VOCtrainval_06-Nov-2007/VOCdevkit/VOC2007/{image_set}.txt", "w")
    for image_id in tqdm(image_ids):
        list_file.write(f"D:/2-Data/VOCtrainval_06-Nov-2007/VOCdevkit/VOC2007/JPEGImages/{image_id}.jpg\n")
        convert_annotation(image_id)
    list_file.close()
print("success")
