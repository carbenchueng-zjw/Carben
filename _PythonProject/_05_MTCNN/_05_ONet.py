from _05_Net import ONet
from _05_Train import Trainer


if __name__ == '__main__':
    o_net = ONet()
    trainer = Trainer(o_net, f"./parameter/onet.pt", r"D:\2-Data\Celeba\data\48")
    trainer.train()
