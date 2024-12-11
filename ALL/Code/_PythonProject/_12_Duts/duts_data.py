# data  D:/2-Data/duts/DUTS-TR/DUTS-TR-Image
# label D:/2-Data/duts/DUTS-TR/DUTS-TR-Mask
import torch, os
from torch.utils.data import Dataset
from torchvision.utils import save_image
from torchvision import transforms
from PIL import Image
from tqdm import tqdm

transform = transforms.Compose([
    transforms.ToTensor()
])
data_path = "D:/2-Data/duts/DUTS-TR/DUTS-TR-Image"
label_path = "D:/2-Data/duts/DUTS-TR/DUTS-TR-Mask"
duta_train_path = "D:/2-Data/duts/DUTS-TR/DUTS-TR-Train"

class Duts_Dataset(Dataset):
    def __init__(self):
        super().__init__()

        self.data_path = data_path
        self.label_path = label_path
        # print(self.name)

    def __len__(self):
        return len(os.listdir(self.data_path))

    def __getitem__(self, index):
        bg1 = transforms.ToPILImage()(torch.zeros(3, 256, 256))
        bg2 = transforms.ToPILImage()(torch.zeros(3, 256, 256))
        datas = os.listdir(self.data_path)
        labels = os.listdir(self.label_path)

        data_path = f"{self.data_path}/{datas[index]}"
        label_path = f"{self.label_path}/{labels[index]}"
        img1 = Image.open(data_path)
        img2 = Image.open(label_path)
        img_size = torch.Tensor(img1.size)
        ratio = 256 / img_size[img_size.argmax()]
        img_size = (img_size * ratio).long()
        img1 = img1.resize(img_size)
        img2 = img2.resize(img_size)

        bg1.paste(img1, (0, 0))
        bg2.paste(img2, (0, 0))
        # bg1.show()
        # exit()
        return transform(bg1), transform(bg2)


if __name__ == '__main__':
    ds = Duts_Dataset()
    i = 1
    for (data, label) in tqdm(ds, total=len(ds)):
        save_image(data, f"{duta_train_path}/{i}.jpg", nrow=1)
        save_image(label, f"{duta_train_path}/{i}.png", nrow=1)
        i += 1
