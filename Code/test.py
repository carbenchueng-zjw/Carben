import math
import random, matplotlib.pyplot as plt, mediapipe as mp
import torch
import torchvision, thop, numpy, os, time, copy, cv2
from tqdm import tqdm
from torchvision.utils import save_image
from PIL import Image, ImageDraw, ImageFont
from torch.nn import *
from torchvision import datasets, transforms
from torch.utils.data import Dataset, DataLoader
from torch.nn import functional as F

# a = numpy.array([[[[6,2,6],[7,5,7]]],[[[1,2,3],[4,5,6]]]],dtype=numpy.float64,ndmin=7)
# a = numpy.array([range(i,i+5) for i in [1,2,3]])
# a = numpy.array([1, 0, 2, 3, 0, 5])
# print(a.shape)
# print(a.size)
# print(numpy.nonzero(a))#返回非零元素的索引


# num = numpy.arange(0,12,dtype=numpy.float64).reshape(2,3,-1)
# num = torch.arange(0,12).reshape(2,3,1,2)
# print(num.shape)
# print(num.transpose())
# num = num.permute(1,2,0,3)
# num = num.transpose(1,3,)
# print(num.shape)
# print(num.dtype)

# a = torch.tensor([range(i, i + 2) for i in [1, 2, 6]])
# a = torch.Tensor([1, 0, 2, 3, 0, 5])
# print(torch.nonzero(a))
# a = torch.tensor([[4,7,5],[4,2,5],[7,2,4],[1,2,4]])
# print(torch.sum(a,axis=1))


# a1 = torch.Tensor([
#     [[10,11,12],[13,14,15],[16,17,18],[1,1,1]],
#     [[20,21,22],[23,24,25],[26,27,28],[2,2,2]],
#     [[30,31,32],[33,34,35],[36,37,38],[3,3,3]],
# ])
# print(a1[:,:,[0,2]])
# print(a1.shape) #3,4,3
# print(a1[:,:,[0,2]])
# print(torch.mean(a1))

# x = torch.tensor([[1,2],[3,4]])
# y = torch.tensor([[5,6],[7,8]])
# z = torch.concatenate((x,y),axis = 1)
# print(z)

# users = ["小花","柠檬",["小松"]]
# # user_c = copy.copy(users)
# user_c = users
# user_dc = copy.deepcopy(users)
# users[2].append("小坤")
# users.append("小菲")
# print(users,user_c,user_dc,sep="\n")

# cap = cv2.VideoCapture(0)
# while cap.isOpened():
#
#     ral, image = cap.read()
#     cv2.imshow("image", image)
#     key = cv2.waitKey(17)
#     if key == ord("q"):
#         break
# cap.release()
# cv2.destroyAllWindows()

# # cv2.namedWindow("trest",cv2.WINDOW_NORMAL)
# # cv2.resizeWindow("trest",1000,800)
# img = cv2.imread(r"./_Image/19.jpg")
# tie_img = cv2.imread(r"./_Image/3.jpg")
# tiee_img = cv2.resize(tie_img,dsize=(100,100))
# tie_h,tie_w = tiee_img.shape[:2]
# img[100:100+tie_h,100:100+tie_w] = tiee_img[:tie_h,:tie_w]
# # b,g,r = cv2.split(img)#通道拆分
# # img = cv2.merge((b,g,r))#通道合并
# h,w,c = img.shape
# padding = 20
# img[:padding,:] = (255,0,0)
# img[h-padding:h,:] = (0,255,0)
# img[:,:padding] = (0,0,255)
# img[:,w-padding:w] = (0,255,255)
#
# # cv2.imshow("b",b)
# # cv2.imshow("g",g)
# # cv2.imshow("r",r)
# cv2.imshow("trest",img)
# cv2.imshow("3",tie_img)
# key = cv2.waitKey(0)
# print(key)

