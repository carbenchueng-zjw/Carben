# D:/2-Data/VOC2012/JPEGImages/2007_000033.jpg
# D:/2-Data/VOC2012/SegmentationClass/2007_000033.png
import torch, os
from torch.utils.data import Dataset
from torchvision.utils import save_image
from torchvision import transforms
from PIL import Image
from tqdm import tqdm


transform = transforms.Compose([
    transforms.ToTensor()
])
class VOC_Dataset(Dataset):
    def __init__(self,path=r"D:\2-Data\VOC2012"):
        super().__init__()
        self.path = path
        self.name = os.listdir(os.path.join(self.path,"SegmentationClass"))
        # print(self.name)

    def __len__(self):
        return len(self.name)

    def __getitem__(self, index):
        bg1 = transforms.ToPILImage()(torch.zeros(3,256,256))
        bg2 = transforms.ToPILImage()(torch.zeros(3,256,256))
        # print(bg1.save)
        name_label = self.name[index]
        name_data = name_label[:-3]+"jpg"
        # img1_path = rf"{self.path}\JPEGImages"
        img1_path = os.path.join(self.path,"JPEGImages")
        # print(img1_path)
        # exit()
        img2_path = os.path.join(self.path,"SegmentationClass")
        img1 = Image.open(os.path.join(img1_path,name_data))
        img2 = Image.open(os.path.join(img2_path,name_label))
        img1_size = torch.Tensor(img1.size)
        max_index = img1_size.argmax()

        #压缩比例
        ratio = 256/img1_size[max_index]

        img1_size = img1_size*ratio
        img1_size = img1_size.long()
        img1 = img1.resize(img1_size)
        img2 = img2.resize(img1_size)

        bg1.paste(img1,(0,0))
        bg2.paste(img2,(0,0))
        # bg1.show()
        # exit()
        return transform(bg1),transform(bg2)

if __name__ == '__main__':
    path = r"D:\2-Data\VOC2012\train"
    ds = VOC_Dataset()
    i = 1
    for (data,label) in tqdm(ds,total=len(ds)):
        save_image(data,f"{path}/{i}.jpg",nrow=1)
        save_image(label,f"{path}/{i}.png",nrow=1)
        i+=1





