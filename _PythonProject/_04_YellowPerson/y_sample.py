from PIL import Image, ImageDraw
import torch, cv2, os, numpy
from tqdm import tqdm

# 制作正负样本
# 测试正样本
def mk_sample():
    bg_pic = r"D:\2-Data\cartoon_face_img"
    yellow = r"D:\2-Data\yellow_pic\y_logo"
    data = r"D:\2-Data\yellow_pic\y_train_img"
    i = 1

    for fileName in tqdm(os.listdir(bg_pic),total=len(os.listdir(bg_pic))):
        bg_img = Image.open(f"{bg_pic}/{fileName}")
        #负样本
        bg_img = bg_img.resize((300, 300))
        # bg_img.save(f"{data}/{i}.0.0.0.0.0.jpg")

        # 正样本
        img_yellow = Image.open(f"{yellow}/{numpy.random.randint(1, 21)}.png")
        w = numpy.random.randint(100, 180)
        img_yellow = img_yellow.resize((w, w))
        x1, y1 = numpy.random.randint(0, 300 - w), numpy.random.randint(0, 300 - w)
        r, g, b, a = img_yellow.split()
        bg_img.paste(img_yellow, (x1, y1), mask=a)
        x2, y2 = x1 + w, y1 + w
        bg_img.save(f"{data}/{i}.{int(x1)}.{int(y1)}.{int(x2)}.{int(y2)}.1.png")

        i+=1
        if i == 50001:
            break


def reg():
    data = "./y_train_img"
    for fileName in os.listdir(data):
        fileName_list = fileName.split(".")

        if fileName_list[-2] == "1":
            file_name = f"{data}/{fileName}"
            img = Image.open(file_name)

            x1 = fileName_list[1]
            y1 = fileName_list[2]
            x2 = fileName_list[3]
            y2 = fileName_list[4]
            draw = ImageDraw.Draw(img)
            draw.rectangle((int(x1), int(y1), int(x2), int(y2)), outline="yellow", width=5)
            img.show()
            exit()


if __name__ == '__main__':
    # mk_sample()
    reg()
