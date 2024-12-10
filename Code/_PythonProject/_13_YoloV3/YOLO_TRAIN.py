import os, torch
from torch.utils.data import DataLoader
from YOLO_V3_NET import Dark_net53
from YOLO_DATA_SET import YoloData
from torch.nn import *


class YoloTrain:
    def __init__(self):
        super().__init__()
        self.save_path = "./models/test.pt"
        self.net = Dark_net53().cuda()
        if os.path.exists(self.save_path):
            self.net.load_state_dict(torch.load(self.save_path))
        self.train_data = YoloData()
        self.train_loader = DataLoader(self.train_data, batch_size=3, shuffle=True)
        self.conf_loss = BCEWithLogitsLoss()  # 置信度损失
        self.crood_loss = MSELoss()  # 偏移量损失
        self.cls_loss = CrossEntropyLoss()  # 分类损失
        self.opt = torch.optim.Adam(self.net.parameters())

    def loss_fn(self, output, target, alpha):
        output = output.permute(0, 2, 3, 1)
        output = output.reshape(output.size(0), output.size(1), 3, -1)
        mask_obj = target[..., 0]>0

        output_obj = output[mask_obj]
        target_obj = target[mask_obj]
        loss_obj_conf = self.conf_loss(output_obj[:, 0], target_obj[:, 0])
        loss_obj_crood = self.crood_loss(output_obj[:, 1:5], target_obj[:, 1:5])
        loss_obj_cls = self.cls_loss(output_obj[:, 5:], torch.argmax(target_obj[:, 5:]), dim=1)
        loss_obj = loss_obj_conf + loss_obj_crood + loss_obj_cls

        mask_noobj = target[..., 0] == 0
        output_noobj = output[mask_noobj]
        target_noobj = target[mask_noobj]

        loss_noobj = self.conf_loss(output_noobj[:,0],target_noobj[:,0])
        loss = alpha*loss_obj+(1-alpha)*loss_noobj
        return loss

    def train(self):
        self.net.train()
        epoch = 1
        while True:
            print(epoch)
            for target_13,target_26,target_52,img_data in self.train_loader:
                target_13,target_26,target_52,img_data = target_13.cuda(),target_26.cuda(),target_52.cuda(),img_data.cuda()
                output_13,output_26,output_52 = self.net(img_data)
                loss_13 = self.loss_fn(output_13,target_13,0.9)
                loss_26 = self.loss_fn(output_26,target_26,0.9)
                loss_52 = self.loss_fn(output_52,target_52,0.9)
                loss = loss_13+loss_26+loss_52

                self.opt.zero_grad()
                loss.backward()
                self.opt.step()
                print(loss.item())

            if epoch %10==0:
                torch.save(self.net.state_dict(),self.save_path.format(epoch))
            epoch+=1

if __name__ == '__main__':
    pass