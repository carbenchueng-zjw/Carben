import torch
from torch import nn

lstm = nn.LSTM(10,5,6,batch_first=True)#用NSV，没有TRUE那就是SNV
ii = torch.randn(50,30,10)
h0 = torch.randn(6,50,5)
c0 = torch.randn(6,50,5)

# out,(hn,cn) = lstm(ii,(h0,c0))
out,(hn,cn) = lstm(ii)
print(out.shape)
print(hn.shape)
print(cn.shape)