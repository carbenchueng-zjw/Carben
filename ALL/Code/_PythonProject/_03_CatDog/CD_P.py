import torch, cv2, os
from tqdm import tqdm
from torch.nn import *
from torch.nn.functional import one_hot
from torch.utils.data import Dataset, DataLoader
from torch.utils.tensorboard import SummaryWriter


class CD_Net(Module):
    def __init__(self):
        super().__init__()
        self.layers = Sequential(
            Linear(3*100*100, 15000), ReLU(),
            Linear(15000, 7500), ReLU(),
            Linear(7500, 3500), ReLU(),
            Linear(3500, 1200), ReLU(),
            Linear(1200, 600), ReLU(),
            Linear(600, 300), ReLU(),
            Linear(300, 150), ReLU(),
            Linear(150, 75), ReLU(),
            Linear(75, 2),
            # Sigmoid(),
            Softmax(dim=1)

        )

    def forward(self, x):
        # print(self.layers(x))
        return self.layers(x)


class CD_Data(Dataset):
    def __init__(self, root, is_train=True):
        super().__init__()
        self.dataset = []
        train_or_test = "train" if is_train else "test"
        self.path = f"{root}/{train_or_test}"
        for i in os.listdir(self.path):
            label = i.split(".")[0]
            self.dataset.append([f"{self.path}/{i}", label])

            # print(self.dataset)
            # if len(self.dataset) > 1:
            #     break

    def __len__(self):
        return len(self.dataset)

    def __getitem__(self, item):
        data = self.dataset[item]
        img = cv2.imread(data[0])
        # img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        # print(img.shape)
        # h,w = img.shape
        # img = cv2.resize(img,(h//2,w//2))

        # print(img.shape)
        img = img / 255
        img = img.reshape(-1)
        one_hot = torch.zeros(2)
        one_hot[int(data[1])] = 1
        # print(one_hot)
        return torch.Tensor(img), torch.Tensor(one_hot)


class CD_Train():
    def __init__(self):
        super().__init__()
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.net = CD_Net().to(self.device)
        self.train_data = CD_Data(r"D:/2-Data/cat_dog_img", True)
        self.test_data = CD_Data(r"D:/2-Data/cat_dog_img", False)
        self.train_loader = DataLoader(self.train_data, batch_size=512, shuffle=True)
        self.test_loader = DataLoader(self.test_data, batch_size=112, shuffle=True)
        self.opt = torch.optim.Adam(self.net.parameters())
        self.summery_writer = SummaryWriter("logs")
        self.loss = MSELoss()
        # self.loss = CrossEntropyLoss()

    def Train(self):
        self.net.train()
        self.net.load_state_dict(torch.load(f"./prarm/Rounds68：0.02286.pt"))
        for epoch in range(1,10000):
            sum_loss = 0
            for i,(img,label) in tqdm(enumerate(self.train_loader),total=len(self.train_loader)):
                img, label = img.to(self.device), label.to(self.device)
                out = self.net(img)
                loss = self.loss(out, label)

                self.opt.zero_grad()
                loss.backward()
                self.opt.step()

                sum_loss = sum_loss + loss
            avg_train_loss = sum_loss / len(self.train_loader)

            self.summery_writer.add_scalar("loss", avg_train_loss, epoch)
            # self.summery_writer.add_images("images", img[:10], epoch)

            # if avg_train_loss < 0.00045:
            # avg_train_loss = "%.5f" % avg_train_loss
            # torch.save(self.net.state_dict(), f"./parameter/Rounds{epoch}：{avg_train_loss}.pt")
            print(f"第{epoch+1}轮的损失是：{avg_train_loss}")
    def Test(self):
        self.net.eval()
        self.net.load_state_dict(torch.load(f"./prarm/0.034.pt"))
        for epoch in range(1,10000):
            sum_score = 0
            for i,(img,label) in tqdm(enumerate(self.test_loader,1),total=len(self.test_loader)):
                img, label = img.to(self.device), label.to(self.device)
                # print(label.shape)
                # exit()
                out = self.net(img)
                a = torch.argmax(out,dim=1)
                b = torch.argmax(label,dim=1)
                score = torch.mean(torch.eq(a,b).float())
                sum_score = sum_score+score
            avg_test_score = sum_score/len(self.test_loader)
            print(f"这是第{epoch}轮次的得分：{avg_test_score}")

if __name__ == '__main__':
    # cd_d = CD_Data(r"D:/2-Data/cat_dog_img",False)[1020]
    # print(cd_d.dataset[0])
    # net = CD_Net()
    # x = torch.randn(6,3*100*100)
    # y = net(x)
    # print(y)
    train = CD_Train()
    # train.Train()
    train.Test()
