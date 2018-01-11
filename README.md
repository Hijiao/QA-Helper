# QA Helper
问答助手，包括 百万英雄(MillionHero) 冲顶大会(RushHour) 芝士超人(SuperZ)。(这些英文名都是我瞎起的)

使用效果 见 http://blog.csdn.net/fo11ower/article/details/79030652

项目的原理是通过adb连接安卓手机，截图后使用[tesseract](https://github.com/tesseract-ocr/tesseract)识别,然后通过[selenium](www.seleniumhq.org/)打开火狐浏览器进行百度搜索。
总耗时大概在2秒左右，其中截图0.2s 识别中文1-1.5s,百度搜索0.5-1s左右




## 前置条件
这个项目依赖的环境很多，不太熟悉的朋友可能会踩不少坑
* Android手机一台，安装以上三个app
* [uiautomator2](https://github.com/openatx/uiautomator2) 用来实现快速截图（有点杀鸡用牛刀的意思，因为我有现成的开发环境就用了。安装起来问题挺多的，要是嫌麻烦可以直接用adb命令，代码中我有写。注意，adb shell screencap 截图慢而且文件太大，会影响后面的识别速度）
* [tesseract](https://github.com/tesseract-ocr/tesseract) 中文识别，需下载中文识别库[chi_sim.traineddata](https://github.com/tesseract-ocr/tessdata)到类似`tesseract/3.05.01/share/tessdata/`目录下。注意chi_sim.traindata的不同版本。
* [selenium](www.seleniumhq.org/) 官网上安装过程很详细

## 安装
```bash
  sudo  pip install selenium pillow pytesseract
```

测试是否安装成功
 ```bash
 cd MillionHero
 python ocr.py
 ```

## 使用
  不同的app，cd到相应的目录下，python main.py就可以了。当需要识别时，直接在命令行里敲击回车。可以从项目里下载任意一张图片到手机上，全屏查看图片进行测试。

