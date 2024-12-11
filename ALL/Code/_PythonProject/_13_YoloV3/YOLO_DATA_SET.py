import torch,torchvision,CFG,math,os,numpy
from torch.nn.functional import one_hot
from torch.utils.data import Dataset,DataLoader
from PIL import Image

LABEL_FILE_PATH = ""
IMG_BASE_DIR = ""

transforms = torchvision.transforms.Compose([
    torchvision.transforms.ToTensor()
])

class YoloData(Dataset):
    def __init__(self):
        with open(LABEL_FILE_PATH) as f:
            self.data_set = f.readlines()

    def __len__(self):
        return len(self.data_set)

    def __getitem__(self, index):
        labels = {}
        line = self.data_set[index]
        strs = line.split()

        _img_data = Image.open(os.path.join(IMG_BASE_DIR,strs[0]))
        img_data = transforms(_img_data)
        _boxes = numpy.array(list(map(float,strs[1:])))
        boxes = numpy.split(_boxes,len(_boxes)//5)

        for feature_size,anchors in CFG.ANCHORS_GROUP.items():
            labels[feature_size] = numpy.zeros(shape=(feature_size,feature_size,
                                                      3,5+CFG.CLASS_NUM),dtype=numpy.float32)
            for box in boxes:
                cls,cx,cy,w,h = box
                cx_offset,cx_index = math.modf(cx*feature_size/CFG.IMG_WIDTH)
                cy_offset,cy_index = math.modf(cy*feature_size/CFG.IMG_WIDTH)
                for i ,anchor in enumerate(anchors):
                    anchor_area = CFG.ANCHORS_GROUP_AREA[feature_size][i]
                    p_w,p_h = w/anchor[0],h/anchor[1]
                    p_area = p_w*p_h
                    iou = min(p_area,anchor_area)/max(p_area,anchor_area)
                    labels[feature_size][int(cy_index),int(cx_index),i] = numpy.array(
                        [iou,cx_offset,cy_offset,numpy.log(p_w),numpy.log(p_h),
                         *one_hot(int(cls),CFG.CLASS_NUM)]
                    )
        return labels[13],labels[26],labels[52]

if __name__ == '__main__':
    yd = YoloData()
    