# data = numpy.full((1000,1600,3),fill_value=(255,255,255),dtype=numpy.int8)
# cv2.imshow("ds",data)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# img_cv2 = cv2.imread(r"./_Image/1.jpg")
# cv2.imshow("asd",img_cv2)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# img_pil = Image.open(r"./_Image/1.jpg")
# yellow = Image.open(r"D:/2-Data/yellow_pic/1.png")
# w,h = img_pil.size
# img_pil = img_pil.crop((100,100,200,200))
# img_pil = img_pil.rotate(90)
# img_pil = img_pil.transpose(Image.FLIP_TOP_BOTTOM)
# draw = ImageDraw.Draw(img_pil)
# draw.rectangle((10,10,100,200),outline=(255,0,255),width=6)
# draw.ellipse(((100,100),(150,150)),outline=(255,255,0),width=6)
# img_pil.paste(yellow)
# test = numpy.array(img_pil)

# print(test.shape[1])
# img_pil.show()
# img_pil_new = img_pil.resize((w//2,h//2))
# img_pil_new.save("img_pil_new.jpg")
# piexl = img_pil.getpixel((100,200))
# print(piexl)
# img_pil= img_pil.convert("L")
# print(img_pil.getbands())

# print(img_cv2.shape)
# c = [5,5,6,7]

# a = numpy.arange(12,dtype="uint8").reshape((2,2,3))
# b = numpy.ones((2,2,3),dtype="uint8")
# # print(a,b,sep="\n")
# c = numpy.concatenate((a,b),axis=2)  #矩阵拼接
# # c = numpy.stack((a,b),axis=2) #矩阵融合
# print(c)
# print(c.shape)
# print(c.shape)
# print(numpy.where(a>2))
# print(numpy.where(a>2,255,0))
# print(numpy.argwhere(a>2))
# print(a[:,[1]])

# a = numpy.random.randn(2,2,3)#标准正太分布
# a = numpy.random.normal(size=(3,3,2))#正太分布
# a = numpy.random.rand(3,2)#0-1的随机数
# a = numpy.random.randint(4,8,size=(2,2))#随机整数

# a = numpy.array([[1,2],[2,2]])
# b = numpy.array([[3,2],[2,2]])
# print(a*b)
# print(a@b)

# x = numpy.arange(-10,11)
# y = 1/(1+numpy.exp(-x))
# y1 = (numpy.exp(x)-numpy.exp(-x))/(numpy.exp(x)+numpy.exp(-x))
# plt.plot(x,y)
# plt.plot(x,y1)
# plt.show()

# _x = [i/100 for i in range(100)]
# _y = [3*e+4+random.random() for e in _x]
# # plt.plot(_x,_y,"*")
# # plt.show()
# w = random.random()
# b = random.random()
# plt.ion()
# for i in range(30):
#     for x, y in zip(_x,_y):
#         z = x*w+b
#         o = z-y
#         loss = o**2
#
#         dw = -2*o*x
#         db = -2*o
#
#         w = dw*0.1+w
#         b = db*0.1+b
#
#         plt.cla()
#
#         plt.plot(_x,_y,"^")
#         v = [w*e+b for e in _x]
#         plt.plot(_x,v)
#
#         plt.show()
#         plt.pause(0.01)
#     print(i,w,b,loss)
# plt.ioff()
# plt.show()

# class GenerateCode():
#     def getCode(self):
#         codes = [code for code in range(97, 123)]
#         codes.extend(range(65, 91))
#         codes.extend(range(48, 58))
#         # print(codes)
#         ids = random.choice(codes)
#         return chr(ids)
#
#     def getBgColor(self):
#         return (random.randint(150, 220),
#                 random.randint(150, 220),
#                 random.randint(150, 220))
#
#     #
#     def getFontColor(self):
#         return (random.randint(60, 100),
#                 random.randint(60, 100),
#                 random.randint(60, 100))
#
#     def drawText(self):
#         w = 240
#         h = 60
#         panle = Image.new(size=(w, h), color="white", mode="RGB")
#         draw = ImageDraw.Draw(panle)
#         font = ImageFont.truetype(font=r"C:/Windows/msyh.ttc", size=30)
#         for x in range(w):
#             for y in range(h):
#                 draw.point((x, y), fill=self.getBgColor())
#         for i in range(4):
#             draw.text((60 * i + 20, 12), text=self.getCode(),
#                       fill=self.getFontColor(), font=font)
#
#         return panle
#
#
# g = GenerateCode()
# img = g.drawText()
# # img.save("test.jpg")
# img.show()

# a = []
# b = []
# plt.ion()
# for i in range(50):
#     a.append(i**2)
#     b.append(i)
#     plt.cla()
#     plt.plot(b,a,"*")
#     plt.pause(0.1)
# plt.show()
# plt.ioff()
# plt.show()

