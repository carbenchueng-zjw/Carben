import os, random, thop, json, time, cv2
import numpy as np, torch
import torchvision, numpy, matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFilter, ImageFont
from torchvision import models, transforms
from mpl_toolkits.mplot3d import Axes3D
from tqdm import tqdm


# torch.set_default_tensor_type(torch.DoubleTensor)
# e = [[1,2],[3,4]]
# a = torch.tensor((2,2,2),dtype=torch.float32,requires_grad=True)
# b = torch.rand(3,2)
# print(a.dtype,b.dtype,type(e))
# print(torch.tensor(e),b,b.mean(),sep="\n")
# a = torch.arange(6.0).reshape(2,3)
# b = torch.linspace(0,10,6).reshape(2,3)
# f = torch.stack((a,b),dim=1)
# print(torch.gt(a,b))
# print(torch.lt(a,b))
# print(torch.pow(a,2)) #幂运算
# print(torch.log(a)) #指数运算
# print(a.T)
# print(a,b,f,sep="\n")



# torch   numpy互相转换
# a = torch.tensor([1,2,3])
# b = numpy.array([1,2,3])
# c = a.numpy()
# e = torch.from_numpy(b)
# print(type(a),type(b),type(c),type(e))
# print(a.dtype,b.dtype,c.dtype,e.dtype)
# b.astype(numpy.float32())
# numpy.save("asd",b)#二进制形式保存
# numpy.load("asd.npy")#读取
# print(b)
# b = numpy.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]],[[7,8,9],[10,11,12]]])
# print(b.shape)
# b = b.reshape((2,9,1,1))
# print(b)
# print(b.ndim)

# 广播:
# a1 = np.arange(24).reshape((4,6))
# a2 = np.arange(24).reshape((4,2,3))
# a = np.arange(6).reshape((2,3))
# # a = a.astype(np.int8)
# b = np.array([11,12,13,14,15,16,17,18],dtype=np.float64)
# f = np.array([[1,2,6,3], [3,3,2,1], [5,6,1,2]])
# c = np.arange(6).reshape((3,2,1,1))#reshape(-1,2),，-1就是让程序自己计算剩下的纬度
# d = np.full((2,3,4),fill_value=2,dtype=np.float64)
# g = np.eye(4,4)#单位矩阵
# o = np.empty((2,3)) #随机初始化的空矩阵
# h = np.tri(5)#下三角
# # j = np.tril(a)#下三角
# # i = np.triu(a)#上三角
# k = np.arange(24).reshape((2,3,4))
# l = np.transpose(k,(2,0,1))
# l = np.swapaxes(k,2,0)#只能换2个轴

# print(a.ndim,a.size,a.shape,a.dtype,sep="\n")
# print(f.ndim,f.size,f.shape,sep="\n")
# print(b.dtype)
# print(a.dot(g))
# print(k.shape)
# print(l.shape)
# print(k)
# print(k[[0,1],[1,2],[1,3]])
# print(a1[0:1,3:])
# print(a1[:,0])
# print(a1[:,[1,3]])
# print(a[:,[0,2]])
# print(a1[:,3:])
# aa = a1[:,3:].reshape(-1)
# print(aa[[1,5,7,11]])
# b1 = np.array([[True,False,False,True],[True,True,False,False]])
a3 = np.arange(8).reshape((2,4))
# print(a2[...,2])
# print(a2[a2>10])
print(a3)
print(np.where(a3>3)) #满足条件变成100，否则为零
# print(np.argwhere(a>1)) #查找大于1的元素的下标

# a = np.array([[1, 2], [2, 4], [2, 4]])
# b = np.array([[5, 5], [4, 2], [4, 2]])
# print(np.concatenate([a, b], axis=0))#再第0纬度拼接，也就是在行上做加法
# print(np.concatenate([a, b], axis=1))#再第0纬度拼接，也就是在行上做加法


