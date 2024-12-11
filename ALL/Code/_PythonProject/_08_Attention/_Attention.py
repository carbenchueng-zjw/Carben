import torch
from torch.nn import *
from torch.nn.functional import *


class Attention(Module):

    def __init__(self, in_c):
        super().__init__()
        self.conv1 = Conv2d(in_c, in_c // 8, 1)
        self.conv2 = Conv2d(in_c, in_c // 8, 1)
        self.conv3 = Conv2d(in_c, in_c, 1)

    def forward(self, x):
        q = self.conv1(x)
        k = self.conv2(x)
        v = self.conv3(x)
        #改变张量纬度NCHW====NSV
        q = q.reshape(q.size(0),q.size(1),-1)
        k = k.reshape(k.size(0),k.size(1),-1)
        v = v.reshape(v.size(0),v.size(1),-1)
        #计算注意力权重
        s = torch.bmm(q.permute(0,2,1),k)
        beat = softmax(s,dim=-1) #神经网络不需要特征降维，所以不用除以跟好dk
        # beat = softmax(torch.div(s,torch.sqrt(k.dim)),dim=-1) 这是单独的公式

        #注意力加权求和
        o = torch.bmm(v,beat.permute(0,2,1))
        #NSV===NCHW
        o = o.reshape(o.size(0),o.size(1),x.size(2),x.size(3))
        x = x+o
        return x


class Net(Module):

    def __init__(self):
        super().__init__()

        self.layers = Sequential(
            Conv2d(3,32,3,1,1),
            PReLU(),
            MaxPool2d(2),
            Attention(32),
            PReLU(),
            Conv2d(32,64,3,1,1),
            MaxPool2d(2),
            PReLU()
        )
        self.out_layers = Sequential(
            Linear(64*8*8,128),
            PReLU(),
            Linear(128,10)
        )

    def forward(self,x):
        x = self.layers(x)
        x = x.reshape(-1,64*8*8)
        x = self.out_layers(x)

        return x

if __name__ == '__main__':
    net = Net()
    x = torch.randn(1,3,32,32)
    print(net(x).shape)






