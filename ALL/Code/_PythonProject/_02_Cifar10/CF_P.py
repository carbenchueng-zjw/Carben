import numpy, torch
from tqdm import tqdm
from torch.nn import *
from torch.utils.tensorboard import SummaryWriter
from torchvision import datasets, transforms
from torch.utils.data import DataLoader
from torch.optim import Adam


class CF_Net(Module):
    def __init__(self):
        super().__init__()
        self.layers = Sequential(
            Conv2d(3, 16, 3,1,1,padding_mode="reflect"), ReLU(),
            Conv2d(16, 32, 3,1,1), ReLU(),
            Conv2d(32, 64, 3), ReLU(),
            Conv2d( 64,128, 3), ReLU(),
            Conv2d( 128,256, 3),

        )

        self.out_layer = Sequential(
            Linear(256*26*26,10),
            # Softmax(dim=1)
        )

    def forward(self, x):
        h = self.layers(x)
        h = h.reshape(h.size(0),-1)
        out = self.out_layer(h)
        # print(type(out),out.shape,sep="\n")
        return out

class Trainer:
    def __init__(self):
        super().__init__()
        self.summer_writer = SummaryWriter("logs")
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.net = CF_Net().to(self.device)
        self.train_data = datasets.CIFAR10(root="D:/2-Data/", train=True, transform=transforms.ToTensor(),
                                           download=False)
        self.test_data = datasets.CIFAR10(root="D:/2-Data/", train=False, transform=transforms.ToTensor(),
                                          download=False)
        self.train_loader = DataLoader(self.train_data, batch_size=512, shuffle=True)
        self.test_loader = DataLoader(self.test_data, batch_size=10, shuffle=False)
        self.opt = Adam(self.net.parameters())
        self.loss = CrossEntropyLoss()


    def train(self):
        self.net.train()
        # self.net.load_state_dict(torch.load("./prarm/Rounds85：0.00002.pt"))
        for epoch in range(1,1001):
            sum_loss = 0.
            for i, (img, label) in tqdm(enumerate(self.train_loader),total=len(self.train_loader)):
                img, label = img.to(self.device), label.to(self.device)
                h = self.net(img)
                loss = self.loss(h, label)

                self.opt.zero_grad()
                loss.backward()
                self.opt.step()

                sum_loss = sum_loss + loss
            avg_train_loss = sum_loss / (len(self.train_loader))
            print(f"第{epoch+1}轮的损失是：{avg_train_loss}")
            self.summer_writer.add_scalar("loss",avg_train_loss,epoch)
            self.summer_writer.add_images("img",img[:40],epoch)
            avg_train_loss = "%.5f"%avg_train_loss
            torch.save(self.net.state_dict(),f"./prarm/Rounds{epoch}：{avg_train_loss}.pt")

    def test(self):
        self.net.load_state_dict(torch.load(f"./prarm/Rounds85：0.00002.pt"))
        self.net.eval()
        for epoch in range(1,10000):
            sum_score = 0
            for i,(img,label) in tqdm(enumerate(self.test_loader,1),total=len(self.test_loader)):
                img,label = img.to(self.device), label.to(self.device)
                # print(label)
                # print(img.shape)
                # exit()
                out = self.net(img)
                a = torch.argmax(out,dim=1)
                # b = torch.argmax(label)
                score = torch.mean(torch.eq(a,label).float())
                # print(score)
                # exit()
                sum_score = sum_score+score
                avg_test_score = sum_score/len(self.test_loader)
            print(f"第{epoch}得分是：{avg_test_score}")


if __name__ == '__main__':
    # net = CF_Net()
    # data = torch.randn(12, 3, 32, 32)
    # y = net(data)
    trainer = Trainer()
    # trainer.train()
    trainer.test()

    # train_data = datasets.CIFAR10(root="D:/2-Data/", train=False, transform=transforms.ToTensor(),
    #                               download=False)
    # test_loader = DataLoader(train_data, batch_size=100, shuffle=True)
    # print(test_loader.dataset.data.shape)