import random
from PIL import Image,ImageDraw,ImageFont,ImageFilter

def randBgColor():
    return (random.randint(0,180),random.randint(0,180),random.randint(0,180))

def randTxColor():
    return (random.randint(125, 255), random.randint(125, 255), random.randint(125, 255))

def randChar():
    return chr(random.randint(48,57))

w = 30*4
h=60

font = ImageFont.truetype("arial.ttf",size=36)

for i in range(1000):
    image = Image.new("RGB",(w,h),(255,255,255))
    draw = ImageDraw.Draw(image)
    for x in range(w):
        for y in range(h):
            draw.point((x,y),fill = randBgColor())

    filename = []
    for t in range(4):
        ch = randChar()
        filename.append(ch)
        draw.text((30*t,10),ch,fill= randTxColor(),font=font)

    image = image.filter(ImageFilter.BLUR)
    image_path = r"data"
    image.save("{0}/{1}.jpg".format(image_path,"".join(filename)))
    print(i)