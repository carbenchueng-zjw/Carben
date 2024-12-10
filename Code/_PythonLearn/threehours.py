import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


def stackImages(scale, imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range(0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape[:2]:
                    imgArray[x][y] = cv.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None,
                                               scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y] = cv.cvtColor(imgArray[x][y], cv.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank] * rows
        hor_con = [imageBlank] * rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None, scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv.cvtColor(imgArray[x], cv.COLOR_GRAY2BGR)
        hor = np.hstack(imgArray)
        ver = hor
    return ver


def empty(a):
    pass

def writeColor():
    wide = 600
    high = 600
    cap = cv.VideoCapture(0)
    cap.set(3, wide)
    cap.set(4, high)

    cv.namedWindow("TrackBars")
    cv.resizeWindow("TrackBars", 1000, 500)
    cv.createTrackbar("hue min", "TrackBars", 101, 179, empty)
    cv.createTrackbar("set min", "TrackBars", 96, 255, empty)
    cv.createTrackbar("val min", "TrackBars", 19, 255, empty)
    cv.createTrackbar("hue max", "TrackBars", 179, 179, empty)
    cv.createTrackbar("set max", "TrackBars", 255, 255, empty)
    cv.createTrackbar("val max", "TrackBars", 255, 255, empty)

    while True:
        _, img = cap.read()
        imghsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

        hue_min = cv.getTrackbarPos("hue min", "TrackBars")
        set_min = cv.getTrackbarPos("set min", "TrackBars")
        val_min = cv.getTrackbarPos("val min", "TrackBars")
        hue_max = cv.getTrackbarPos("hue max", "TrackBars")
        set_max = cv.getTrackbarPos("set max", "TrackBars")
        val_max = cv.getTrackbarPos("val max", "TrackBars")
        # print(hue_min,hue_max,set_min,set_max,val_min,val_max)
        lower = np.array([hue_min, set_min, val_min])
        upper = np.array([hue_max, set_max, val_max])
        # print(lower,upper)
        mask = cv.inRange(imghsv, lower, upper)
        imgResult = cv.bitwise_and(img, img, mask=mask)
        mask = cv.cvtColor(mask, cv.COLOR_GRAY2BGR)

        imgStack = stackImages(0.8, ([img, imghsv], [mask, imgResult]))
        # cv.imshow("ou",img)
        # cv.imshow("ot",imghsv)
        # cv.imshow("oe",imgResult)
        cv.imshow("od", imgStack)

        if cv.waitKey(1) & 0xff == ord("q"):
            break

    cap.release()
    cv.destroyAllWindows()

# writeColor()

# ======================================图片，视频访问=======================================
# kkk = cv.imread("a.jpg")
#
# cv.imshow("out",kkk)
# cv.waitKey(0)
#
# kkk = cv.VideoCapture(0)
# kkk.set(3,640)#高
# kkk.set(4,480)#宽
# kkk.set(10,10)#亮度
#
# while True:
#     secc,img = kkk.read()
#     cv.imshow("v",img)
#     if cv.waitKey(1)& 0xFF == ord("q"):
#         break


# ======================================图片优化============================
img = cv.imread("lambo.jpg")

w,h,c = img.shape
ds = cv.resize(img,(h//2,w//2))
ker = np.ones((1,1),np.uint8)

imgGray = cv.cvtColor(ds,cv.COLOR_BGR2GRAY) #转色
# imgBlur = cv.GaussianBlur(ds,(33,33),0) #模糊
imgCan2 = cv.Canny(imgGray,50,180) #取细节
imgDia = cv.dilate(imgCan2,ker,iterations=1) #膨胀
imgEro = cv.erode(imgDia,ker,iterations=1) #腐蚀

cv.imshow("out",imgCan2)
# cv.imshow("out",imgDia)
cv.imshow("o",imgGray)
# cv.imshow("ou",imgEro)
cv.waitKey(0)


# =======================================改变尺寸和颜色===========================

# img = cv.imread("lambo.jpg")
# w,h,c = img.shape
# img = cv.resize(img,(h//2,w//2),c)
# imgrez = img[0:200,200:800]
# print(img.shape)

# imgGray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# imgCan = cv.Canny(imgGray,60,60)


# cv.imshow("oq",img)
# cv.imshow("ou",imgrez)
# cv.waitKey(0)


# =====================================划线写字=============================

# img = cv.imread("a.jpg")
# pt = np.zeros((300,300,3),np.uint8)
# # pt[0:100] = 160,0,0
# # pt[100:200,100:200] = 0,166,0
# # pt[200:300] = 0,0,160
# # 直线
# cv.line(pt,(0,0),(pt.shape[1],200),(255,0,0),3)
# # 矩形
# cv.rectangle(pt,(0,0),(150,250),(0,255,0),1)
# # 圆
# cv.circle(pt,(150,150),50,(255,0,255),-1)
#
# cv.putText(img,"Beautiful Girl",(100,130),cv.FONT_HERSHEY_SIMPLEX,
#            5,(0,255,255),5,cv.LINE_AA)
#
# cv.imshow("oq",img)
# # cv.imshow("ou",pt)
# cv.waitKey(0)


# =====================================扭曲透视=============================

# img = cv.imread("a.jpg")
# wid,hig = 200,300
#
# pt1 = np.float32([[111,219],[288,188],[150,0],[30,130]])
# pt2 = np.float32([[0,0],[wid,0],[0,hig],[wid,hig]])
# mat = cv.getPerspectiveTransform(pt1,pt2)
# imgOut = cv.warpPerspective(img,mat,(wid,hig))
#
# cv.imshow("ou",imgOut)
# cv.waitKey(0)


# ==================================图像添加================================
# 注意：大小，通道数量必须相同

# img = cv.imread("a.jpg")
# img = cv.resize(img,(img.shape[1]//2,img.shape[0]//2),3)
# # 横向添加
# img1 = np.hstack((img,img))
# # 纵向添加
# img2 = np.vstack((img,img))

# cv.imshow("ou",img2)
# cv.waitKey(0)


# ==================================彩色图像================================
#
# path = "a.jpg"
#
# cv.namedWindow("TrackBars")
# cv.resizeWindow("TrackBars",1000,500)
# cv.createTrackbar("hue min","TrackBars",112,179,empty)
# cv.createTrackbar("hue max","TrackBars",179,179,empty)
# cv.createTrackbar("set min","TrackBars",38,255,empty)
# cv.createTrackbar("set max","TrackBars",60,255,empty)
# cv.createTrackbar("val min","TrackBars",184,255,empty)
# cv.createTrackbar("val max","TrackBars",221,255,empty)
#
# while True:
#     img = cv.imread(path)
#     imghsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
#
#     hue_min = cv.getTrackbarPos("hue min","TrackBars")
#     hue_max = cv.getTrackbarPos("hue max","TrackBars")
#     set_min = cv.getTrackbarPos("set min","TrackBars")
#     set_max = cv.getTrackbarPos("set max","TrackBars")
#     val_min = cv.getTrackbarPos("val min","TrackBars")
#     val_max = cv.getTrackbarPos("val max","TrackBars")
#     print(hue_min,hue_max,set_min,set_max,val_min,val_max)
#     lower = np.array([hue_min,set_min,val_min])
#     upper = np.array([hue_max,set_max,val_max])
#     # print(lower,upper)
#     mask = cv.inRange(imghsv,lower,upper)
#     imgResult = cv.bitwise_and(img,img,mask=mask)
#
#
#     imgStack = stackImages(0.6,([img,imghsv],[mask,imgResult]))
#     # cv.imshow("ou",img)
#     # cv.imshow("ot",imghsv)
#     # cv.imshow("oe",imgResult)
#     cv.imshow("od",imgStack)
#
#     cv.waitKey(1)


# ==================================轮廓检测================================
# def getContours(img):
#     contours, hier = cv.findContours(img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
#     for cnt in contours:
#         zrea = cv.contourArea(cnt)
#         # print(zrea)
#         if zrea > 500:
#             cv.drawContours(imgContour, cnt, -1, (255, 0, 0), 5)
#             peri = cv.arcLength(cnt, True)
#             # print(peri)
#             approx = cv.approxPolyDP(cnt, 0.02 * peri, True)
#             # print(approx)
#             objcor = len(approx)
#             x, y, w, h = cv.boundingRect(approx)
#             if objcor == 3:
#                 ObjectType = "Tri"
#             elif objcor == 4:
#
#                 aspRatio = w / float(h)
#                 if aspRatio > 0.95 and aspRatio < 1.05:
#                     ObjectType = "Square"
#                 else:
#                     ObjectType = "Rectangle"
#             elif objcor > 4:
#                 ObjectType = "Circle"
#
#             else:
#                 ObjectType = "None"
#
#             cv.rectangle(imgContour, (x, y), (x + w, y + h), (255, 255, 0), 5)
#             cv.putText(imgContour, ObjectType,
#                        (x + (w // 2) + 10, y + (h // 2)), cv.FONT_HERSHEY_COMPLEX,
#                        0.5, (0, 0, 0), 2)
#
#
# img = cv.imread("allshape.jpeg")
# imgContour = img.copy()
# # img = cv.resize(img,(img.shape[1]//2,img.shape[0]//2),3)
# imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# imgBlur = cv.GaussianBlur(imgGray, (7, 7), 1)
# imgCanny = cv.Canny(imgBlur, 50, 50)
# contours = getContours(imgCanny)
#
# ImageStack = stackImages(0.5, ([img, imgBlur, imgGray, imgCanny, imgContour]))
#
# # cv.imshow("os",ImageStack)
#
# images = [img, imgBlur, imgGray, imgCanny, imgContour]
# for i in range(5):
#     plt.subplot(2, 3, i + 1)  # （行，列，索引）
#     plt.imshow(images[i], "gray")
#
#     plt.xticks([])  # 隐藏x轴
#     plt.yticks([])  # 隐藏y轴
# plt.show()
#
# cv.waitKey(0)


# ==================================人脸检测================================
# faceCascade = cv.CascadeClassifier("Ai/haarcascade_frontalface_default.xml")
# img = cv.imread("jack.jpg")
# imgGray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#
# faces = faceCascade.detectMultiScale(imgGray,1.1,3)
# for (x,y,w,h) in faces:
#     cv.rectangle(img,(x, y), (x + w, y + h), (255, 255, 0), 2)
#
# cv.imshow("os",img)
# # cv.imshow("osv",imgGray)
# cv.waitKey(0)


# ==================================颜色写入================================
# wide = 600
# high = 600
# cap = cv.VideoCapture(0)
# cap.set(3,wide)
# cap.set(4,high)
#
# myColors = [[101,96,19,179,255,255],
#             [0,157,95,179,255,255]]
#
# colorValues = [[255,255,0],
#                [51,153,255]]
#
# myPoints = [] #x,y,color id
#
# def findColor(img,myColors,colorValues):
#     imghsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
#     count = 0
#     newPoints = []
#     for color in myColors:
#         lower = np.array(color[0:3])
#         upper = np.array(color[3:6])
#         mask = cv.inRange(imghsv,lower,upper)
#         x,y = getContours(mask)
#         cv.circle(imgResult,(x,y),3,colorValues[count],cv.FILLED)
#         if x != 0 and y != 0:
#             newPoints.append([x,y,count])
#         count+=1
#         # cv.imshow(str(color[0]),mask)
#     return newPoints
#
# def getContours(img):
#     contours, hier = cv.findContours(img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
#     x, y, w, h = 0,0,0,0
#     for cnt in contours:
#         zrea = cv.contourArea(cnt)
#         if zrea > 500:
#             # cv.drawContours(imgResult, cnt, -1, (255, 0, 0), 5)
#             peri = cv.arcLength(cnt, True)
#
#             approx = cv.approxPolyDP(cnt, 0.02 * peri, True)
#             x, y, w, h = cv.boundingRect(approx)
#     return x+w//2,y
#
# def drawOnCanvas(myPoins,colorValues):
#     for poings in myPoins:
#         cv.circle(imgResult, (poings[0], poings[1]), 3, colorValues[poings[2]], cv.FILLED)
#
#
# while True:
#     succse,imgb = cap.read()
#     imgResult = imgb.copy()
#     newPoints = findColor(imgb,myColors,colorValues)
#     if len(newPoints) != 0:
#         for newp in newPoints:
#             myPoints.append(newp)
#     if len(myPoints)!= 0:
#         drawOnCanvas(myPoints,colorValues)
#
#     cv.imshow("rr",imgResult)
#     if cv.waitKey(1) & 0xff == ord("q"):
#         break


# ==================================物品认证================================
# wide = 800
# high = 500
# cap = cv.VideoCapture(0)
# cap.set(3,wide)
# cap.set(4,high)
#
# def perProcessig(img):
#     imgGray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#     imgGray = cv.GaussianBlur(imgGray,(5,5),1)
#     imgCanny = cv.Canny(imgGray,200,200)
#     ker = np.ones((5,5))
#     imgDila = cv.dilate(imgCanny,ker,iterations=2)
#     imgErode = cv.erode(imgDila,ker,iterations=1)
#
#     return imgErode
#
# def getContours(img):
#     biggest = np.array([])
#     maxArea = 0
#     contours, hier = cv.findContours(img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
#     x, y, w, h = 0,0,0,0
#     for cnt in contours:
#         zrea = cv.contourArea(cnt)
#         if zrea > 5000:
#
#             peri = cv.arcLength(cnt, True)
#
#             approx = cv.approxPolyDP(cnt, 0.02 * peri, True)
#             if zrea > maxArea and len(approx) ==4:
#                 biggest = approx
#                 maxArea = zrea
#     cv.drawContours(imgCountours, biggest, -1, (255, 0, 0), 20)
#     return biggest
#
# def reorder(myPoint):
#     myPoint = myPoint.reshape((4,2))
#     myPointNew = np.zeros((4,1,2),np.int32)
#     add =myPoint.sum(1)
#     print(add)
#
#     myPointNew[0] = myPoint[np.argmin(add)]
#     myPointNew[3] = myPoint[np.argmax(add)]
#     diff = np.diff(myPoint,axis=1)
#     myPointNew[1] = myPoint[np.argmin(diff)]
#     myPointNew[2] = myPoint[np.argmax(diff)]
#
#     return myPointNew
#
# def getWarp(img,biggest):
#     biggest = reorder(biggest)
#     pt1 = np.float32(biggest)
#     pt2 = np.float32([[0,0],[wide,0],[0,high],[wide,high]])
#     mat = cv.getPerspectiveTransform(pt1,pt2)
#     imgOut = cv.warpPerspective(img,mat,(wide,high))
#
#     imgCropped = imgOut[20:imgOut.shape[0]-20,20:imgOut.shape[1]-20]
#     imgCropped = cv.resize(imgCropped,(wide,high))
#     return imgOut
#
# while True:
#     succ,img = cap.read()
#     img = cv.resize(img, (wide, high))
#     imgCountours = img.copy()
#     imgtr = perProcessig(img)
#     biggest = getContours(imgtr)
#     print(biggest)
#     imgWarp = getWarp(img,biggest)
#
#     imgArray = ([img,imgCountours],[imgtr,imgWarp])
#
#     cv.imshow("a",imgCountours)
#     if cv.waitKey(1) & 0xff == ord("q"):
#         break


# ==================================车牌检测================================
# wide = 600
# high = 500
# cap = cv.VideoCapture(0)
# cap.set(3,wide)
# cap.set(4,high)
# minArea = 500
# color = (255,255,0)
# count = 0
#
# CarCascade = cv.CascadeClassifier("Ai/haarcascade_russian_plate_number.xml")
#
# while True:
#     succ,img = cap.read()
#
#     imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#
#     CarNumber = CarCascade.detectMultiScale(imgGray, 1.1, 3)
#     for (x, y, w, h) in CarNumber:
#         area = w*h
#         if area >minArea:
#
#             cv.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 2)
#             cv.putText(img,"CarNumber",(x,y-5),cv.FONT_HERSHEY_COMPLEX_SMALL,1,color,2)
#
#             imgRoi = img[y:y+h,x:x+w]
#
#     cv.imshow("a",img)
#     if cv.waitKey(1) & 0xff == ord("s"):
#         cv.imwrite("Ai/bibi"+str(count)+".jpg",imgRoi)
#         cv.rectangle(img,(0,200),(640,300),(0,255,0),cv.FILLED)
#         cv.putText(imgRoi,"sss",(150,265),cv.FONT_HERSHEY_COMPLEX_SMALL,2,(0,0,255),2)
#         cv.imshow("Result",img)
#         cv.waitKey(500)
#         count +=1
































