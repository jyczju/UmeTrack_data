# 参考https://blog.csdn.net/weixin_44072750/article/details/120707399


import os
import time
from datetime import datetime, timedelta
import copy

import psutil

def count_down(weeks=0, days=0, hours=0, minutes=0, seconds=0):
    remain_time = timedelta(weeks=weeks, days=days, hours=hours, minutes=minutes, seconds=seconds)
    while remain_time.total_seconds() > 0:
        time.sleep(1)
        remain_time -= timedelta(seconds=1)
        print("\r 倒计时：{}".format(remain_time), end="", flush=True)
    print("\n")

def getNet():
    recv_before = psutil.net_io_counters().bytes_recv  # 已接收的流量
    time.sleep(1)
    recv_now = psutil.net_io_counters().bytes_recv
    recv = (recv_now - recv_before)/1024
    # print("下载：{0}KB/s".format("%.2f"%recv))
    return recv

def IDMdownload(DownUrl, DownPath, FileName):
    IDMPath = r"C:\Program Files (x86)\Internet Download Manager"
    os.chdir(IDMPath)
    IDM = r"IDMan.exe"
    # command = ' '.join([IDM, '/d', DownUrl, '/p', DownPath, '/f', FileName, '/q', '/n'])
    # command = ' '.join([IDM, '/d', DownUrl, '/p', DownPath, '/f', FileName, '/n']) # 马上开始下载任务
    command = ' '.join([IDM, '/d', DownUrl, '/p', DownPath, '/f', FileName, '/a']) # 添加到下载队列，但不下载
    print(command)
    os.system(command)

def begin_download():
    IDMPath = r"C:\Program Files (x86)\Internet Download Manager"
    os.chdir(IDMPath)
    IDM = r"IDMan.exe"

    command = ' '.join([IDM, '/s']) # 开始下载
    print(command)
    os.system(command)

def download_dataset():
    # 遍历文件夹路径
    path = "./UmeTrack_data-355df534a1c761ac416427925485b311f22ce50e"
    for root,dirs,files in os.walk(path):
        # 找到所有mp4文件
        for file in files:
            if file.endswith(".mp4"):
                t_root = copy.deepcopy(root)
                t_root = t_root[1:]
                t_root = t_root.replace("\\", "/")
                t_root = t_root.replace("-", "/")

                FileName = copy.deepcopy(file)

                DownUrl = "https://media.githubusercontent.com/media/facebookresearch" + t_root + "/" + FileName + "?download=true"
                DownPath = r"E:\脚本调用IDM自动下载dataset" + root[1:]
                
                file_size = os.path.getsize(DownPath + '/' + FileName)
                print("准备下载文件：", t_root + '/' + FileName)
                print("文件大小：",file_size, "字节")


                if file_size < 400:
                    

                    IDMdownload(DownUrl, DownPath, FileName)
                    os.chdir(r"E:\脚本调用IDM自动下载dataset")
                    
                    # count_down(seconds=10)
                    
                    # # 如果当前系统网速很慢，说明下载已经完成，可以继续下一个文件的下载
                    # while True: # 这是一个等待循环
                    #     recv = getNet()
                    #     print("\r 当前下载速度：{0}KB/s     ".format("%.2f"%recv), end="", flush=True)
                    #     if recv < 1000:
                    #         print("\n 当前下载速度低于1000KB/s，可以下载下一个文件")
                    #         count_down(seconds=5)
                    #         break
                    #     else:
                    #         time.sleep(2)
                    #         continue
                
                print("\n")
    begin_download()


if __name__ == "__main__":
    download_dataset()






