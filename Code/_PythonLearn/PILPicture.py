
from PIL import Image, ImageFilter, ImageDraw, ImageFont  # PIL图片操作
import matplotlib.pyplot as plt  # 可以画图和展示图片
import random
import numpy as np
from mpl_toolkits.mplot3d import Axes3D  # 导入3d坐标系


# ff=gg=hh=3
# print(ff,gg,hh)

# img = Image.open(r"D:\1-Git\Code\_PythonProject\_04_YellowPerson\y_train_img\1.47.49.205.207.1.png")
# img.show() #操作系统查看图片
# plt.imshow(img)
# plt.title("haha")
# plt.show()

# w, h = img.size
# print(w, h)
# print(img.size) #元组形式返回
# bands = img.getbands()#获取通道
# print(bands)
# mode = img.mode
# print(mode)
# img = img.convert("1")
# img = img.convert("L")
# pixel = img.getpixel((100,100))#查看像素值
# print(pixel)
# img = img.convert("RGB")
# pixel = img.getpixel((100,100))
# print(pixel)

# 图片缩放，复制一份，不对原图操作
# img = img.resize((1600,866))#尺寸缩放图片
# img.show()

# 等比缩放图片，原图采样, res****抗锯齿，在原图上修改
# img.thumbnail((w // 2, h // 2),resample = Image.ANTIALIAS)
# img.show()

# 抠图
# img = img.crop((10,10,100,100)) #图片左上角和右下角的坐标
# img = img.crop((150,150,260,260))
# img.show()
# img.save("haha.jpg")#保存图像

# 旋转
# img = img.rotate(45) #从右到左，
# img = img.rotate(-90) #从右到左，超过180就用负数


# 粘贴（加logo）
# logo = Image.open("/Users/kabunchueng/Desktop/2-Cpp/1.png")
# logo = logo.resize((50, 50), resample=Image.ANTIALIAS)
# img.paste(logo,(200,200)) #粘贴，第二个属性是粘贴的位置

# 翻转
# img = img.transpose(Image.FLIP_LEFT_RIGHT)
# plt.imshow(img)
# img = img.transpose(Image.FLIP_TOP_BOTTOM)
# plt.imshow(img)
# plt.show()

# 画图：创建画笔 47.49.205.207
draw = ImageDraw.Draw(img)
# #矩形
# draw.rectangle((47,49,205,207),outline="yellow",width=3,fill="white")
# draw.rectangle((47,49,205,207),outline="yellow",width=3)
#圆
draw.ellipse(((200,200),(350,350)),outline="black",width=3 )
plt.imshow(img)
plt.axis(False)#隐藏坐标轴
plt.show()


# 滤波器
# img = img.filter(ImageFilter.CONTOUR) #素描效果
# img = img.filter(ImageFilter.BLUR) #模糊效果
# img = img.filter(ImageFilter.BoxBlur(radius=0)) #模糊效果,radius模糊程度
# img = img.filter(ImageFilter.DETAIL) #锐化
# img = img.filter(ImageFilter.EMBOSS) #浮雕
# img = img.filter(ImageFilter.EDGE_ENHANCE) #增强纹理

#提取 RGB通道的图像
# img_data = np.array(img)
# # img_data = img_data.transpose((1,0,2))#翻转
# print(img_data.shape)
# B_data = img_data[...,1]
# B_data = np.expand_dims(B_data ,axis=2)
# back_img = np.zeros((461, 820,1))
# B_img = np.concatenate((back_img,back_img,B_data),axis=2)
# B_img = np.array(B_img,dtype=np.uint8)
# # print(B_data.shape)
# print(B_img.shape)
# img = Image.fromarray(B_img)
# print(img.mode)
# img.show()