# img = Image.open(r"./_Image/1.jpg")
# img_data = numpy.array(img)
# 图片变蓝色
# b_data = img_data[...,2]
# b_data = numpy.expand_dims(b_data,axis =2)
# # print(b_data.shape)
# black_img = numpy.zeros((418, 300,1),dtype=numpy.uint8)
# B_img = numpy.concatenate((black_img,black_img,b_data),axis=2)
# # img = Image.fromarray(black_img)
# img = Image.fromarray(B_img)
# print(black_img.shape)
# img.show()
# 图片切分#(必须保证图片都是偶数才能切分)
# h,w,c = img_data.shape
# print(img_data.shape)
# img_data = img_data.reshape((2,h//2,2,w//2,c))#(必须保证图片都是偶数才能切分)
# img_data = img_data.transpose(0,2,1,3,4)
# img_data = img_data.reshape((-1,209,150,c))
# # print(img_data[0].shape)
# img_data1 = img_data[0]
# img_data2 = img_data[1]
# img_data3 = img_data[2]
# img_data4 = img_data[3]
# img_d1 = Image.fromarray(img_data1)
# img_d2 = Image.fromarray(img_data2)
# img_d3 = Image.fromarray(img_data3)
# img_d4 = Image.fromarray(img_data4)
# # plt.figure(figsize=(7,7),facecolor="yellow")
#
# plt.subplot(2,2,1)
# plt.imshow(img_d1)
# plt.subplot(2,2,2)
# plt.imshow(img_d2)
# plt.subplot(2,2,3)
# plt.imshow(img_d3)
# plt.subplot(2,2,4)
# plt.imshow(img_d4)
# # plt.axis("off")
# plt.suptitle("people")
# plt.show()


# p1 = cv2.imread(r"./_Image/1.jpg")
# p2 = cv2.imread(r"./_Image/6.jpg")
# p = cv2.resize(p,(500,500))
# ret,binary = cv2.threshold(p,0,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)
# print(ret)
# bin_2 = cv2.adaptiveThreshold(p,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
#                               cv2.THRESH_BINARY,18,2)
# pos = numpy.array([[30,30],[120,60],[120,200],[30,200]])
# font = cv2.FONT_HERSHEY_SIMPLEX
# text = "test"
# p = cv2.cvtColor(p,cv2.COLOR_BGR2RGB)
# p[...,0] = 0
# p[...,1] = 0
# cv2.rectangle(p,(100,100),(200,200),(0,0,255),thickness=2)
# cv2.line(p,(50,50),(200,200),(0,255,255))
# cv2.circle(p,(50,50),30,(255,0,0),thickness=-1)
# cv2.ellipse(p,(150,150),(100,30),90,60,300,(255,0,0),thickness=-1)
# cv2.polylines(p,[pos],True,(255,255,0),thickness=2)
# cv2.putText(p,text,(30,80),font,2,(0,0,255),thickness=2)

# p = cv2.addWeighted(p1,0.3,p2,0.7,0)
#
# cv2.imshow("asd",p)
# cv2.waitKey(0)
# plt.subplot(2,2,4)
# plt.imshow(p)
# plt.show()

# 回调

#
# st_p = [-1,-1]
# end_p = [-1,-1]
# img = cv2.imread(r"./_Image/19.jpg")
# def drawLine(event,x,y,flags,param):
#     global st_p,end_p
#     if event == cv2.EVENT_LBUTTONDOWN:
#         st_p=(x,y)
#         print(f"down:{event} {x} {y}")
#
#     if event == cv2.EVENT_LBUTTONUP:
#         end_p=(x,y)
#
#         print(f"up:{event} {x} {y}")
#         cv2.line(img,st_p,end_p,(0,255,0),thickness=2)
#
#         cv2.imshow("board",img)
#
# def callBack(event,x,y,flags,param):
#     drawLine(event,x,y,flags,param)
#     drawLine(event,x,y,flags,param)
# def mouseDrawing():
#     cv2.namedWindow("board",cv2.WINDOW_NORMAL)
#     # cv2.resizeWindow("board",1000,600)
#     cv2.setMouseCallback("board",callBack,"hello")
#
#     #将函数callback注册在窗口(board)上，
#     cv2.imshow("board",img)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
#
# mouseDrawing()

