This repo contains dataset used in the paper [UmeTrack: Unified multi-view end-to-end hand tracking for VR](https://research.facebook.com/publications/umetrack-unified-multi-view-end-to-end-hand-tracking-for-vr/). See [UmeTrack github](https://github.com/facebookresearch/UmeTrack) page for usage.

## 关于数据集下载
该数据集的视频全部存储在git LFS上，且相当大，约150GB，假如在国内使用git clone进行下载，成功率相当低，且不支持断点续传！！

这里提供一个python脚本downloader.py来自动对数据集中的所有mp4文件调用IDM下载器下载。

具体使用方法如下：

1.在网页端下载Umetrack_data仓库的zip压缩包

2.将downloader.py放置在同一目录下，修改代码中的路径，一个是IDM下载器的路径，一个是数据集在本地的存储路径，注意有多处需要修改

3.运行downloader.py

4.打开IDM下载器，查看是否已经创建下载任务并开始下载


## License
UmeTrack_data is licensed under the Creative Commons Attribution-NonCommerial 4.0 International License, as found in the LICENSE file.
