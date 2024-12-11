import torch
from torch.nn import *
from torch.nn import functional as F

class CNN_Block(Module):
    def __init__(self, c_in, c_out):
        super().__init__()
        self.layers = Sequential(
            # 不改变特征的HW，只改C
            Conv2d(c_in, c_out, 3, 1, 1),
            BatchNorm2d(c_out),
            LeakyReLU(),
            # Dropout(0.2)
            Conv2d(c_out, c_out, 3, 1, 1),
            BatchNorm2d(c_out),
            LeakyReLU(),
            # Dropout(0.2)
        )

    def forward(self, x):
        return self.layers(x)


class Down_sample(Module):
    def __init__(self, c):
        super().__init__()
        self.layers = Sequential(
            MaxPool2d(2),
            CNN_Block(c, c),
        )

    def forward(self, x):
        x = self.layers(x)
        return x


class Up_sample(Module):
    def __init__(self, c):
        super().__init__()
        self.layers = Sequential(
            Conv2d(c, c // 2, 3, 1, 1),
            BatchNorm2d(c // 2),
            LeakyReLU(),
            # Dropout(0.2)
        )

    def forward(self, x, r):
        data = F.interpolate(x, scale_factor=2, mode="nearest")
        data = self.layers(data)
        return torch.cat((data, r), dim=1)


class UNet(Module):
    def __init__(self):
        super().__init__()
        self.conv1 = CNN_Block(3, 64)
        self.down1 = Down_sample(64)
        self.conv2 = CNN_Block(64, 128)
        self.down2 = Down_sample(128)
        self.conv3 = CNN_Block(128, 256)
        self.down3 = Down_sample(256)
        self.conv4 = CNN_Block(256, 512)
        self.down4 = Down_sample(512)
        self.conv5 = CNN_Block(512, 1024)
        self.up1 = Up_sample(1024)

        self.conv6 = CNN_Block(1024, 512)
        self.up2 = Up_sample(512)
        self.conv7 = CNN_Block(512, 256)
        self.up3 = Up_sample(256)
        self.conv8 = CNN_Block(256, 128)
        self.up4 = Up_sample(128)
        self.conv9 = CNN_Block(128, 64)

        self.out_layer = Conv2d(64, 3, 1, 1)

    def forward(self, x):
        o1 = self.conv1(x)
        o2 = self.conv2(self.down1(o1))
        o3 = self.conv3(self.down2(o2))
        o4 = self.conv4(self.down3(o3))
        o5 = self.conv5(self.down4(o4))
        # 信息补全
        o6 = self.conv6(self.up1(o5, o4))
        o7 = self.conv7(self.up2(o6, o3))
        o8 = self.conv8(self.up3(o7, o2))
        o9 = self.conv9(self.up4(o8, o1))
        return self.out_layer(o9)
        # return o9


if __name__ == '__main__':
    data = torch.randn(8, 3, 256, 256)
    unt = UNet()

    out = unt(data)
    print(out.shape)
