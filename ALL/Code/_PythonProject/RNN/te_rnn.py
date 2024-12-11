import torch
from torch import nn

#        RNN(input,隐藏的尺寸（神经元的个数），网络层数)
rnn = nn.RNN(10,5,6,batch_first=True)#用NSV，没有TRUE那就是SNV

ii = torch.randn(50,30,10)#序列，状态，长度（input）
h0 = torch.zeros(6,50,5)

out,hn = rnn(ii,h0)
print(out.shape)
print(hn.shape)