# for i in tqdm(range(30)):
#     time.sleep(0.5)
#     print(i)


# b= numpy.array([[5,3,2],[1,1,1]],dtype=numpy.float64)
# a = numpy.arange(24).reshape(2,3,4)#起始，结尾，步数
# print(numpy.linalg.matrix_rank(a))#求秩
# a = a.astype(numpy.int32)
# print(a)
# print(a.ndim)
# print(a.shape)
# print(a.dtype)
# a = a.reshape(-1,2)
# print(a)
# print(a.shape)
# a = numpy.zeros((2,3))#元足要加括号
# print(a)
# print(a.dtype)
# c = numpy.full((2,3),fill_value=3)
# c = numpy.empty((2,3))#随机初始化，如果没有被初始化过，那么就会默认为0
# print(c)
# e = numpy.eye(3,3)#对角矩阵
# e = numpy.arange(9).reshape(3,3)
# print(e)

# # b = numpy.triu(e)#上三角矩阵
# b = numpy.tril(e)#下三角矩阵
# print(b.T)#倒叙换轴
# c = numpy.arange(24).reshape(2,3,1,4)
# # b = numpy.swapaxes(c,1,2)#只能换2个轴，一般不用
# b = numpy.transpose(c,(0,2,3,1))
# # print(numpy.tri(3))
# print(b.shape)

# a = numpy.arange(24).reshape(2,3,4)
# a = numpy.arange(6).reshape(2,3)
# a = numpy.arange(6)
# print(a[[0,1],[2,2]])
# print(a[[1,2,3]])

# a = numpy.arange(24).reshape(4,6)
# print(a[0][3:])
# print(a[0:1,3:6])#不降纬
# print(a[0:1][3:6])#
# print(a[:,[2,5]])#
# print(a[:,3:6],[[]])#

# a = numpy.arange(24).reshape(4,2,3)
# print(a[...])#a[:,;]
# print(a[...,0])

# a = numpy.arange(6).reshape(2,3)
# print(a)
# # a = numpy.where(a>4,255,0)#满足条件赋值成255，不然就赋值成0
# b = numpy.argwhere(a>3)#返回满足条件的索引
# c = numpy.where(a>2)
# print(c)
# print(b)

# a= numpy.array([[1,2,3],[4,5,6]])
# b= numpy.array([[3,3,3],[5,5,5]])
# print(numpy.concatenate([a,b],axis=1))


# a= numpy.array([1,2,3])
# print(numpy.add(a,3))  #加法
# print(numpy.subtract(a,3))  #减法
# print(numpy.multiply(a,3))  #乘法
# print(numpy.true_divide(a,3))   #除法（保持纬度）
# print(numpy.divide(a,3))   #除法（影响纬度）

# print("逻辑运算")
# a = numpy.array([True,False,False])
# b = numpy.array([False,True,False])
# print(numpy.logical_and(a,b))#  与
# print(numpy.logical_or(a,b))#   或
# print(numpy.logical_not(a))#  非
# print(numpy.logical_xor(a,b))# 相同为假，不同为真

# a= numpy.array([[1,2,3],[4,5,6]])
# print(a.sum())
# print(a.sum(axis=0))
# print(a.mean(axis=0))#平均
# print(a.std())#标准差
# print(a.var(axis=0))#方差，衡量数据的离散程度
# print(a.max(axis=0))
# print(a.argmax(axis=1))#返回最大值的索引
# print(a.argmax())#返回最大值的索引


# print("线性代数")
# a = numpy.array([3,-2,0,1])
# c = numpy.array([[1,2],[3,4]])
# b = numpy.linalg.norm(a,ord=0)#求范数,默认二范数
# print(b)
# print(numpy.linalg.inv(a))#求逆

