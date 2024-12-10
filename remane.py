import os
#
path = r"E:\BaiduNetdiskDownload\01 讲透中药\19 消食药"
# path = r"E:\BaiduNetdiskDownload\01 讲透中药\讲义"
os.chdir(path)
# print(os.getcwd())
# print(os.listdir(path))
i=1
for dirs in os.listdir(path):
    # print(dirs[2:])

    os.rename(dirs,str(i)+dirs)
    # os.rename(dirs,str(i)+dirs[2:])
    i+=1
    print(i)
    # exit()
