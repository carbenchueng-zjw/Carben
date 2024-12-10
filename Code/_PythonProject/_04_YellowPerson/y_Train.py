import torch,os,numpy,cv2
from y_data import Y_Data
from y_Net import yNet
from PIL import Image,ImageDraw
from tqdm import tqdm
from torch.nn import *
from torch.utils.data import DataLoader
from iou import iou
from torchvision import transforms
import matplotlib.pyplot as plt
from torch.utils.tensorboard import SummaryWriter

train_data = "D:/2-Data/yellow_pic/y_train_img"
test_data = "D:/2-Data/yellow_pic/y_test_img"
save_path = "./model/step4：0.00047.pt"
device = "cuda" if torch.cuda.is_available() else "cpu"

step = 1
# print(device)

if __name__ == '__main__':
    net = yNet().cuda()
    if os.path.exists(save_path):
        net.load_state_dict(torch.load(save_path))
        print("加载预训练文件成功")

    fc_loss1= MSELoss()
    fc_loss2= BCELoss()
    # fc_loss2= CrossEntropyLoss()
    opt = torch.optim.Adam(net.parameters())

    # train_or_test = True
    train_or_test = False
    s_w = SummaryWriter("logs")
    for epoch in range(1,100):
        if train_or_test:
            net.train()
            ds = Y_Data(train_data)
            data_loader = DataLoader(ds,batch_size=300,shuffle=True)
            for i ,(img,label1,label2) in tqdm(enumerate(data_loader,1),total=len(data_loader)):
                img,label1,label2 = img.cuda(),label1.cuda(),label2.cuda()
                out1,out2 = net(img)
                # print(out2.shape,label2.shape)

                loss1 = fc_loss1(out1,label1)
                loss2 = fc_loss2(out2,label2)
                loss = loss1+loss2
                # print(loss)
                # exit()

                opt.zero_grad()
                loss.backward()
                opt.step()

                layer = net.layer[20].weight
                o1_layer = net.out_layer1[0].weight
                o2_layer = net.out_layer2[0].weight
                s_w.add_scalar("loss",loss,step)
                s_w.add_images("img",img[:10],step)
                s_w.add_histogram("weight1",layer,step)
                s_w.add_histogram("weight2",o1_layer,step)
                s_w.add_histogram("weight3",o2_layer,step)
                step+=1

                # if i%100 ==0:
                print(f"第{epoch}轮次的第{i}批次的损失：{loss}" )
                if loss <0.0008:
                    loss = round(loss,5)
                    torch.save(net.state_dict(),f"./model/step{epoch}：{loss}.pt")

        else:
            net.eval()
            ds = Y_Data(test_data)
            data_loader = DataLoader(ds,batch_size=1,shuffle=False)
            for i ,(img,label1,label2) in tqdm(enumerate(data_loader,1),total=len(data_loader)):
                img,label1 = img.cuda(),label1.cuda()
                out1,out2 = net(img)
                loss = fc_loss1(out1,label1)
                # print(loss)

                img = img[0]
                # print(img)
                # exit()
                out1 = out1[0].detach().cpu().numpy() * 300
                label1 = label1[0].detach().cpu().numpy() * 300

                iou1 = iou(out1,label1)
                if iou1 > 0.7:

                    img = transforms.ToPILImage()(img)
                    draw = ImageDraw.Draw(img)
                    draw.rectangle(xy = numpy.array(label1),outline="red",width=3)
                    draw.rectangle(xy = numpy.array(out1),outline="yellow",width=3)
                    plt.ion()
                    plt.imshow(img)
                    plt.title("yellow")
                    plt.pause(1)
                    plt.ioff()