# a = torch.Tensor([[[1,2,3],[7,8,9]],[[4,5,6],[1,1,1]]])
# b = torch.randn(3,4).cuda()
# c = torch.rand(3,4)
# print(f"tensor的形状：{c.shape}")
# print(f"tensor的数据类型：{c.dtype}")
# print(f"tensor的数据类型：{b.dtype}")
# print(f"tensor的运算形式：{c.device}")
# print(f"tensor的运算形式：{b.device}")
# print(b.sum(dim=1))
# g = torch.eye(5).cuda()
# print(torch.numel(a))#返回张量的总个数

# t1 = torch.arange(8).reshape(2,4)
# t2 = torch.arange(9,17).reshape(2,4)
# print(torch.mul(t1,t2))

# a = torch.tensor([[[1],[2]]])
# b = torch.tensor([[[3],[4]]])
# c = torch.cat((a,b),0)
# d = torch.cat((a,b),1)
# print(torch.eq(a,b))
# print(a.unsqueeze(dim=1).shape)
# print(a.squeeze().shape)

# x = torch.arange(1,10).reshape(3,3)
# a,b,c = x.split(1,0)
# print(a,b,c,sep="\n")

# class Net(Module):
#     def __init__(self):
#         super().__init__()
#         self.seq = Sequential(
#             Linear(3,10),
#             ReLU(),
#             Linear(10,2),
#             ReLU(),
#             Softmax(dim=1)
#         )
#
#     def forward(self,x):
#        return self.seq(x)
#
#
# N = Net()
# y = torch.randn(3,3)
# h = N(y)
# print(h.shape)

# t_train = datasets.cifar(root=r"D:/2-Data",download=True)
# t_test = datasets.cifar(root=r"D:/2-Data",download=True,train=False)
# print(t_train.data[500].shape)
# un = transforms.ToPILImage()(t_train.data[500])
# un.show()
# print(t_train.targets[500])

# bg = Image.new("RGB",(500,500),(0,0,255))
# img_1 = Image.open("./_Image/2.jpg")
# img_2 = Image.open("./_Image/3.jpg")
# bg.paste(img_1,(0,0))
# bg.paste(img_2,(200,200))
# plt.subplot(1,3,1)
# plt.imshow(img_1)
# plt.axis(False)
# plt.subplot(1,3,2)
# plt.imshow(img_2)
# plt.axis(False)
# plt.subplot(1,3,3)
# plt.imshow(bg)
# plt.axis(False)
# plt.show()


# net_1 = Linear(3*32*32,512)
# net_2 = Conv2d(1,1,1,padding=1,padding_mode="zeros")
# x_1 = [p.numel() for p in net_1.parameters()]
# x_2 = [p.numel() for p in net_2.parameters()]
# print(x_1,x_2)
# x = torch.randn(1,1,3,3)
# y = net_2(x)
# print(y)

# 编解码
'''
class Encoder(Module):
    def __init__(self):
        super().__init__()
        self.layer = Sequential(
            Linear(784, 512), ReLU(),
            Linear(512, 256), ReLU(),
            Linear(256, 256), ReLU(),
            Linear(256, 128), ReLU(),
            Linear(128, 128), ReLU(),
            Linear(128, 128), ReLU(),
            Linear(128, 64), ReLU(),
            Linear(64, 32), ReLU(),
            Linear(32, 32), ReLU(),
            Linear(32, 10), ReLU(),

        )

    def forward(self, x):
        return self.layer(x)


class Decoder(Module):
    def __init__(self):
        super().__init__()
        self.layer = Sequential(
            Linear(10, 32), ReLU(),
            Linear(32, 32), ReLU(),
            Linear(32, 64), ReLU(),
            Linear(64, 64), ReLU(),
            Linear(64, 128), ReLU(),
            Linear(128, 128), ReLU(),
            Linear(128, 128), ReLU(),
            Linear(128, 256), ReLU(),
            Linear(256, 512), ReLU(),
            Linear(512, 784), ReLU(),

        )


    def forward(self, x):
        return self.layer(x)


class EDcoder(Module):
    def __init__(self):
        super().__init__()
        self.encoder = Encoder()
        self.decoder = Decoder()

    def forward(self,x):

        x = self.encoder(x.reshape(-1,784))
        return self.decoder(x)

ed = EDcoder()
ed.cuda()
ed.load_state_dict(torch.load(f"./params/50.pt"))
train_data = datasets.MNIST(r"D:/2-Data/", transform=transforms.ToTensor(),train=True,download=False)
train_loader = DataLoader(train_data, shuffle=True, batch_size=100)
fc_loss = MSELoss()
opt = torch.optim.Adam(ed.parameters())
j = 1
for epoch in range(1,10001):
    for i,(img,label) in tqdm(enumerate(train_loader),total=len(train_loader)):
        img = img.cuda()
        out = ed(img)
        out = out.reshape(out.size(0),1,28,28)
        # print(img.size())
        # print(out.shape)
        # exit()
        loss = fc_loss(out,img)
        opt.zero_grad()
        loss.backward()
        opt.step()
        if i%500 ==0:
            print(loss.item())
            out.detach()
            # print(out.shape)
            # exit()
            save_image(out,f"./_Image/write_generate/{j}.jpg",nrow=10,padding=5)
            j+=1
        # torch.save(ed.state_dict(),f"./params/{j}.pt")
'''

