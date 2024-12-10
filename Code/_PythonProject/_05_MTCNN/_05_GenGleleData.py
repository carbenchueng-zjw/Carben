import os, numpy as np, traceback
import time

from _05_Utils import *
from PIL import Image
from tqdm import tqdm

anno_src = "D:/2-Data/Celeba/label.txt"
img_dir = "D:/2-Data/Celeba/sample"
save_path = "D:/2-Data/Celeba/data"

# anno_src = "D:/2-Data/Celeba/test/test_label.txt"
# img_dir = "D:/2-Data/Celeba/test/test_img"
# save_path = "D:/2-Data/Celeba/test/test_save"

# for face_size in tqdm([12, 24, 48],total=len([12, 24, 48])):
for face_size in [48]:
    print(face_size)
    positive_image_dir = f"{save_path}/{face_size}/positive"
    negative_image_dir = f"{save_path}/{face_size}/negative"
    part_image_dir = f"{save_path}/{face_size}/part"

    for dir_path in [positive_image_dir, negative_image_dir, part_image_dir]:
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

    positive_anno_filename = f"{save_path}/{face_size}/positive.txt"
    negative_anno_filename = f"{save_path}/{face_size}/negative.txt"
    part_anno_filename = f"{save_path}/{face_size}/part.txt"
    #
    positive_count = 0
    negative_count = 0
    part_count = 0

    try:
        positive_anno_file = open(positive_anno_filename, "w")
        negative_anno_file = open(negative_anno_filename, "w")
        part_anno_file = open(part_anno_filename, "w")
        # print(len(open(anno_src).readlines()))
        # exit()

        for i, line in tqdm(enumerate(open(anno_src), 1), total=len(open(anno_src).readlines())):
            strs = line.split()
            # print(strs)
            # exit()
            img_file_name = strs[0]
            img_file = f"{img_dir}/{img_file_name}"
            # print(img_file)
            # exit()
            with Image.open(img_file) as img:  # 打开图片文件
                img_w, img_h = img.size
                x1 = float(strs[1])
                x2 = float(strs[3])
                y1 = float(strs[2])
                y2 = float(strs[4])
                w = x2 - x1
                h = y2 - y1
                # print(w,h)
                if max(w, h) < 40 or x1 < 0 or y1 < 0 or w < 0 or h < 0:
                    continue

                boxes = [[x1, y1, x2, y2]]
                cx = x1 + w / 2
                cy = y1 + h / 2

                # 生成正样本，部分样本
                for _ in range(6):
                    w_ = np.random.randint(-w * 0.2, w * 0.2)
                    h_ = np.random.randint(-h * 0.2, h * 0.2)
                    cx_ = cx + w_
                    cy_ = cy + h_

                    side_len = np.random.randint(int(min(w, h) * 0.8), np.ceil(1.2 * max(w, h)))
                    x1_ = np.max(cx_ - side_len / 2, 0)
                    y1_ = np.max(cy_ - side_len / 2, 0)
                    x2_ = x1_ + side_len
                    y2_ = y1_ + side_len
                    #
                    crop_box = np.array([x1_, y1_, x2_, y2_])
                    offset_x1 = (x1 - x1_) / side_len
                    offset_y1 = (y1 - y1_) / side_len
                    offset_x2 = (x2 - x2_) / side_len
                    offset_y2 = (y2 - y2_) / side_len
                    face_crop = img.crop(crop_box)
                    face_resize = face_crop.resize((face_size, face_size), Image.Resampling.LANCZOS)
                    #
                    iou = IouPro(crop_box, np.array(boxes))[0]
                    if iou > 0.55:
                        positive_anno_file.write(
                            f"positive/{positive_count}.jpg 1 {offset_x1} {offset_y1} {offset_x2} {offset_y2}\n"
                        )
                        positive_anno_file.flush()
                        face_resize.save(f"{positive_image_dir}/{positive_count}.jpg")
                        positive_count += 1

                    elif iou > 0.25:
                        part_anno_file.write(
                            f"part/{part_count}.jpg 2 {offset_x1} {offset_y1} {offset_x2} {offset_y2}\n"
                        )
                        part_anno_file.flush()
                        face_resize.save(f"{part_image_dir}/{part_count}.jpg")
                        # print(part_image_dir)
                        part_count += 1

                # 生成负样本
                _boxes = np.array(boxes)
                if min(img_w, img_h) / 2 < 100 :
                    continue
                for _i in range(6):

                    side_len = np.random.randint(face_size, min(img_w, img_h) / 2)
                    x_ = np.random.randint(0, img_w - side_len)
                    y_ = np.random.randint(0, img_h - side_len)
                    crop_box = np.array([x_, y_, x_ + side_len, y_ + side_len])
                    # print(crop_box)
                    # exit()

                    if np.max(IouPro(crop_box, _boxes)) < 0.08:  # 在加IOU进行判断：保留小于0.3的那一部分；原为0.3
                        face_crop = img.crop(crop_box)  # 抠图
                        face_resize = face_crop.resize((face_size, face_size), Image.Resampling.LANCZOS)  # LANCZOS：平滑,抗锯齿

                        negative_anno_file.flush()
                        negative_anno_file.write(f"negative/{negative_count}.jpg 0 0 0 0 0\n")
                        face_resize.save(f"{negative_image_dir}/{negative_count}.jpg")
                        negative_count += 1

    except Exception as e:
        print("产生异常 :", e)
        with open("Erro.txt", "a+") as ff:
            ff.write(str(e))
