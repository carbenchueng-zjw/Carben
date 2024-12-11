import torch
from torchvision.models import densenet201
from torch.nn import *

class Net(Module):

    def __init__(self):
        super().__init__()
        self.conv = Sequential(
            Conv2d(1,64,3,padding=1,bias=False),
            PReLU(),
            BatchNorm2d(64),
            Conv2d(64,32,3,2,padding=1,bias=False),
            PReLU(),
            BatchNorm2d(32),
        )

        self.layer = Sequential(
            Linear(32*14*14,512),
            PReLU(),
            Linear(512,256),
            PReLU(),
            Linear(256,64),
            PReLU(),
            Linear(64,2),
        )

    def forward(self,x):
        conv_out = self.conv(x)
        conv_out = conv_out.reshape(-1,32*14*14)
        out = self.layer(conv_out)

        return out

if __name__ == '__main__':
    net = Net()
    x = torch.randn((1,1,28,28))
    y = net(x)
    print(y.shape)