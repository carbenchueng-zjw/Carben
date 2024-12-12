import torch, os, numpy, cv2
from torch.nn import *
from tqdm import tqdm
from torch.utils.data import Dataset, DataLoader
from torch.utils.tensorboard import SummaryWriter
from torchvision import transforms, datasets
import torchvision.datasets.mnist as mnist
from skimage import io


# root = r"D:/2-Data/MNIST/raw/"
# train_set = mnist.read_image_file(os.path.join(root,"train-images-idx3-ubyte")),\
#     mnist.read_label_file(os.path.join(root,"train-labels-idx1-ubyte"))
# # print(train_set[0].shape)
# # print(train_set[1].shape)
#
# test_set = mnist.read_image_file(os.path.join(root,"t10k-images-idx3-ubyte")),\
#     mnist.read_label_file(os.path.join(root,"t10k-labels-idx1-ubyte"))
#
# train_path = os.path.join(root,"train")
# if not os.path.exists(train_path):
#     os.mkdir(train_path)
#
# for i,(img,label) in enumerate(zip(train_set[0],train_set[1])):
#
#     path = f"{train_path}/{label}/{i}.jpg"
#     if not os.path.exists(f"{train_path}/{label}"):
#         os.makedirs(f"{train_path}/{label}")
#
#     io.imsave(path,numpy.array(img))
#     if i%500 == 0:
#         print(f"{i}:train_succee")
#
# #测试集
# test_path = os.path.join(root,"test")
# if not os.path.exists(test_path):
#     os.mkdir(test_path)
#
# for i,(img,label) in enumerate(zip(test_set[0],test_set[1])):
#     # print(f"{train_path}")
#     # exit()
#     path = f"{test_path}/{label}/{i}.jpg"
#     if not os.path.exists(f"{test_path}/{label}"):
#         os.makedirs(f"{test_path}/{label}")
#     io.imsave(path,numpy.array(img))
#     if i%500 == 0:
#         print(f"{i}:test_succee")

class MNIST_Net(Module):
    def __init__(self):
        super().__init__()
        self.layers = Sequential(
            Linear(1 * 28 * 28, 512), ReLU(),
            Linear(512, 256), ReLU(),
            Linear(256, 128), ReLU(),
            Linear(128, 64), ReLU(),
            Linear(64, 32),ReLU(),
            Linear(32, 10),
            Softmax(dim=1)

        )

    def forward(self, x):
        return self.layers(x)


# data = torch.randn(13,1*28*28)
# print(MNIST_Net()(data).shape)

class MNIST_Dataset(Dataset):
    def __init__(self, root, is_train=True):
        super().__init__()
        self.data_set = []
        train_or_test = "train" if is_train else "test"
        path = f"{root}/{train_or_test}"
        for label in os.listdir(path):
            for img_path in os.listdir(f"{path}/{label}"):
                # print(f"{path}/{label}/{img_path}")
                self.data_set.append((f"{path}/{label}/{img_path}", label))

    def __len__(self):
        return len(self.data_set)

    def __getitem__(self, index):
        data = self.data_set[index]
        img = cv2.imread(data[0], 0)
        img = (img.reshape(-1)) / 255

        one_hot = numpy.zeros(10)
        one_hot[int(data[1])] = 1
        # print(torch.tensor(img,dtype=torch.float32).shape,
        #       torch.tensor(one_hot,dtype=torch.float32).shape)
        # exit()
        return torch.tensor(img,dtype=torch.float32), torch.tensor(one_hot,dtype=torch.float32)


class Trainer:
    def __init__(self):
        super().__init__()
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        # print(self.device)
        self.net = MNIST_Net()
        self.net.to(self.device)
        self.train_dataset = MNIST_Dataset(r"D:/2-Data/MNIST/raw/", is_train=True)
        self.train_loader = DataLoader(self.train_dataset, shuffle=True, batch_size=1024)
        self.test_dataset = MNIST_Dataset(r"D:/2-Data/MNIST/raw/", is_train=False)
        self.test_loader = DataLoader(self.test_dataset, shuffle=True, batch_size=1024)
        self.summer_writer = SummaryWriter("logs")
        self.opt = torch.optim.Adam(self.net.parameters())
        self.loss = CrossEntropyLoss()
        self.step = 1

    def train(self):
        self.net.load_state_dict(torch.load(f"parameter/Rounds37：0.00026.pt"))
        self.net.train()
        for epoch in range(1,10000):
            sum_loss = 0
            for i, (img, label) in tqdm(enumerate(self.train_loader),total=len(self.train_loader)):
                img = img.to(self.device)
                label = label.to(self.device)
                # print(label.shape)
                # exit()
                h = self.net(img)
                loss = self.loss(h,label)
                self.opt.zero_grad()
                loss.backward()
                self.opt.step()

                layer_10 = self.net.layers[0].weight
                # layer_2 = self.net.layers[0].weight
                # layer_4 = self.net.layers[0].weight
                # layer_6 = self.net.layers[0].weight
                # layer_8 = self.net.layers[0].weight

                self.summer_writer.add_histogram("layer_10",layer_10,self.step)
                # self.summer_writer.add_histogram("layer_2",layer_2,self.step)
                # self.summer_writer.add_histogram("layer_4",layer_4,self.step)
                # self.summer_writer.add_histogram("layer_6",layer_6,self.step)
                # self.summer_writer.add_histogram("layer_8",layer_8,self.step)
                self.step+=1

                sum_loss = sum_loss + loss

            avg_train_loss = sum_loss / len(self.train_loader)
            self.summer_writer.add_scalar("loss",avg_train_loss,epoch)
            print(f"这是第{epoch}轮次的损失：{avg_train_loss}")
            # if avg_train_loss < 0.00033:
            #     avg_train_loss = "%.5f"%avg_train_loss
            #     torch.save(self.net.state_dict(), f"parameter/Rounds{epoch}：{avg_train_loss}.pt")

    def test(self):
        self.net.eval()
        self.net.load_state_dict(torch.load("parameter/Rounds33：0.00029.pt"))
        for epoch in range(1,10000):
            sum_score = 0
            for i, (img, label) in tqdm(enumerate(self.test_loader,1),total=len(self.test_loader)):
                img, label = img.to(self.device), label.to(self.device)
                h = self.net(img)
                a = torch.argmax(h, dim=1)
                b = torch.argmax(label, dim=1)
                score = torch.mean(torch.eq(a, b).float())
                sum_score = sum_score + score
                avg_test_score = sum_score / len(self.test_loader)
            print(f"这是第{epoch}轮次的得分：{avg_test_score}")


if __name__ == '__main__':
    train = Trainer()
    train.train()
    # train.test()
    # print(MNIST_Net())