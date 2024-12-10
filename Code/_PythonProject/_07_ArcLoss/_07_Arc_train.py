import torch,torchvision
from torch.nn import *
from torch.utils import data
from matplotlib import pyplot as plt
from _07_ArcLoss import *
from _07_ArcLoss_net import *
from torch.backends import mps

Deivce = torch.device("mps" if mps.is_available() else "cpu")

train_data = torchvision.datasets.MNIST(root="/Users/carbenchueng/Desktop/2-Data",
                                        train=True, download=False,
                                        transform=torchvision.transforms.ToTensor())

train_loader = data.DataLoader(dataset = train_data,shuffle = True,batch_size = 500)

if __name__ == '__main__':
    net = Net().to(Deivce)
    arc = Arc(2,10).to(Deivce)

    opt_net  = torch.optim.Adam(net.parameters())
    opt_arc  = torch.optim.Adam(arc.parameters())

    loss_nll = NLLLoss()
    plt.ion()
    epoch = 0
    while True:
        for i,(data,target) in enumerate(train_loader):
            data,target = data.to(Deivce),target.to(Deivce)
            layer = net(data)
            out = arc(layer)

            c = ["#ff0000", "#ffff00", "#00ff00", "#00ffff", "#0000ff",
                 "#ff00ff", "#990000", "#999900", "#009900", "#009999"]
            plt.clf()
            for j in range(10):
                plt.plot(layer[target == j, 0].detach().cpu().numpy(), layer[target == j, 1].detach().cpu().numpy(), ".", c=c[j])
            plt.legend(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"], loc="upper right")

            loss = loss_nll(out,target)
            opt_arc.zero_grad()
            opt_net.zero_grad()
            loss.backward()
            opt_arc.step()
            opt_net.step()


            plt.title(f"{epoch}")
            if i %500 == 0:
                print(loss.item())
                plt.savefig(f"./_07_images/{epoch}.jpg")
                torch.save(net.state_dict(),f"./_07_weight/{epoch}.pt")
            epoch+=1









