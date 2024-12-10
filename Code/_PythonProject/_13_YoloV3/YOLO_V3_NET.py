import torch
from torch.nn import *


class Up_sample_layer(Module):
    def __init__(self):
        super().__init__()

    def forward(self,x):
        return torch.nn.functional.interpolate(x,scale_factor=2,mode="nearest")

class Convolutional_layer(Module):
    def __init__(self,c_in,c_out,ker_size,strid,padding,bias=False):
        super().__init__()
        self.con_layer = Sequential(
            Conv2d(c_in,c_out,ker_size,strid,padding,bias=bias),
            BatchNorm2d(c_out),
            LeakyReLU(0.1),
        )
    def forward(self,x):
        return self.con_layer(x)

class Residua_layer(Module):
    def __init__(self,c_in):
        super().__init__()
        self.con_layer = Sequential(
            Convolutional_layer(c_in,c_in//2,1,1,0),
            Convolutional_layer(c_in//2,c_in,3,1,1),
        )
    def forward(self,x):
        return self.con_layer(x) + x

class Down_sample_layer(Module):
    def __init__(self,c_in,c_out):
        super().__init__()
        self.con_layer = Sequential(
        Convolutional_layer(c_in,c_out,3,2,1),
    )

    def forward(self,x):
        return self.con_layer(x)

class Convolutional_set(Module):
    def __init__(self,c_in,c_out):
        super().__init__()
        self.con_layer = Sequential(
            Convolutional_layer(c_in,c_out,1,1,0),
            Convolutional_layer(c_out,c_in,3,1,1),
            Convolutional_layer(c_in,c_out,1,1,0),
            Convolutional_layer(c_out,c_in,3,1,1),
            Convolutional_layer(c_in,c_out,1,1,0),
        )
    def forward(self,x):
        return self.con_layer(x)


class Dark_net53(Module):
    def __init__(self):
        super().__init__()

        self.trunk_52 = Sequential(
            Convolutional_layer(3,32,1,1,0),
            Convolutional_layer(32,64,3,2,1),
            Residua_layer(64),
            Down_sample_layer(64,128),
            Residua_layer(128),
            Residua_layer(128),
            Down_sample_layer(128,256),
            Residua_layer(256),
            Residua_layer(256),
            Residua_layer(256),
            Residua_layer(256),
            Residua_layer(256),
            Residua_layer(256),
            Residua_layer(256),
            Residua_layer(256),
        )

        self.trunk_26 = Sequential(
            Down_sample_layer(256,512),
            Residua_layer(512),
            Residua_layer(512),
            Residua_layer(512),
            Residua_layer(512),
            Residua_layer(512),
            Residua_layer(512),
            Residua_layer(512),
            Residua_layer(512),
        )

        self.trunk_13 = Sequential(
            Down_sample_layer(512,1024),
            Residua_layer(1024),
            Residua_layer(1024),
            Residua_layer(1024),
            Residua_layer(1024),
        )

        self.conv_set_13 = Sequential(
            Convolutional_set(1024,512)
        )
        self.deteion_13 = Sequential(
            Convolutional_layer(512,1024,3,1,1),
            Conv2d(1024,45,1,1,0)
        )
        self.up_26 = Sequential(
            Convolutional_layer(512,256,3,1,1),
            Up_sample_layer(),
        )
        self.conv_set_26 = Sequential(
            Convolutional_set(768,256),
        )
        self.deteion_26 = Sequential(
            Convolutional_layer(256,512,3,1,1),
            Conv2d(512,45,1,1,0)
        )

        self.up_52 = Sequential(
            Convolutional_layer(256,128,3,1,1),
            Up_sample_layer(),
        )
        self.conv_set_52 = Sequential(
            Convolutional_set(384,128),
        )
        self.deteion_52 = Sequential(
            Convolutional_layer(128,256,3,1,1),
            Conv2d(256,45,1,1,0)
        )
    def forward(self,x):
        h_52 = self.trunk_52(x)
        h_26 = self.trunk_26(h_52)
        h_13 = self.trunk_13(h_26)

        convset_out_13 = self.conv_set_13(h_13)
        detetion_out_13 = self.deteion_13(convset_out_13)

        up_out_26 = self.up_26(convset_out_13)
        route_out_26 = torch.cat((up_out_26,h_26),dim=1)
        convset_out_26 = self.conv_set_26(route_out_26)
        detetion_out_26 = self.deteion_26(convset_out_26)


        up_out_52 = self.up_52(convset_out_26)
        route_out_52 = torch.cat((up_out_52,h_52),dim=1)
        convset_out_52 = self.conv_set_52(route_out_52)
        detetion_out_52 = self.deteion_52(convset_out_52)

        return  detetion_out_13,detetion_out_26,detetion_out_52

if __name__ == '__main__':
    yolo = Dark_net53()
    x = torch.randn(1,3,416,416)
    y = yolo(x)
    print(y[0].shape)
    print(y[1].shape)
    print(y[2].shape)







