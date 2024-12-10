import torch,os,numpy,cv2
from torch.nn import *
from torchvision import transforms
from torch.utils.data import DataLoader,Dataset
from PIL import Image,ImageDraw

class Y_Data(Dataset):
    def __init__(self,path):
        super().__init__()
        self.path = path
        self.dataset = os.listdir(self.path)


    def __len__(self):
        return len(self.dataset)

    def __getitem__(self, item):
        label1 = numpy.array(self.dataset[item].split(".")[1:5],dtype=numpy.float32)/300
        # print(label1)
        # exit()
        label2 = numpy.array(self.dataset[item].split(".")[5:6],dtype=numpy.float32)
        label1,label2 = torch.Tensor(label1),torch.Tensor(label2)
        img = cv2.imread(f"{self.path}/{self.dataset[item]}")
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        # img = Image.open(f"{self.path}/{self.dataset[item]}")
        # print(type(img))
        img = transforms.ToTensor()(img)
        # print(img,type(img),img.dtype)

        return img,label1,label2


if __name__ == '__main__':
    yd = Y_Data(r"D:\2-Data\yellow_pic\y_train_img")
    yd[1]



