from _05_Net import PNet
from _05_Train import Trainer


if __name__ == '__main__':
    p_net = PNet()
    trainer = Trainer(p_net, "parameter/pnet.pt：0.02885.pt", r"D:\2-Data\Celeba\data\12")
    trainer.train()