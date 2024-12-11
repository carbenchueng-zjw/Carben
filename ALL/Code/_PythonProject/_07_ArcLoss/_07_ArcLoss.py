import torch
from torch.nn import *


class Arc(Module):

    def __init__(self,feat_num,cls_num):
        super().__init__()
        self.w = Parameter(torch.randn(feat_num,cls_num))
        # print(self.w)

    def forward(self,x,m=1,s=10):
        x_norm = functional.normalize(x,dim=1)
        w_norm = functional.normalize(self.w,dim=0)

        #除以10，为了防止梯度爆炸
        cos = torch.matmul(x_norm,w_norm)/10
        a = torch.arccos(cos)

        top = torch.exp(s*torch.cos(a+m))
        # down = top + torch.sum(torch.exp(s*torch.cos(a)),dim=1,keepdim=True)-torch.exp(s*torch.cos(a))
        down = top + torch.sum(torch.exp(s*cos),dim=1,keepdim=True)-torch.exp(s*cos)
        arc_soft_max = torch.log(top/down)

        return arc_soft_max

if __name__ == '__main__':
    aarc = Arc(2,10)
    # print(aarc)
    data = torch.randn(1,2)
    out = aarc(data)
    print(out)
    print(data)
    print(torch.sum(out))
