import torch,os,numpy as np
import torch.utils.data as data
from torch import nn
from Ai.AI_RNN.te_data import MyDataset

img_path = "data"
BATCH_SIZE = 10
EPOCH = 100
save_path = r"params/result.pkl"

class RNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = nn.Sequential(
            nn.Linear(180,128),
            nn.BatchNorm1d(128),
            nn.LeakyReLU()
        )

        self.lstm = nn.LSTM(128,128,2,batch_first=True)
        self.out = nn.Linear(128,10)

    def forward(self,x):
        x = x.reshape(-1,180,120).permute(0,2,1)#NCHW--->N,180,120--->N,120,180
        x = x.reshape(-1,180)#N,120,180--->N,180
        fc = self.fc(x)#N,128
        fc = fc.reshape(-1,120,128)#N,128--->N,120,128
        lstm_out,(hn,hc) = self.lstm(fc)#NSV
        out = lstm_out[:,-1,:]#NV

        out = out.reshape(-1,1,128)#NV--->N,1,V
        out = out.expand(-1,4,128)#NV--->N,4,V,expand是广播
        lstm_out,(hn,hc)= self.lstm(out)#N,4,246
        y1 = lstm_out.reshape(-1,128)#N,4,246--->N*4,246
        out = self.out(y1)#N*4,10
        out = out.reshape(-1,4,10)#N*4,10--->N,4,10
        return out


if __name__ == '__main__':
    # data = torch.randn(64, 3, 60, 120)
    # net1 = RNN()
    # p = net1(data)
    # exit()
    net = RNN().cuda()

    opt = torch.optim.Adam(net.parameters())
    loss_func = nn.MSELoss()

    if os.path.exists(save_path):
        net.load_state_dict(torch.load(save_path))
    train_data = MyDataset(root="data")
    train_loader = data.DataLoader(train_data,BATCH_SIZE,shuffle=True,num_workers=4)
    for epoch in range(EPOCH):
        for i,(x,y) in enumerate(train_loader):
            batch_x = x.cuda()
            batch_y = y.float().cuda()
            # print(batch_x.shape)

            out = net(batch_x)
            loss = loss_func(out,batch_y)

            opt.zero_grad()
            loss.backward()
            opt.step()

            if i%5 == 0:
                test_y = torch.argmax(y,2).detach().cpu().numpy()
                perd_y = torch.argmax(out,2).detach().cpu().numpy()
                acc = np.mean(np.all(perd_y==test_y,axis=1))
                print("epoch:",epoch,"loss:",loss,"acc:",acc)
                print("test:",test_y[0])
                print("perd:",perd_y[0])
        torch.save(net.state_dict(),save_path)













