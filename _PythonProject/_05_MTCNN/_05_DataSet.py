import os, numpy, torch
from torch.utils.data import Dataset
from PIL import Image
from torchvision.transforms import *


class FaceDataSet(Dataset):

    def __init__(self, path):
        self.path = path
        self.data_set = []
        self.data_set.extend(open(os.path.join(self.path, "positive.txt")).readlines())
        self.data_set.extend(open(os.path.join(self.path, "part.txt")).readlines())
        self.data_set.extend(open(os.path.join(self.path, "negative.txt")).readlines())

    def __len__(self):
        return len(self.data_set)

    def __getitem__(self, item):
        strs = self.data_set[item].split()
        # print(strs)
        cond = torch.Tensor([int(strs[1])])
        offset = torch.Tensor([float(strs[2]), float(strs[3]), float(strs[4]), float(strs[5])])
        # print(type(offset))
        # print(offset)
        img_path = os.path.join(self.path, strs[0])
        img_data = Image.open(img_path)
        img_data = ToTensor()(img_data)

        # img_data = torch.Tensor(numpy.array(Image.open(img_path)) / 255 )
        # img_data = img_data.permute(2, 0, 1)
        return img_data, cond, offset


if __name__ == '__main__':
    data = FaceDataSet(r"D:\2-Data\Celeba\test\test_save\48")
    print(data[6][0].shape)
    print(data[6][1].shape)
    print(data[6][2].shape)
