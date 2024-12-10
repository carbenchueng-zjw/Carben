import torch
from torch.nn import *
from torch.nn.functional import *


#PNet
class PNet(Module):
    def __init__(self):
        super(PNet, self).__init__()
        self.p_layers = Sequential(
            Conv2d(3,10,3,padding=1),
            PReLU(),
            MaxPool2d(kernel_size=3,stride=2),
            Conv2d(10,16,3),
            PReLU(),
            Conv2d(16,32,3),
            PReLU(),
        )

        self.confidence = Conv2d(32,1,1)
        self.offset = Conv2d(32,4,1)


    def forward(self,x):
        x = self.p_layers(x)
        confidence = sigmoid(self.confidence(x))
        offset = self.offset(x)

        return confidence,offset


#RNet
class RNet(Module):
    def __init__(self):
        super(RNet, self).__init__()
        self.r_layers = Sequential(
            Conv2d(3,28,3,1,1),
            PReLU(),
            MaxPool2d(3,2),
            Conv2d(28,48,3),
            PReLU(),
            MaxPool2d(3,2),
            Conv2d(48,64,2),
            PReLU(),
        )

        self.linears = Linear(64*3*3,128)
        self.prelu = PReLU()
        self.confidence = Linear(128,1)
        self.offset = Linear(128,4)

    def forward(self,x):
        x = self.r_layers(x)
        x = x.reshape(-1,64*3*3)
        x = self.linears(x)
        x = self.prelu(x)
        # print(x.shape)
        confidence = sigmoid(self.confidence(x))
        offset = self.offset(x)
        #
        return confidence,offset

#ONet
class ONet(Module):
    def __init__(self):
        super(ONet, self).__init__()
        self.o_layers = Sequential(
            Conv2d(3,32,3,1,1),
            PReLU(),
            MaxPool2d(3,2),
            Conv2d(32,64,3),
            PReLU(),
            MaxPool2d(3,2),
            Conv2d(64,64,2),
            PReLU(),
            MaxPool2d(2),
            Conv2d(64,128,2),
            PReLU()
        )

        self.linears = Linear(128*3*3,256)
        self.prelu = PReLU()
        self.confidence = Linear(256,1)
        self.offset = Linear(256,4)

    def forward(self,x):
        x = self.o_layers(x)
        # print(x.shape)
        x = x.reshape(x.size(0),-1)
        # print(x.shape)
        x = self.linears(x)
        x = self.prelu(x)
        confidence = sigmoid(self.confidence(x))
        offset = self.offset(x)

        return confidence,offset

if __name__ == '__main__':
    pn = PNet()
    rn = RNet()
    on = ONet()
    x1 = torch.randn(6,3,12,12)
    x2 = torch.randn(2,3,24,24)
    x3 = torch.randn(4,3,48,48)
    y1 = pn(x1)
    y2 = rn(x2)
    y3 = on(x3)
    # print(y3)
    print(y1[0].shape)
    print(y1[1].shape)
    print(y3[0].shape)
    print(y3[1].shape)