# ===========================================图像切分显示===================================
# def ImgCrop():
#     img = Image.open("/Users/carbenchueng/Desktop/1-Git/Code/_Image/1.jpg")
#     w,h = img.size
#     # print(w,h)
#     size_w = w//3
#     size_h = h//3
#     for i in range(3):
#         for j in range(3):
#             box = (size_w*j,size_h*i,size_w*(j+1),size_h*(i+1))
#             spl_img = img.crop(box)
#             spl_img.save(f"/Users/carbenchueng/Desktop/1-Git/Code/_Image/{999}{i}{j}.jpg")
#
# def ImgShow():
#     img_1 = Image.open("/Users/carbenchueng/Desktop/1-Git/Code/_Image/99900.jpg")
#     img_2 = Image.open("/Users/carbenchueng/Desktop/1-Git/Code/_Image/99901.jpg")
#     img_3 = Image.open("/Users/carbenchueng/Desktop/1-Git/Code/_Image/99902.jpg")
#     img_4 = Image.open("/Users/carbenchueng/Desktop/1-Git/Code/_Image/99910.jpg")
#     img_5 = Image.open("/Users/carbenchueng/Desktop/1-Git/Code/_Image/99911.jpg")
#     img_6 = Image.open("/Users/carbenchueng/Desktop/1-Git/Code/_Image/99912.jpg")
#     img_7 = Image.open("/Users/carbenchueng/Desktop/1-Git/Code/_Image/99920.jpg")
#     img_8 = Image.open("/Users/carbenchueng/Desktop/1-Git/Code/_Image/99921.jpg")
#     img_9 = Image.open("/Users/carbenchueng/Desktop/1-Git/Code/_Image/99922.jpg")
#     plt.subplot(3,3,1)
#     plt.title("01")
#     plt.axis(False)
#     plt.imshow(img_1)
#     plt.subplot(3,3,2)
#     plt.title("02")
#     plt.axis(False)
#     plt.imshow(img_2)
#     plt.subplot(3,3,3)
#     plt.title("03")
#     plt.axis(False)
#     plt.imshow(img_3)
#     plt.subplot(3,3,4)
#     plt.title("04")
#     plt.axis(False)
#     plt.imshow(img_4)
#     plt.subplot(3,3,5)
#     plt.title("05")
#     plt.axis(False)
#     plt.imshow(img_5)
#     plt.subplot(3,3,6)
#     plt.title("06")
#     plt.axis(False)
#     plt.imshow(img_6)
#     plt.subplot(3,3,7)
#     plt.title("07")
#     plt.axis(False)
#     plt.imshow(img_7)
#     plt.subplot(3,3,8)
#     plt.title("08")
#     plt.axis(False)
#     plt.imshow(img_8)
#     plt.subplot(3,3,9)
#     plt.title("09")
#     plt.axis(False)
#     plt.imshow(img_9)
#     plt.show()
#
# # ImgCrop()
# ImgShow()





# ===========================================3D画图===================================


# x = np.random.normal(0,1,100) #标准正态分布（均值，方差，采集数量）
# y = np.random.normal(0,1,100) #标准正态分布（均值，方差，采集数量）
# z = np.random.normal(0,1,100) #标准正态分布（均值，方差，采集数量）
#
# fig = plt.figure() #生成坐标系
# ax = Axes3D(fig)
# ax.scatter(x,y,z,c = "purple",marker="1")
# # plt.imshow(ax)
# plt.show()


# ===========================================实时画图===================================

# ax = []
# ay = []
#
# plt.ion()
# for i in range(100):
#     ax.append(i)
#     ay.append(i**2)
#
#     # 清除 clf清除当前画板内容，cla清除整个画板
#     plt.clf()
#     plt.plot(ax,ay,c = "pink")#画折线图
#     # plt.scatter(ax,ay) #画点
#
#     plt.pause(0.5)
# plt.ioff()
# plt.show()


# ===========================================实时画图===================================


# x = np.random.randn(20)
# a = np.random.randn(10)
# y = np.random.randn(20)
# b = np.random.randn(10)

# # 画点
# plt.scatter(x,y,c="green",marker="s",s=60,label="like")
# plt.scatter(a,b,c="red",marker="+",s=60,label="unlike")
# plt.legend()#显示图例
# plt.show()


# ================================生成验证码===============================================

# class GenerateCoder(object):
#
#     def get_text(self):
#         return chr(random.randint(65,90))
#     #生成随机前景色
#     def font_color(self):
#         return (random.randint(100,160),
#                 random.randint(100,160),
#                 random.randint(100,160))
#
#     #生成随机背景色
#     def back_color(self):
#         return (random.randint(1,60),
#                 random.randint(1,60),
#                 random.randint(1,60))
#
#     def encoder(self):
#         #创建画板
#         w,h = 240,60
#         panel = Image.new("RGB",(w,h),color=(255,255,255))
#         # panel =  Image.new("RGB",(w,h),color=(0,0,0))
#         draw = ImageDraw.Draw(panel)
#         #创建字体
#         font = ImageFont.truetype(font="Noteworthy.ttc",size=25)
#         #给画板上色
#         for y in range(h):
#             for x in range(w):
#                 draw.point((x,y),fill=self.back_color())
#
#         for i in range(4):
#             draw.text((60*i+20,8),text=self.get_text(),fill=self.font_color(),font=font)
#             # panel.save("code.jpg")
#         return panel
#
# gc = GenerateCoder()
# img = gc.encoder()
# plt.title("new_1")
# plt.imshow(img,cmap="Reds")
# plt.axis(False)#隐藏坐标轴
# plt.show()



