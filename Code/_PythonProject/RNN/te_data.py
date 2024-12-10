import os,torch,numpy as np
import torch.utils.data as data
from PIL import Image
from torchvision import transforms

data_transforms = transforms.Compose(
    [
        transforms.ToTensor()
    ]
)

class MyDataset(data.Dataset):
    def __init__(self,root):
        self.transform = data_transforms
        self.ll = []

        for filenames in os.listdir(root):
            x = os.path.join(filenames)
            ys = filenames.split(".")
            y = self.one_hot(ys[0])
            self.ll.append([x,np.array(y)])

    def __len__(self):
        return len(self.ll)

    def __getitem__(self, item):
        img_path,label = self.ll[item]
        # print(img_path)
        img = Image.open(f'./data/{img_path}')

        img = self.transform(img)
        label = torch.from_numpy(label)
        return img,label

    def one_hot(self,x):
        z = np.zeros(shape=[4,10])

        for i in range(4):
            index = int(x[i])
            z[i][index]+=1
        return z


if __name__ == '__main__':
    mydata = MyDataset("data")
    data_loader = data.DataLoader(mydata,batch_size=1,shuffle=True)
    for i,(x,y) in enumerate(data_loader):

        print(x.shape)
        print("=========")
        print(y.shape)