# print("随机数")
# a = numpy.random.randn(3,3,3)#标准正态分布去随机数
# print(a.shape)
# a = numpy.random.normal(size = (3,3,3))#正态分布去随机数
# print(a.shape)
# print(a)
# a = numpy.random.rand(2,3)#0-1的随机数
# print(a)
# a = numpy.random.randint(2,8,size=(3,3))#随机数整
# print(a)

# print("降/升纬")
# a = numpy.arange(6).reshape((1,2,3,1))
# a = numpy.arange(6).reshape(2,3)
# b = numpy.expand_dims(a,axis=2)#只能升1纬度
# print(b.shape)
# print(a)
# a = numpy.squeeze(a)#只能降1的纬度
# print(a.shape)

# print("i/o操作")  读写操作
# a = numpy.arange(24).reshape(4,6)
# numpy.save("arrA.npy",a)
# b = numpy.load("arrA.npy")
# print(b)

# print("矩阵乘法")
# a = numpy.array([[1,2],[3,4]])
# b = numpy.array([[0,2],[3,3]])
# print(a*b)#对应位置相乘
# print(a@b)#第一个的行乘以第二个的列（1,2 * 0,3）(1,2 *2,3) (3,4 * 0,3) (3,4 *2,3)
# print(a.dot(b))

# 广播
# a = numpy.array([1,2,3])
# b = numpy.arange(6).reshape(2,3)
# c = numpy.array([[2],[1]])
# print(b+a)
# a = numpy.tile(a,(2,1))
# d = numpy.tile(c,(1,4))#手动广播
# print(a)
# print(d)

# 图像
# a = Image.open(r"/Users/kabun/Desktop/11.jpg")
# # a.show()
# w,h = a.size
# # print(w,h)
# pixel = a.getpixel((100,100))
# print(pixel)
# # print(a.getbands())
# # print(a.mode)
# a  = a.convert("L")#转换模式
# pixel = a.getpixel((100,100))
# print(pixel)
# print(a.mode)

# 图像缩放
# a = Image.open("11.jpg")
# b = Image.open("1.png")
# a = a.resize((200,200))
# a.show()
# a.save("xxxxx")
# a = a.crop((55,55,100,100)) #抠图
# a.show()
# a = a.rotate(-45)#旋转 默认逆时针旋转
# a.show()
# a.paste(b) #粘贴
# a.show()
# a = a.transpose(Image.FLIP_LEFT_RIGHT)#翻转
# a.show()
# 画图
# draw = ImageDraw.Draw(a)
# draw.rectangle((100,100,200,200),outline="black",width=1)
# draw.ellipse(((200,200),(250,250)),fill="green",width=3,outline="red")
# a.show()

# 滤波器
# a = a.filter(ImageFilter.CONTOUR)
# a = a.filter(ImageFilter.EMBOSS)
# a = a.filter(ImageFilter.BuiltinFilter)
# a.show()

# PIL 矩阵操作查看图片的rgb
# backImg = numpy.zeros((461,820,1))
# a = numpy.array(a)
# print(a.shape)
# b_data = a[...,2]
# b_data = numpy.expand_dims(b_data,axis=2)
# print(b_data.shape)
# a = a.transpose((1,0,2))
# print(backImg.shape)
# b_img = numpy.concatenate((backImg,backImg,b_data),axis=2)
# print(b_img.dtype)
# b_img = numpy.array(b_img,dtype=numpy.uint8)
# a = Image.fromarray(b_img)
# print(a.mode)
# a.show()