# 分组
# data = torch.arange(1,7).reshape(1,6)
# data = data.reshape(1,2,3)
# print(data)
# # data = data.transpose(2,4)
# data = data.permute(0,2,1)
# data.reshape(1,6,)
# print(data)

# net = torchvision.models.mobilenet_v3_small()
# print(net.classifier[3])

# class Net(Module):
#     def __init__(self):
#         super().__init__()
#         self.layer = Sequential(
#             Conv2d(3,16,3)
#         )
#
#     def forward(self,x):
#         return self.layer(x)
#
# net = Net()
# img = torch.randn(1,3,16,16)
# x = net(img)
# w = conv.padding()
# b = conv.bias
# print(img)
# print(x)
# print(conv.weight)
# print(w)
# print(b)
# flops,par = thop.profile(net,(img,))
# print(flops,par)

# x = torch.tensor([1,5,2,8,7])
# y = functional.one_hot(x,10)
# print(y)

# img = cv2.imread("./_Image/23.jpg")
# img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
# img = Image.open("./_Image/23.jpg")
# # cv2.flip(img,0)
# trans = transforms.Compose([
#     # transforms.ToTensor(),
#     transforms.RandomRotation(45),
#     transforms.RandomCrop((140,140)),
#
# ])
# img = trans(img)
# plt.imshow(img)
# plt.show()

# cv2.imshow("img",img)
# cv2.waitKey(0)

# data = torch.arange(1,5.).reshape(1,2,2)
# print(data)
# # ``'nearest'`` | ``'linear'`` | ``'bilinear'`` | ``'bicubic'`` |
# # ``'trilinear'`` | ``'area'`` | ``'nearest-exact'``. Default: ``'nearest'``
# data = F.interpolate(data,scale_factor=2)#默认插值法
# print(data)


# name = "VOC2012"
# add = rf"D:\2-Data\{name}"
# print(add)
# a = torch.randn(2,3,2,3)
# print(a.shape)
# print(a.size())
# b = torch.randn(2,3,2,3)
# c = torch.cat((a,b),dim=3)
# d = torch.stack((a,b),dim=3)
# print(c.shape)
# print(d.shape)
# b=torch.argmax(a,dim=1)
# print(b)

# a = [3,4,5,6,7,8,9,10,11]
# for i ,item in enumerate(a,3):
#     print(i,item)

# img.show()

# print(type(torch.Tensor(img2)))
# cv2.imshow("pic show",img)#使用opencv自带的窗口
# cv2.waitKey(0)#0是死循环，里面单位是毫秒
# cv2.destroyAllWindows()#摧毁所有窗口
# print(img.shape)
# print(img.size)

