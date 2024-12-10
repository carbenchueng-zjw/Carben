import time
import cv2
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


# =====================================看图===========================================
# 读取图片
# img = cv2.imread("Image/handsome.jpg",0)#代表灰度图
# img = Image.fromarray(img)#因为经过cv2，所以图片颜色有问题OPENCV变成BGR
# img = img[...,::-1]#变回rgb
# cv2.imshow("pic show",img)#使用opencv自带的窗口
#
# 显示图片，是个非阻塞方法 “窗口名字”,需要展示的内容
# cv2.waitKey(0)#0是死循环，里面单位是毫秒
# cv2.destroyAllWindows()#摧毁所有窗口


# =====================================画图===========================================
# img = np.random.randint(0,255,(200,300,3),np.uint8)
# img = np.zeros((200,300,3),np.uint8)
# img[:,:,2] = 255
# img[...,1] = 255
# cv2.imwrite("img_save.jpg",img)#保存图片
#
# cv2.imshow("s",img)
# cv2.waitKey(0)

# =====================================视频，摄像头===========================================

# cap = cv2.VideoCapture("http://ivi.bupt.edu.cn/hls/cctv1hd.m3u8")#可以读取视频，网络视频（视频格式有要求），数字0不带引号表示摄像头
# cap = cv2.VideoCapture(0)#可以读取视频，网络视频（视频格式有要求），数字0不带引号表示摄像头
# cap = cv2.VideoCapture("D:/2-Data/yolov3训练数据-金鱼/20221111_145850.mp4")#0：前置摄像头，1：后置摄像头
# i=0
# try:
#     while cap.isOpened():
#
#         ret,frame = cap.read()#ret返回bool值，判断是否读取成功，frame就是读取到的每一帧画面
#
#         key = cv2.waitKey(25)
#         if key == ord("q"):
#             break
#         cv2.imshow("frame",frame)
#     cap.release()
#     cv2.destroyAllWindows()#关闭窗口
#
# except Exception as e:
#     print(e)


# lt = time.localtime()
# print(lt[5])

# t1 = time.time()
# print(time.strftime("%Y年-%m月-%d日 %H时%M分%S秒"))
# time.sleep(2)
# print(time.ctime())
# t2 = time.time()
# print(f"执行了{(t2-t1)}秒")
# print(lt)

# =====================================色彩转换===========================================

# src = cv2.imread("../Image/paint.jpg")
# dst = cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)
# ppp = cv2.cvtColor(src,cv2.COLOR_BGR2RGB)
# img = Image.fromarray(ppp,"RGB")
# img.show()
#
# cv2.imshow("src show",src)
# cv2.imshow("dst show",dst)
# cv2.waitKey(0)

# hsv
# src = cv2.imread("a.jpg")
# dst = cv2.cvtColor(src,cv2.COLOR_BGR2HSV)
#
#
# cv2.imshow("src show",src)
# cv2.imshow("dst show",dst)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# =====================================抠图===========================================
# img = cv2.imread("../Image/4.jpg")
# hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
# lower = np.array([1,110,100])
# upper = np.array([200,255,200])
# mask = cv2.inRange(hsv,lower,upper)
#
# cv2.imshow("ha",img)
# cv2.imshow("hw",mask)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# =====================================图上画图===========================================
# img = cv2.imread("../Image/paint.jpg")
# # 直线
# cv2.line(img,(100,30),(210,180),color=(0,0,255),thickness=2)
# # 圆
# cv2.circle(img,(300,200),60,color=(0,0,255),thickness=-1)
# # 正方形
# cv2.rectangle(img,(100,30),(210,180),color=(0,0,255),thickness=5)
# # 椭圆形
# cv2.ellipse(img,(300,600),(100,50),90,0,360,(0,255,0),thickness=2)
# 多边形
# pts = np.array([[10,5],[200,200],[300,600],[150,38]])
# cv2.polylines(img,[pts],True,(255,0,0),thickness=2)
#
# cv2.imshow("as",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# =====================================图上写字===========================================
# img = cv2.imread("../Image/handsome.jpg")
# cv2.putText(img,"HELLO WORLD",(10,60),cv2.FONT_HERSHEY_SIMPLEX,2,(255,0,0),5,lineType=cv2.LINE_AA)
# # (图片，内容，位置，字体，字体大小，颜色，抗锯齿)
#
# cv2.imshow("as",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# =====================================阀值===========================================
# 全局二值化
# img = cv2.imread("../Image/handsome.jpg")
# gray = cv2.cvtColor(img,cv2.COLOR_BGRA2GRAY)
# ret,binary = cv2.threshold(gray,0,255,cv2.THRESH_BINARY|cv2.THRESH_OTSU)#OTSU自动计算预值
#
#
# cv2.imshow("as",gray)
# cv2.imshow("ass",binary)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# img = cv2.imread("../_Image/1.jpg")
# grayimg = cv2.cvtColor(img,cv2.COLOR_BGRA2GRAY)
#
# ret,ptir1 = cv2.threshold(grayimg,127,255,cv2.THRESH_BINARY)
# ret,ptir2 = cv2.threshold(grayimg,127,255,cv2.THRESH_BINARY_INV)
# ret,ptir3 = cv2.threshold(grayimg,127,255,cv2.THRESH_TRUNC)
# ret,ptir4 = cv2.threshold(grayimg,127,255,cv2.THRESH_TOZERO)
# ret,ptir5 = cv2.threshold(grayimg,127,255,cv2.THRESH_TOZERO_INV)
#
# titles = ["Original Image","BINARY","BINARY_INV","TRUNC","TOZERO","TOZERO_INV"]
# images = [img,ptir1,ptir2,ptir3,ptir4,ptir5]
# for i in range(6):
#     plt.subplot(2,3,i+1) #（行，列，索引）
#     plt.imshow(images[i],"gray")
#     plt.title(titles[i])
#     plt.xticks([])#隐藏x轴
#     plt.yticks([])#隐藏y轴
# plt.show()