# 生成验证码
# class GenrateCoder():
#     #生成字母
#     def get_text(self):
#         return chr(random.randint(65,90))
#     #生成前景色
#     def font_color(self):
#         return (random.randint(0,150),
#                 random.randint(0,150),
#                 random.randint(0,150))
#         #生成后景色
#     def back_color(self):
#         return (random.randint(150,255),
#                 random.randint(150,255),
#                 random.randint(150,255))
#     def write(self):
#         w,h = 240,60
#         panel = Image.new(size=(w,h),color=(255,255,255),mode="RGB")
#         draw = ImageDraw.Draw(panel)
#         #创建字体
#         font = ImageFont.truetype(font=r"/System/Library/Fonts/STHeiti Medium.ttc",size=30)
#         #给画板上色
#         for y in range(h):
#             for x in range(w):
#                 draw.point((x,y),fill=self.back_color())
#         #写内容
#         for i in range(4):
#             draw.text((60*i+20,15),text=self.get_text(),fill=self.font_color(),font=font)
#
#         return panel
# if __name__ == '__main__':
#     gc = GenrateCoder()
#     img = gc.write()
#     # img.save(r"/Users/kabun/Desktop/2-data/code/test.jpg")
#     img.show()

# img = Image.open(r"/Users/kabun/Desktop/11.jpg")
# # plt.imshow(img)
# # plt.show()
# a = []
# b = []
# plt.ion()
# for i in range(100):
#     a.append(i**2)
#     b.append(i)
#     plt.cla()
#     plt.plot(b,a)
#     plt.pause(0.2)
# plt.ioff()
# plt.show()

# x= numpy.random.randn(20)
# y= numpy.random.randn(20)
# plt.scatter(x,y,label = "like",c="blue",marker="D")
# f1= numpy.random.randn(10)
# f2= numpy.random.randn(10)
# plt.scatter(f1,f2,label = "dislike",c="red",marker="D")
# plt.legend()#展示图例
# plt.show()

# x= numpy.random.normal(0,1,100)
# y= numpy.random.normal(0,1,100)
# z= numpy.random.normal(0,1,100)
# fig = plt.figure()#创建画布
# ax = Axes3D(fig)#放到三维坐标
# ax.scatter(x,y,z,marker="D")
# plt.show()

# img = Image.open(r"/Users/kabun/Desktop/11.jpg")
# img = img.resize((820,460))
# # img.show()
# img_data = numpy.array(img)
# print(img_data.shape)
# h,w,c = img_data.shape
# img_data = img_data.reshape((2,h//2,2,w//2,c))
# print(img_data.shape)
# img_data = numpy.transpose(img_data,(0,2,1,3,4))
# print(img_data.shape)
# img_data = img_data.reshape(-1,230,410,c)
# img_data1 = img_data[0]
# img_data2 = img_data[1]
# img_data3 = img_data[2]
# img_data4 = img_data[3]
# #
# img1 = Image.fromarray(img_data1,"RGB")
# img2 = Image.fromarray(img_data2,"RGB")
# img3 = Image.fromarray(img_data3,"RGB")
# img4 = Image.fromarray(img_data4,"RGB")
# img1.show()
# img2.show()
# img3.show()
# img4.show()

# imgos = os.listdir("/Users/kabunchueng/Desktop/3-data/yellow_pic")
# print(imgos)
# plt.ion()
# for i in imgos:
#     img_path = os.path.join("/Users/kabunchueng/Desktop/3-data/yellow_pic",i)
#     img = Image.open(img_path)
#     plt.clf()
#     plt.imshow(img)
#     plt.axis(False)
#     plt.pause(1)
# plt.ioff()


#
# img = cv2.imread("/Users/kabun/Desktop/1.jpeg",0)
# cv2.imshow("asd",img)
# cv2.waitKey(0)

# cap = cv2.VideoCapture(0)
# while True:
#     ret,fa = cap.read()
#     cv2.imshow("asd",fa)
#     if cv2.waitKey(41) & 0xff == ord("q"):
#         break
#
# cap.release()
# cv2.destroyWindow()

