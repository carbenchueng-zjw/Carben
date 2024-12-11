import torch,os
from torch.utils.data import DataLoader
from torchvision.utils import save_image
from tqdm import tqdm
from voc_data import VOC_Dataset
from UNet import *

module = "./params/unet_voc/unet_voc.pt"
img_save = "./train_img/unet_voc"
# li = os.listdir(module)
# print(li)
net = UNet().cuda()
opt = torch.optim.Adam(net.parameters())
fc_loss = MSELoss()
voc_dataloader = DataLoader(VOC_Dataset(),batch_size=16,shuffle=False)

if os.path.exists(module):
    net.load_state_dict(torch.load(module))
    print("加载预训练成功")
def train():
    net.train()
    for epoch in range(1,10000):
        for i,(data,label) in tqdm(enumerate(voc_dataloader,1),total=len(voc_dataloader)):
            data,label = data.cuda(),label.cuda()
            out = net(data)
            loss = fc_loss(out,label)

            opt.zero_grad()
            loss.backward()
            opt.step()

            if i %100 == 0:
                print(f"这是第{epoch}轮次第{i}批次的损失：{loss}")
                # if loss < 0.003:
                #     loss = "%5f"%loss
                #     torch.save(net.state_dict(),f"./params/Rounds{epoch}: {loss}.pt")
        x = data[0]
        y = label[0]
        o = out[0]
        img = torch.stack((x,y,o),dim=0)
        save_image(img.cpu(),f"{img_save}/{epoch}.jpg")

        torch.save(net.state_dict(),module)
        print("保存成功")

if __name__ == '__main__':
    train()


