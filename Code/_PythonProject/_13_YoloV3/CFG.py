# 建议框和尺寸
IMG_GEIGHT = 416
IMG_WIDTH = 416
CLASS_NUM = 4

# 自定义建议框
ANCHORS_GROUP = {
    13: [[360, 360], [360, 180], [180, 360]],
    26: [[180, 180], [180, 90], [90, 180]],
    52: [[90, 90], [90, 45], [45, 90]]
}
# 计算建议框面积
ANCHORS_GROUP_AREA = {
    13: [x * y for x, y in ANCHORS_GROUP[13]],
    26: [x * y for x, y in ANCHORS_GROUP[26]],
    52: [x * y for x, y in ANCHORS_GROUP[52]]
}

if __name__ == '__main__':
    for feature_size,anchors in ANCHORS_GROUP.items():
        print(feature_size)
        print(anchors)

    for feature_size,anchors in ANCHORS_GROUP_AREA.items():
        print(feature_size)
        print(anchors)