# 直方图
# img = cv2.imread("11.jpg")
# img1 = cv2.imread("11.jpg",0)
# dst = cv2.equalizeHist(img1,)
# cv2.imshow("asd",dst)
# cv2.waitKey(0)
# img_b = cv2.calcHist([img],[0],None,[256],[0,256])
# plt.plot(img_b,label="B",color="b")
# img_g = cv2.calcHist([img],[1],None,[256],[0,256])
# plt.plot(img_g,label="G",color="g")
# img_r = cv2.calcHist([img],[2],None,[256],[0,256])
# plt.plot(img_r,label="R",color="r")
# plt.show()
# 自适应均衡化
# cclahe = cv2.createCLAHE(clipLimit=2.0,tileGridSize=(7,7))
# sdt2 = cclahe.apply(img1)
# his1 = cv2.calcHist([img1],[0],None,[256],[0,256])
# cv2.imshow("asd",sdt2)
# cv2.waitKey(0)

# canny算法，边缘提取
# img = cv2.GaussianBlur(img,(3,3),0)
# canny = cv2.Canny(img,80,150)
# #高亮处理
# img = cv2.convertScaleAbs(img1,alpha=3,beta=0)
# cv2.imshow("asd",canny)
# cv2.imshow("1sd",img)
# cv2.waitKey(0)

# 轮廓绘制
# img = cv2.imread("16.jpg")
# imggary = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# ret ,thre = cv2.threshold(imggary,0,255,0|cv2.THRESH_OTSU)
# contours,image= cv2.findContours(thre,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
# # print(contours)
# img_con = cv2.drawContours(img,contours,-1,(0,255,0),-1)
# cv2.imshow("1sd",img_con)
# # cv2.imshow("2sd",img)
# cv2.waitKey(0)

# 求衷心，周长，面积
# img = cv2.imread("16.jpg")
# imggary = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# ret,thr = cv2.threshold(imggary,127,255,0)#二值化
# cons,_= cv2.findContours(thr,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
# M = cv2.moments(cons[0]) #求矩
# cx,cy = int(M["m10"]/M["m00"]),int(M["01"]/M["m00"])
# print("重心",cx,cy)
# area = cv2.contourArea(cons[0])
# print("面积",area)
# perimrter = cv2.arcLength(cons[0],True)
# print("周长",perimrter)
# 轮廓近似
# approx = cv2.approxPolyDP(cons[0],13,True)
# 凸包曲线
# hull = cv2.convexHull(cons[0])
# print(cv2.isContourConvex(cons[0]),cv2.isContourConvex(hull))
# img_con = cv2.drawContours(img,[hull],-1,(255,0,0),3)
# 边界检测
# x,y,w,h = cv2.boundingRect(cons[0])
# img_con = cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
# #最小矩形
# rect = cv2.minAreaRect(cons[0])
# box = cv2.boxPoints(rect)
# box = numpy.int0(box)#int0 是直接去掉，不是四舍五入
# img_con = cv2.drawContours(img,[box],-1,(255,0,0),3)
# 最小外切圆
# (x,y),radius = cv2.minEnclosingCircle(cons[0])
# center = (int(x),int(y))
# radius = int(radius)
# img_con = cv2.circle(img,center,radius,(0,255,0),2)
# cv2.imshow("asd",img_con)
# cv2.waitKey(0)

# 霍夫变换 用来检测任意能够用数学公式表达的形状
# src = cv2.imread("33.jpg")
# img = cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)
# img = cv2.Canny(img,50,150)
# lines = cv2.HoughLinesP(img,1.0,numpy.pi/180,10)
# lines = numpy.squeeze(lines)
# print(lines)
# for x1,y1,x2,y2 in lines:
#     cv2.line(src,(x1,y1),(x2,y2),(0,0,255),2)
# cv2.imshow("asd",src)
# cv2.waitKey(0)


