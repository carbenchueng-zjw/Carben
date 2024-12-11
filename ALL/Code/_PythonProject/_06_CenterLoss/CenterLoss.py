import torch, matplotlib.pyplot as plt, torchvision,os
from torch.nn import *
from torchvision import transforms
from torch.utils.data import *
from torch.backends import mps


save_path = "./center_loss.pt"

class CenterLoss(Module):

    def __init__(self,cls_num,feature_num):
        super().__init__()
        self.center = Parameter(torch.randn(cls_num,feature_num))
        self.cls_num = cls_num
        # self.feature_num = feature_num
        # print(self.center,self.cls_num)

    def forward(self,xs,ys):
        # xs = torch.nn.functional.normalize(xs)
        center_exp = self.center.index_select(dim=0,index = ys.long())
        count = torch.histc(ys,bins=self.cls_num,min=0,max=self.cls_num-1)
        # print(center_exp)
        count_exp = count.index_select(dim=0,index = ys.long())
        center_loss = torch.sum(torch.div(torch.sqrt(torch.sum((torch.pow(xs-center_exp,2)),dim=1)),count_exp))

        return center_loss

class Net(Module):

    def __init__(self):
        super().__init__()
        self.fc1 = Sequential(
            # Linear(32*32*3,512),
            Linear(784,512),
            PReLU(),
            Linear(512,256),
            PReLU(),
            Linear(256,128),
            PReLU(),
            Linear(128,64),
            PReLU(),
            Linear(64,2),
        )

        self.fc2 = Sequential(
            Linear(2,10),
            # Softmax(dim=1)
        )

        self.center_loss = CenterLoss(10,2)
        self.cross_entropy_loss = CrossEntropyLoss()
        # self.fc1 = Sequential(
        #     Conv2d(1,26,3),
        #     ReLU(),
        #     Conv2d(26,32,3),
        #     ReLU(),
        #     Conv2d(32, 64,3),
        #     ReLU(),
        #     Conv2d(64,128, 3),
        #
        # )
        # self.out1 = Sequential(
        #     Linear(128*20*20, 2),
        #     # Softmax(dim=1)
        # )
        # self.out2 = Sequential(
        #     Linear(128*20*20, 10),
        #     # Softmax(dim=1)
        # )
        #
        # self.center_loss = CenterLoss(10,2)
        # self.cross_entropy_loss = CrossEntropyLoss()

    def forward(self, x):
        features = self.fc1(x)
        outputs = self.fc2(features)
        return features, outputs

    def GetLoss(self,outputs,features,labels):
        loss_cls = self.cross_entropy_loss(outputs,labels)
        loss_center = self.center_loss(features,labels)
        loss = loss_cls+loss_center

        return loss

def Visualize(feat, label, epoch):
    plt.ion()
    c = ["#ff0000", "#ffff00", "#00ff00", "#00ffff", "#0000ff",
         "#ff00ff", "#990000", "#999900", "#009900", "#009999"]
    plt.clf()
    for s in range(10):
        plt.plot(feat[s == label, 0], feat[s == label, 1], ".", c=c[s])
        # exit()
    plt.legend(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"], loc="upper right")
    plt.title(f"{epoch}")
    plt.savefig(f"./canter_loss_img/{epoch}.jpg")
    plt.draw()
    plt.pause(0.001)


if __name__ == '__main__':
    Device = torch.device("mps" if mps.is_available() else "cpu")
    # x = torch.randn(3,1,28,28)
    train_data = torchvision.datasets.MNIST(root="/Users/carbenchueng/Desktop/2-Data",
                                            train=True, download=True,
                                            transform=transforms.ToTensor())

    train_load = DataLoader(train_data, shuffle=True, batch_size=512)
    net = Net().to(Device)
    # if os.path.exists("./clw/center_loss.pt"):
    #     net.load_state_dict(torch.load("clw/center_loss.pt"))

    # loss_func = MSELoss()
    # loss_func = CrossEntropyLoss()

    opt = torch.optim.Adam(net.parameters())
    # opt = torch.optim.SGD(net.parameters(),lr=0.0001,weight_decay=0.0005)

    epoch = 0
    while True:
        feat_loader = []
        label_loader = []
        for i, (x, y) in enumerate(train_load):
            x = x.reshape(-1,784).to(Device)
            # target = functional.one_hot(y, 10).float()
            target = y.to(Device)
            feat, out = net(x)
            # loss = loss_func(out,target)
            loss = net.GetLoss(out,feat,target)
            # exit()

            opt.zero_grad()
            loss.backward()
            opt.step()

            feat_loader.append(feat)
            label_loader.append(y)

            if i % 10 == 0:
                print(loss.item())

        feat = torch.cat(feat_loader, 0)
        label = torch.cat(label_loader, 0)

        Visualize(feat.detach().cpu().numpy(), label.detach().cpu().numpy(), epoch)
        torch.save(net.state_dict(),f"./clw/{epoch}.pt")
        epoch += 1