# bg_pic = "D:/2-Data/cartoon_face_img"
# yellow = "D:/2-Data/yellow_pic/y_logo"
# data = "D:/2-Data/yellow_pic/y_test_img"
# file_all = os.listdir(bg_pic)
# i = 129999
# file_all = file_all[i:]
# print(len(file_all))
#
# for fileName in tqdm(file_all,total=len(file_all)):
#     bg_img = Image.open(f"{bg_pic}/{fileName}")
#     bg_img = bg_img.resize((300, 300))
#     img_yellow = Image.open(f"{yellow}/{numpy.random.randint(1, 21)}.png")
#     w = numpy.random.randint(100, 180)
#     img_yellow = img_yellow.resize((w, w))
#     x1, y1 = numpy.random.randint(0, 300 - w), numpy.random.randint(0, 300 - w)
#     r, g, b, a = img_yellow.split()
#     bg_img.paste(img_yellow, (x1, y1), mask=a)
#     x2, y2 = x1 + w, y1 + w
#     bg_img.save(f"{data}/{i}.{int(x1)}.{int(y1)}.{int(x2)}.{int(y2)}.1.png")
#     i+=1

    # bg_img.show()
    # exit()

# data = "D:/2-Data/yellow_pic/y_test_img"
# file = os.listdir(data)
# plt.ion()
# for file_name in os.listdir(data):
#     img = Image.open(f"{data}/{file_name}")
#     plt.clf()
#     plt.imshow(img)
#     # plt.show()
#     plt.pause(1)
# plt.ioff()

# a = 0.0123456
# a = "%.5f"%a
# print(a)
# box = torch.Tensor([1, 1, 10, 10, 40])
# boxes = torch.Tensor([[1, 1, 19, 9, 10],
#                      [9, 8, 13, 20, 15],
#                      [6, 11, 18, 17, 13]])
# index = boxes[:,4].argsort()
# print(boxes[index])

# img = Image.open(r"D:\2-Data\Celeba\sample\165126.jpg")
# # img1 = img.crop((845,368,1203,792))
# # img = cv2.imread(r"D:\2-Data\Celeba\test\test_img\000147.jpg")
# # img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
# # img = transforms.ToPILImage()(img)
# draw = ImageDraw.Draw(img)
# draw.rectangle((37,39,65,71),outline="red",width=1)
# # draw.ellipse(((1031,558),(1051,578)),fill="green",outline="red",width=3)
# plt.imshow(img)
# plt.show()

# # a = torch.Tensor([[1,3,3],[2,3,3],[3,3,3],[7,3,3],[8,3,3],[9,3,3]])
# a = torch.Tensor([[[[1,3]]],[[[2,3]]]])
# # a = torch.Tensor([1,2,3,4,5,6])
# # b = torch.lt(a,5)
# # c = torch.masked_select(a,b)
# b = torch.gt(a,3)
# c = torch.nonzero(b)[:,0]
# d = a[c]
# e = torch.nn.functional.interpolate(a,scale_factor=2)
# # b = torch.where(a>3)
# # c = a[b]
#
# # print(torch.where(a>3[0]))
# print(e)

# #打印菱形
# row_ = int(input("输入奇数"))
# row = (int(row_)+1)//2
#
# for i in range(1,row+1):
#     print(" "*(row-i),end="")
#     for j in range(2*i-1):
#         print("*",end="")
#         j+=i
#     print()
#     i+=1
#
# for j in range(1,row):
#     # for l in range(j):
#     print(" "*j,end="")
#     for k in range(1,row_-j*2+1):#4,2,(
#         print("*",end="")
#     print()

#打印空心菱形
# row_ = int(input("输入奇数"))
# row = (int(row_)+1)//2
#
# for i in range(1,row+1):
#     print(" "*(row-i),end="")
#     for j in range(1,2*i):
#         if j ==1 or j==2*i-1:
#             print("*",end="")
#         else:
#             print(" ",end="")
#         j+=i
#     print()
#     i+=1
#
# for j in range(1,row):
#     # for l in range(j):
#     print(" "*j,end="")
#     for k in range(1,row_-j*2+1):#4,2,(
#         if k ==1 or k==row_-j*2:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()


# a = torch.arange(12).reshape(3,2,2)
# mask = a[...,0]>5
# idx = mask.nonzero()
# # print(a)
# # print(idx)
# print(a[idx])
# # print(idx.shape)
# # print(a[...,0])
# # print(a[...,0]>3)

# s = dict(cat = 10,cow = 20)
# lst = list(s.items())
# dit = dict(lst)
# print(lst)
# print(dit)
# print(s.get("horse","100"))
print(torch.__version__)