# #车牌检测
# rawimg = cv2.imread("23.jpg")
# imgaus = cv2.GaussianBlur(rawimg,(3,3),0)
# imggary = cv2.cvtColor(imgaus,cv2.COLOR_BGR2GRAY)
# sobel_x = cv2.Sobel(imggary,cv2.CV_16S,1,0)
# # sobel_y = cv2.Sobel(imggary,cv2.CV_16S,0,1)
# # 转回uint8
# absx = cv2.convertScaleAbs(sobel_x)#默认就是uint8
# # absy = cv2.convertScaleAbs(sobel_y)#默认就是uint8
# image = absx
# #二值化
# ret,img = cv2.threshold(image,0,255,cv2.THRESH_BINARY|cv2.THRESH_OTSU)
# #闭操作：可以让目标区域连成一块，便于后续的轮廓提取
# kernelx = cv2.getStructuringElement(cv2.MORPH_RECT,(17,5))
# image1 = cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernelx)
# #形态学操作进去去燥
# kernelx = cv2.getStructuringElement(cv2.MORPH_RECT,(20,1))
# kernely = cv2.getStructuringElement(cv2.MORPH_RECT,(1,20))
# image = cv2.dilate(image1,kernelx)
# image = cv2.erode(image,kernelx)
# image = cv2.erode(image,kernely)
# image = cv2.dilate(image,kernely)
# #平滑处理
# image = cv2.medianBlur(image,19)
# #查找轮廓
# cons,_ = cv2.findContours(image,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
# for i in cons:
#     rect = cv2.boundingRect(i)
#     x = rect[0]
#     y = rect[1]
#     w = rect[2]
#     h = rect[3]
#     if w>(3*h):
#         img = rawimg[y:y+h,x:x+w]
#         cv2.imshow("aw",img)
#         # cv2.waitKey(0)
# #绘制轮廓
# image = cv2.drawContours(rawimg,cons,-1,(0,0,255),3)
# cv2.imshow("asd1",image)
# # cv2.imshow("asd2",image1)
# cv2.waitKey(0)

# conv_img = torch.randn(1,1,9,9)
# advp = torch.nn.AdaptiveAvgPool2d((3,5))#自适应最大池化
# out = advp(conv_img)
# print(out.shape)

# class Net1(torch.nn.Module):
#     def __init__(self):
#         super(Net1, self).__init__()
#         self.layers = torch.nn.Sequential(
#             torch.nn.Conv2d(3,16,3,1)
#         )
#     def forward(self,x):
#         return self.layers(x)
# net = Net1()
# x = torch.randn(1,3,16,16)
# flops,params = thop.profile(net,(x,))
# print(flops,params)

# a = torch.Tensor([0.8,0.6,0.3,0.2])
# out = torch.where(a>0.5,1,0)
# print(out)

# img_dir = r"/Users/kabun/Desktop/3-Data/Celeba/sample"
# path = "/Users/kabun/Desktop/3-Data/Celeba/test_zuobiao/12"
# path = "/Users/kabun/Desktop/3-Data/Celeba/all"
# for i in tqdm(range(len(os.listdir(path)))):
# new_path = os.path.join(path,os.listdir(path)[i])
# print(new_path)
# print(os.listdir(path))

# with open("/Users/kabun/Desktop/3-Data/Celeba/all/handlabel_14/139427.json","r+",encoding="utf-8") as t:
#     with open(new_path,"r+",encoding="utf-8") as t:
#         data = json.load(t)
#         x1 = float(data["outputs"]["object"][0]["bndbox"]["xmin"])
#         y1 = float(data["outputs"]["object"][0]["bndbox"]["ymin"])
#         x2 = float(data["outputs"]["object"][0]["bndbox"]["xmax"])
#         y2 = float(data["outputs"]["object"][0]["bndbox"]["ymax"])
#         print(x1,y1,x2,y2)

# t.seek(0)
# json.dump(data,t,ensure_ascii=False)
# t.truncate()
#     img = Image.open(data["path"])
#     draw = ImageDraw.Draw(img)
#     # draw.rectangle((80,120,190,248),outline="red",width=3)
#     draw.rectangle((x1,y1,x2,y2),outline="red",width=3)
#     img.show()


# hh = os.listdir(r"/Users/kabun/Desktop/3-Data/Celeba/all")
# # os
# print(hh)

