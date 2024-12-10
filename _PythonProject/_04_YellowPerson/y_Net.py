import torch
from torch.nn import *


class yNet(Module):
    def __init__(self):
        super().__init__()
        self.layer = Sequential(
            # Conv2d(3,16,3,bias=False),MaxPool2d(2),BatchNorm2d(16),LeakyReLU(),
            # Conv2d(16,32,3,bias=False),MaxPool2d(2),BatchNorm2d(32), LeakyReLU(),
            # Conv2d(32,64,3,bias=False),MaxPool2d(2),BatchNorm2d(64), LeakyReLU(),
            # Conv2d(64,128,3,bias=False),MaxPool2d(2),BatchNorm2d(128), LeakyReLU(),
            # Conv2d(128,256,3,bias=False),BatchNorm2d(256), LeakyReLU(),
            # Conv2d(256,425,3,bias=False),BatchNorm2d(425), LeakyReLU(),
            # Conv2d(425,256,3,bias=False),BatchNorm2d(256), LeakyReLU(),
            # Conv2d(256,128,3,bias=False),BatchNorm2d(128), LeakyReLU(),
            # Conv2d(128,64,3,bias=False),BatchNorm2d(64), LeakyReLU(),
            Conv2d(3,16,3,bias=False),MaxPool2d(2),LeakyReLU(),
            Conv2d(16,32,3,bias=False),MaxPool2d(2), LeakyReLU(),
            Conv2d(32,64,3,bias=False),MaxPool2d(2), LeakyReLU(),
            Conv2d(64,128,3,bias=False),MaxPool2d(2), LeakyReLU(),
            Conv2d(128,256,3,bias=False), LeakyReLU(),
            Conv2d(256,425,3,bias=False), LeakyReLU(),
            Conv2d(425,256,3,bias=False), LeakyReLU(),
            Conv2d(256,128,3,bias=False), LeakyReLU(),
            Conv2d(128,64,3,bias=False), LeakyReLU(),

        )
        self.out_layer1 = Sequential(
            Linear(64*6*6,4)
        )
        self.out_layer2 = Sequential(
            Linear(64*6*6,1),
            # Softmax(dim=1)
            Sigmoid()
        )


    def forward(self,x):
        x = self.layer(x)
        # print(x.shape)
        x = x.reshape(x.shape[0],-1)
        o1 = self.out_layer1(x)
        o2 = self.out_layer2(x)
        return o1,o2

if __name__ == '__main__':
    yn = yNet()
    x = torch.rand(2,3,300,300)
    y = yn(x)
    print(yn)
    # print(yn.out_layer1[0])
    # print(yn.out_layer2[0])
    # print(y.shape)

