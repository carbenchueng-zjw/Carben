import os,torch
from tqdm import tqdm
from torch import optim
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter
from torch import nn
from torch.backends import mps
from _05_DataSet import FaceDataSet
from _05_Net import *


Device = "cuda" if torch.cuda.is_available() else "cpu"

class Trainer:
    def __init__(self,net,save_path,dataset_path):
        self.net = net
        self.dataset_path = dataset_path
        self.save_path = save_path
        # print(self.save_path)
        self.summaryWriter = SummaryWriter("./logs")
        self.cls_loss_fn = nn.BCELoss()
        self.offset_loss_fn = nn.MSELoss()
        self.loss1 = 1
        self.optimizer = optim.Adam(self.net.parameters())

        if os.path.exists(self.save_path):
            net.load_state_dict(torch.load(self.save_path))
            print("加载预训练成功")
            # exit()

    def train(self):
        self.net.train()
        for epoch in range(1,1000):
            faceDateset = FaceDataSet(self.dataset_path)
            dataloader = DataLoader(faceDateset,batch_size=250,shuffle=True,drop_last=True)

            for i,(img_data_,category_,offset_) in tqdm(enumerate(dataloader,1),total=len(dataloader)):
                img_data_ = img_data_
                category_ = category_
                offset_ = offset_
                _output_category,_output_offset = self.net(img_data_)

                output_category = _output_category.reshape(-1,1)
                output_offset = _output_offset.reshape(-1,4)
                #计算分类的损失--置信度
                category_mask = torch.lt(category_,2)
                category = torch.masked_select(category_,category_mask)
                output_category = torch.masked_select(output_category,category_mask)
                cls_loss = self.cls_loss_fn(output_category,category)

                #计算bound的损失--偏移量
                offset_mask = torch.gt(category_, 0)  # 对置信度大于0的标签，进行掩码；★负样本不参与计算,负样本没偏移量;[512,1]
                offset_index = torch.nonzero(offset_mask)[:, 0]  # 选出非负样本的索引；[244]
                offset = offset_[offset_index]                   # 标签里饿偏移量；[244,4]
                output_offset = output_offset[offset_index]      # 输出的偏移量；[244,4]
                offset_loss = self.offset_loss_fn(output_offset, offset)  # 偏移量损失

                loss = cls_loss + offset_loss

                # 反向传播，优化网络
                self.optimizer.zero_grad() # 清空之前的梯度
                loss.backward()           # 计算梯度
                self.optimizer.step()    # 优化网络

                self.summaryWriter.add_scalar("loss",loss,i)
                self.summaryWriter.add_images("img",img_data_[:10],i)

                # 保存
                if i%5==0:
                #输出损失：loss-->gpu-->cup（变量）-->tensor-->array
                    print("epoch=",epoch,"i=",i ,"loss：", loss.cpu().data.numpy(), " cls_loss：", cls_loss.cpu().data.numpy(), " offset_loss",
                          offset_loss.cpu().data.numpy())

                    if loss < self.loss1:
                        loss_str = "%.5f"%loss
                        torch.save(self.net.state_dict(), f"{self.save_path}：{loss_str}.pt") # state_dict保存网络参数，save_path参数保存路径
                        self.loss1 = loss
                        print("save succeed")

if __name__ == '__main__':
    net = ONet()

    trainer = Trainer(net, "./test.pt：0.01685.pt", r"D:\2-Data\Celeba\data\48")
    trainer.train()