# {"name": "人脸", "bndbox": {"xmin": 80, "ymin": 120, "xmax": 190, "ymax": 248}}


# def iou(box,boxes,isMin = False):
#     #计算面积
#     box_area = (box[2] - box[0]) * (box[3] - box[1])
#     area = (boxes[:,2]-boxes[:,0]) * (boxes[:,3]-boxes[:,1])
#     # print(boxes[:,2])
#
#     #交集
#     xx1 = np.maximum(box[0],boxes[:,0])
#     xx2 = np.maximum(box[2],boxes[:,2])
#     yy1 = np.minimum(box[1],boxes[:,1])
#     yy2 = np.minimum(box[3],boxes[:,3])
#     # print(np.maximum(box[0])
#     # print(xx1)
#
#     #判断是否有交集
#     w = np.maximum(0,xx2-xx1)
#     h = np.maximum(0,yy2-yy1)
#     #交集面积
#     inter = w*h
#     if isMin:
#         ovr = np.true_divide(inter,np.minimum(box_area,area))
#     else:
#         ovr = np.true_divide(inter,(box_area+area-inter))
#     return ovr
#
# def nms(boxes,thresh=0.3,isMin=False):
#     if boxes.shape[0] ==0:
#         return np.array([])
#     #根据置信度对框进行排序
#     _boxes = boxes[(-boxes[:,4]).argsort()]
#     r_boxes = []
#     while _boxes.shape[0] >1:
#         a_box = _boxes[0]
#         print(a_box)
#         b_boxes = _boxes[1:]
#         r_boxes.append(a_box)
#         index = np.where(iou(a_box,b_boxes,isMin) < thresh)
#         _boxes =  b_boxes[index]
#     if _boxes.shape[0]>0:
#         r_boxes.append(_boxes[0])
#     return np.stack(r_boxes)

# if __name__ == '__main__':
# a = np.array([1,1,11,11])
# bs = np.array([[1,1,10,10],[11,11,20,20]])
# print(iou(a,bs))
# b = np.array([[5,3],[3,2],[1,6]])
# index = b[:,1].argsort()
# print(b[index])


# bs = np.array([[1, 1, 10, 10, 40], [1, 1, 9, 9, 10], [9, 8, 13, 20, 15], [6, 11, 18, 17, 13]])
# print(bs[:,3].argsort())
# print(nms(bs))

# a = np.array([9, 8, 13, 20, 15])
# aa = np.array([1, 1, 10, 10, 40])
# aa = np.array([[1, 1, 10, 10, 40], [1, 1, 9, 9, 10],[6, 11, 18, 17, 13]])
# print(numpy.maximum(a[2],aa[2]))

# a = torch.tensor([1,2,3,4,5])
# print(torch.lt(a,4))
# print(torch.masked_select(a,torch.lt(a,4)))

# cls = torch.arange(12).reshape(1,1,3,4)
# print(cls[0][0].shape)
# print(cls[0].shape)

# _cls = torch.randn(1,1,9,12)
# cls = _cls[0][0]
# mask = torch.gt(cls,0.6)
# print(mask)
# idxs = torch.nonzero(mask)
# print(idxs.shape)

# aa = os.listdir(r"/Users/kabun/Desktop/test_img")
# print(aa)

# conv1 = torch.nn.Conv2d(4,8,3,1)
# conv2 = torch.nn.Conv2d(4,8,3,1,groups=2)
#
# x = torch.randn(1,4,112,112)
#
# out_1 = conv1(x)
# out_2 = conv2(x)
# print(conv1.weight.shape,conv2.weight.shape)


# u, s, v = np.linalg.svd(f)
# print(u, s, v, sep="\n")
#
# d = np.array([[1, 2], [3, 3], [5, 6]])
# u, s, v = np.linalg.svd(d)
# print(u, s, v, sep="\n")