# 局部二值化(高斯)
# img = cv2.imread("../Image/2.jpg",0)
# # print(img.shape)
# plt.imshow(img)
# plt.show()
# # gray = cv2.cvtColor(img,cv2.COLOR_BGRA2GRAY)
# ret,pt1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
# th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,
#                             cv2.THRESH_BINARY,11,2)#平均算法
# # (图片，最大值，自适应计算方法，二值化，窗口大小（必须是基数），常数)
# th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
#                             cv2.THRESH_BINARY,11,2)#高斯算法
#
# titles = ["Original Image","Global Thresholding(v=127)","MEAN","GAUSSIAN"]
# images = [img,pt1,th2,th3]
#
# for i in range(4):
#     plt.subplot(2,2,i+1)
#     plt.title(titles[i])
#     plt.imshow(images[i])
#     plt.xticks()
#     plt.yticks()
#
# plt.show()


# =====================================图像加减(混合)===========================================
# x = np.uint8([250]) #array是不行的，会超过255
# y = np.uint8([10])
#
# print(cv2.add(x,y))#add必须针对无符号的uint8
# print(cv2.subtract(x,y))#必须针对无符号的uint8

# 第一种简单的
# img1 = cv2.imread("../Image/1.jpg")
# img2 = cv2.imread("../Image/6.jpg")
# img = cv2.add(img1,img2)
# cv2.imshow("ashd",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 第二种
# img1 = cv2.imread("../Image/1.jpg")#美女
#
# img2 = cv2.imread("../Image/6.jpg")#字
#
# wide,high,channels = img2.shape#字
# roi = img1[0:wide,0:high]
# img2gray = cv2.cvtColor(img2,cv2.COLOR_BGRA2GRAY)
# ret,mask = cv2.threshold(img2gray,10,255,cv2.THRESH_BINARY)
# # 非
# mask_inv = cv2.bitwise_not(mask)
# # 与
# img1_bg = cv2.bitwise_and(roi,roi,mask=mask_inv)
# # 与
# img2_bg = cv2.bitwise_and(img1,img2,mask=mask)
#
# dst = cv2.add(img1_bg,img2_bg)
# img1[0:wide,0:high] = dst
#
# cv2.imshow("ashd",img1)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 图片的权重处理
# img1 = cv2.imread("../Image/1.jpg")
# img2 = cv2.imread("../Image/6.jpg")
# dst = cv2.addWeighted(img1,0.7,img2,0.2,0)
# cv2.imshow("jj",dst)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# =====================================图像变换===========================================

# src = cv2.imread("../Image/handsome.jpg")
# w,h,c = src.shape
# 变大
# ds = cv2.resize(src,(h*2,w*2),interpolation=cv2.INTER_CUBIC)
# 变小
# lk = cv2.resize(src,(h//2,w//2),interpolation=cv2.INTER_CUBIC)
# 翻转,0:上下 1：左右 -1：上下左右
# zhuan1 = cv2.flip(src,0)
# 仿射变换：三维
# m = np.float32([[1,0,50],[0,1,50]])
# m = np.float32([[0.5,0,0],[0,0.5,0]])
# m = np.float32([[-0.5,0,h//2],[0,0.5,0]])
# m = np.float32([[1,0.5,0],[0,1,0]])
# m = cv2.getRotationMatrix2D((h/2,w/2),45,0.7)#图片中心点，旋转角度，缩放比例

# ds = cv2.warpAffine(src,m,(h,w))


# 透视变换：类似放大
# pitch = cv2.imread("../Image/food.jpg")
#
# pts1 = np.float32([[25,30],[179,25],[12,188],[189,190]])
# pts2 = np.float32([[0,0],[500,0],[0,500],[500,500]])
#
# m = cv2.getPerspectiveTransform(pts1,pts2)
# ds = cv2.warpPerspective(pitch,m,(200,200))
#
# cv2.imshow("h",pitch)
# cv2.imshow("c",ds)


# 膨胀变换（变换前需要二值化）:像素值大的进行膨胀
# img1 = cv2.imread("../Image/3.jpg")
# img2 = cv2.imread("../Image/4.jpg")
# 核函数(矩形核)
# kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))
# 椭圆核
# kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(8,8))
# 十字核
# kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(8,8))
# 膨胀
# ds = cv2.dilate(img1,kernel)
# 腐蚀(缩小)
# ds = cv2.erode(img1,kernel)
# 开（先腐蚀再膨胀）：去噪
# ds = cv2.morphologyEx(img2,cv2.MORPH_OPEN,kernel)
# 闭（先膨胀再腐蚀）：补漏洞
# ds = cv2.morphologyEx(img2,cv2.MORPH_CLOSE,kernel)
# 梯度（膨胀减去腐蚀）：提轮廓
# ds = cv2.morphologyEx(img1,cv2.MORPH_GRADIENT,kernel)
# 顶帽（原图-开运算图像）：获取噪音
# ds = cv2.morphologyEx(img2,cv2.MORPH_TOPHAT,kernel)
# 黑帽（开运算图像-原图）：获取漏洞
# ds = cv2.morphologyEx(img2,cv2.MORPH_BLACKHAT,kernel)

# cv2.imshow("s",ds)
# cv2.imshow("a",img1)

# cv2.waitKey(0)

