import CFG, torch, numpy, os
from YOLO_V3_NET import *
from PIL import ImageDraw, Image, ImageFont
from matplotlib import pyplot as plt


class Detector(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.net = Dark_net53().cuda()
        self.net.load_state_dict(torch.load("./models", map_location="cuda"))
        self.net.eval()

    def forward(self, input_data, thresh, anchors):
        output_13, output_26, output_52 = self.net(input_data)
        idxs_13, vecs_13 = self._filter(output_13, thresh)
        boxes_13 = self._parse(idxs_13,vecs_13,32,anchors[13])
        idxs_26, vecs_26 = self._filter(output_26, thresh)
        boxes_26 = self._parse(idxs_26,vecs_26,16,anchors[26])
        idxs_52, vecs_52 = self._filter(output_52, thresh)
        boxes_52 = self._parse(idxs_52,vecs_52,8,anchors[52])

        return torch.cat([boxes_13,boxes_26,boxes_52],dim=0)

    def _filter(self, output, thresh):
        output = output.permute(0, 2, 3, 1)
        output = output.reshpe(output.size(0), output.size(1), output.size(2), 3, -1)
        mask = output[..., 0] > thresh
        idxs = mask.nonzero()
        vecs = output[mask]
        return idxs, vecs

    def _parse(self, idxs, vecs, t, anchors):
        anchors = torch.Tensor(anchors).cuda()
        a = idxs[:, 3]
        confidence = torch.sigmoid(vecs[:, 0])

        _classify = vecs[:5:]
        if len(_classify) == 0:
            classify = torch.Tensor([]).cuda()
        else:
            classify = torch.argmax(_classify, dim=1).float()
        cy = (idxs[:, 1].float() + vecs[:, 2]) * t
        cx = (idxs[:, 2].float() + vecs[:, 1]) * t
        w = anchors[a, 0] * torch.exp(vecs[:, 3])
        h = anchors[a, 1] * torch.exp(vecs[:, 4])

        x1 = cx - w / 2
        y1 = cy - h / 2
        x2 = x1 + w
        y2 = y1 + h
        out = torch.stack([confidence, x1, y1, x2, y2, classify], dim=1)
        return out


if __name__ == '__main__':
    detector = Detector()
    img_path = "./data"
    img_name_list = os.listdir(img_path)
    name = {0:"",1:"",2:"",3:""}
    color = {0:"red",1:"yellow",2:"bule",3:"green"}
    font = ImageFont.truetype("simsun.ttc",18,encoding="unic")
    for image_file in img_name_list:
        im = Image.open(f"{img_path}/{image_file}")
        img = im.convert("RGB")
        img = torch.Tensor(numpy.array(img)/255)
        img = img.unsqueeze(0).permute(0,3,1,2).cuda()

        out_value = detector(img,0.3,CFG.ANCHORS_GROUP)
        boxes = []

        for j in range(4):
            classify_mask = (out_value[...,-1] == j)
            _boxes = out_value[classify_mask]
            boxes.append()

        for box in boxes:
            img_draw = ImageDraw.Draw(im)
            for i in range(len(box)):
                c,x1,y1,x2,y2,cls = box[i,:]
                img_draw.rectangle((x1,y1,x2,y2),outline=color[int(cls.item())],width=2)

                img_draw.text((max(x1,0)+3,max(y1,0)+3),fill=color[int(cls.item())],
                              text=str(int(cls.item())),font=font,width = 2)
                img_draw.text((max(x1,0)+15,max(y1,0)+3),fill=color[int(cls.item())],
                          text=name[int(cls.item())],font=font,width = 2)
                img_draw.text((max(x1,0)+3,max(y1,0)+20),fill=color[int(cls.item())],
                              text=str(round(c.item()),4),font=font,width = 2)

if __name__ == '__main__':
    de = Detector()
    y = de(torch.randn(3,3,416,416),0.3,CFG.ANCHORS_GROUP)
    print(y.shape)

