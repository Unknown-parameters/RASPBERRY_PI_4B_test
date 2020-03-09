# RASPBERRY_PI_4B_test
由于python，opencv版本的不同，创建虚拟环境的工具不同，以及到本地路径的不同，会出现一些阻碍，下面给出自己遇到的一些差错及对应的措施；

- [首先，说明下流程的框架：](https://www.pyimagesearch.com/2017/09/04/raspbian-stretch-install-opencv-3-python-on-your-raspberry-pi/)

- 编译前的准备

1.腾出足够的内存和[缓存空间](https://shumeipai.nxez.com/2017/12/18/how-to-modify-raspberry-pi-swap-partition.html)

[2.加载必要的支持（具体清单和加速过程）](https://www.cnblogs.com/letusgo/p/11523493.html)

[3.配置好虚拟环境](https://blog.csdn.net/Skankhunt/article/details/77762810)

- [编译（可能遇到的麻烦）](http://www.cirmall.com/bbs/thread-106131-1-1.html)

  [1.缺失相关文件（库中有下载）](https://blog.csdn.net/AlexWang30/article/details/99612188)
  
  [2.路径不服（看清提醒的路径做相应的更改）](https://www.jianshu.com/p/1c9978145022)

- [安装（安装后要配置文件名和路径）](https://www.veryarm.com/95272.html)

  1.在文件查找的路径可能与上述参考文档的路径不尽相同，需耐修正

- 测试("__"是两个"_"组成的）

在之前设置好的虚拟环境下：

`python`

`import cv2`

`cv2.__version__`


- 若是顺利的话，几个小时后，你会看到亲切的

  '4.2.0'
