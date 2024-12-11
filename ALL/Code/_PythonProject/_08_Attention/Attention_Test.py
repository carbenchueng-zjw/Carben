import torch
from torch.nn import *
from torch.nn.functional import *


class CnnWithAttention(Module):

    def __init__(self):
        super().__init__()
        self.layers = Sequential(
            Conv2d(3,16,3,1,1),
            PReLU(),
            MaxPool2d(2),
            PReLU(),
            Conv2d(16,32,3,1,1),
            PReLU(),
            MaxPool2d(2)
        )
        self.attention_layer = MultiheadAttention(embed_dim=32,num_heads=1)
        self.fc = Linear(32*8*8,10)

    def forward(self,x):
        x = self.layers(x)
        x = x.reshape(x.size(0),x.size(1),-1)
        x,_ = self.attention_layer(x,x,x)
        x = x.reshape(x.size(0),-1)
        x = self.fc(x)

        return x
if __name__ == '__main__':
    net = CnnWithAttention()
    x = torch.randn(1,3,32,32)
    print(net(x).shape)






