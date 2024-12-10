import torch
from torch.nn import *

# t==》 通道的扩充倍数（相对于输入通道而言）
# c==》 输出的通道数
# n==》 模块的调用次数
# s==》 最后一次调用的步长（默认是1）
config = [
    [-1, 32, 1, 2],
    [1, 16, 1, 1],
    [6, 24, 2, 2],
    [6, 32, 3, 2],
    [6, 64, 4, 2],
    [6, 96, 3, 1],
    [6, 160, 3, 2],
    [6, 320, 1, 1],
]


class Block(Module):

    def __init__(self, p_c, i, t, c, n, s):
        super().__init__()

        self.i = i
        self.n = n
        # 判断是否是最后一次调用，最后一次调用的步长为s
        _s = s if i == n - 1 else 1
        # 判断是否是最后一次调用，最后一次调用把通道变为下层的输入
        _c = c if i == n - 1 else p_c

        #扩增后的输入通道
        _p_c = p_c*t

        self.layers = Sequential(
            Conv2d(p_c,_p_c,1,1,bias=False),
            BatchNorm2d(_p_c),
            ReLU6(),
            Conv2d(_p_c,_p_c,3,_s,padding=1,groups=_p_c,bias=False),
            BatchNorm2d(_p_c),
            ReLU6(),
            Conv2d(_p_c,_c,1,1,bias=False),
            BatchNorm2d(_c),
            ReLU6(),
        )

    def forward(self,x):
        if self.i == self.n-1:
            return self.layers(x)

        else:
            return self.layers(x)+x


class MobileNet_V2(Module):

    def __init__(self):
        super().__init__()
        self.input_layers = Sequential(
            Conv2d(3,32,3,2,1,bias=False),
            BatchNorm2d(32),
            ReLU6()
        )

        self.blocks = []
        p_c = config[0][1]
        for t,c,n,s in config[1:]:
            for i in range(n):
                self.blocks.append(Block(p_c,i,t,c,n,s))
            p_c = c

        self.hidden_laters = Sequential(*self.blocks)
        self.out_layers = Sequential(
            Conv2d(320,1280,1,1,bias=False),
            BatchNorm2d(1280),
            ReLU6(),
            AvgPool2d(7,1),
            Conv2d(1280,1000,1,1,bias=False)
        )

    def forward(self,x):
        h = self.input_layers(x)
        h = self.hidden_laters(h)
        h = self.out_layers(h)
        h = torch.squeeze(h)
        return h

if __name__ == '__main__':
    net = MobileNet_V2()
    x = torch.randn(2,3,224,224)
    y = net(x)
    print(y.shape)
