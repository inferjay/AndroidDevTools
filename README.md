AndroidDevTools
===============

[![Gitter](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/inferjay/AndroidDevTools?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

**Android Dev Tools官网地址：[www.androiddevtools.cn](http://www.androiddevtools.cn)**

收集整理Android开发所需的Android SDK、开发中用到的工具、Android开发教程、Android设计规范，免费的设计素材等。

欢迎大家推荐自己在Android开发过程中用的好用的工具、学习开发教程、用到设计素材，欢迎Star、Fork 😄。

>如果你对翻译英文的Android开发技术文章感兴趣，欢迎Start和Fork[AndroidWeekly中国文章翻译项目](https://github.com/AWCNTT/ArticleTranslateProject)


#Android Tools
---

####Android SDK在线更新镜像服务器
	
1. 大连东软信息学院镜像服务器地址: 

	`http://mirrors.neusoft.edu.cn` 端口：80

2. 北京化工大学镜像服务器地址: 
   	
   * IPv4: `http://ubuntu.buct.edu.cn/` 端口：80
   
   * IPv4: `http://ubuntu.buct.cn/`   端口：80
   
   * IPv6: `http://ubuntu.buct6.edu.cn/`  端口：80
	
3. 上海GDG镜像服务器地址:

	`http://sdk.gdgshanghai.com `  端口：8000

**使用方法**：
	
1. 启动 Android SDK Manager ，打开主界面，依次选择『**Tools**』、『**Options...**』，弹出『**Android SDK Manager - Settings**』窗口；

2. 在『**Android SDK Manager - Settings**』窗口中，在『**HTTP Proxy Server」和「HTTP Proxy Port**』输入框内填入上面镜像服务器地址和端口，并且选中『**Force https://... sources to be fetched using http://...**』复选框。设置完成后单击『**Close**』按钮关闭『**Android SDK Manager - Settings**』窗口返回到主界面；

3. 依次选择『**Packages**』、『**Reload**』。


####ADT Bundle
ADT Bundle包含了Eclipse、ADT插件和SDK Tools，是已经集成好的IDE，只需安装好Jdk即可开始开发，推荐初学者下载ADT Bundle，不用再折腾开发环境。

| 版本号  | Windows                |      Mac OSX       |          Linux         |
|:----------:|:-------------:|:------:|:----------:|
| 23.0.2 | [32位][adtb-23-0-2-win-32] [64位][adtb-23-0-2-win-64] |[64位][adtb-23-0-2-mac-64] | [32位][adtb-23-0-2-linux-32] [64位][adtb-23-0-2-linux-64] |
| 23.0.0 | [32位][adtb-23-win-32] [64位][adtb-23-win-64] |[64位][adtb-23-mac-64] | [32位][adtb-23-linux-32] [64位][adtb-23-linux-64] |

[adtb-23-0-2-win-32]:http://pan.baidu.com/s/1dDGM8oD
[adtb-23-0-2-win-64]:http://pan.baidu.com/s/1mgn2dOs

[adtb-23-0-2-mac-64]:http://pan.baidu.com/s/1o6OBIHG

[adtb-23-0-2-linux-32]:http://pan.baidu.com/s/1GmIsQ
[adtb-23-0-2-linux-64]:http://pan.baidu.com/s/1EQMT4

[adtb-23-win-32]:http://pan.baidu.com/s/1i39mvY1
[adtb-23-win-64]:http://pan.baidu.com/s/1o65ExPS

[adtb-23-mac-64]:http://pan.baidu.com/s/1hqvHkry

[adtb-23-linux-32]:http://pan.baidu.com/s/1mgoh41q
[adtb-23-linux-64]:http://pan.baidu.com/s/1qWJh4wk


####Android Studio
| 版本号  |   Windows         |       Mac OSX     |       Linux     |
|:------:|:--------------:|:-----------------:|:------------------:|
|  1.1正式版 | [下载][1.1-win] | [下载][1.1-mac] | [下载][1.1-linux] |
|  1.1 RC1 | [下载][1.1rc1-win] | [下载][1.1rc1-mac] | [下载][1.1rc1-linux] |
|  1.1 Beta 4 | [下载][1.1-b4-win] | [下载][1.1-b4-mac] | [下载][1.1-b4-linux] |
|  1.1 Beta 3 | [下载][1.1-b3-win] | [下载][1.1-b3-mac] | [下载][1.1-b3-linux] |
|  1.1 Beta 2 | [下载][1.1-b2-win] | [下载][1.1-b2-mac] | [下载][1.1-b2-linux] |
|  1.1 Beta 1 | [下载][1.1-b1-win] | [下载][1.1-b1-mac] | [下载][1.1-b1-linux] |
|  1.1 Preview 2 | [下载][1.1-p2-win] | [下载][1.1-p2-mac] | [下载][1.1-p2-linux] |
|  1.1 Preview 1 | [下载][1.1-p1-win] | [下载][1.1-p1-mac] | [下载][1.1-p1-linux] |
|  1.0.2 | [下载][1.0.2-win] | [下载][1.0.2-mac] | [下载][1.0.2-linux] |
|  1.0.1 | [下载][1.0.1-win] | [下载][1.0.1-mac] | [下载][1.0.1-linux] |
|  1.0正式版 | [下载][1.0-win] | [下载][1.0-mac] | [下载][1.0-linux] |
|  1.0 RC4 | [下载][1.0rc4-win] | [下载][1.0rc4-mac] | [下载][1.0rc4-linux] |
|  1.0 RC2 | [下载][1.0rc2-win] | [下载][1.0rc2-mac] | [下载][1.0rc2-linux] |
|  1.0 RC1 | [下载][1.0rc1-win] | [下载][1.0rc1-mac] | [下载][1.0rc1-linux] |
|  0.9.3 | [下载][0.9.3-win] | [下载][0.9.3-mac] | [下载][0.9.3-linux] |
|  0.9.2 | [下载][0.9.2-win] | [下载][0.9.2-mac] | [下载][0.9.2-linux] |
|  0.9.1 | [下载][0.9.1-win] | [下载][0.9.1-mac] | [下载][0.9.1-linux] |
|  0.9.0 | [下载][0.9.0-win] | [下载][0.9.0-mac] | [下载][0.9.0-linux] |
|  0.8.14 | [下载][0.8.14-win] | [下载][0.8.14-mac] | [下载][0.8.14-linux] |
|  0.8.13 | [下载][0.8.13-win] | [下载][0.8.13-mac] | [下载][0.8.13-linux] |
|  0.8.12 | [下载][0.8.12-win] | [下载][0.8.12-mac] | [下载][0.8.12-linux] |
|  0.8.11 | [下载][0.8.11-win] | [下载][0.8.11-mac] | [下载][0.8.11-linux] |
|  0.8.10 | [下载][0.8.10-win] | [下载][0.8.10-mac] | [下载][0.8.10-linux] |
|  0.8.9 | [下载][0.8.9-win] | [下载][0.8.9-mac] | [下载][0.8.9-linux] |
|  0.8.8 | [下载][0.8.8-win] | [下载][0.8.8-mac] | [下载][0.8.8-linux] |
|  0.8.7 | [下载][0.8.7-win] | [下载][0.8.7-mac] | [下载][0.8.7-linux] |
|  0.8.6 | [下载][0.8.6-win] | [下载][0.8.6-mac] | [下载][0.8.6-linux] |
|  0.8.5 | [下载][0.8.5-win] | [下载][0.8.5-mac] | [下载][0.8.5-linux] |
|  0.8.4 | [下载][0.8.4-win] | [下载][0.8.4-mac] | [下载][0.8.4-linux] |
|  0.8.3 | [下载][0.8.3-win] | [下载][0.8.3-mac] | [下载][0.8.3-linux] |
|  0.8.2 | [下载][0.8.2-win] | [下载][0.8.2-mac] | [下载][0.8.2-linux] |
|  0.8.1 | [下载][0.8.1-win] | [下载][0.8.1-mac] | [下载][0.8.1-linux] |
|  0.8 0 | [下载][0.8.0-win] | [下载][0.8.0-mac] | [下载][0.8.0-linux] |
|  0.6.1 | [下载][0.6.1-win] | [下载][0.6.1-mac] | [下载][0.6.1-linux] |
|  0.6.0 | [下载][0.6.0-win] | [下载][0.6.0-mac] | [下载][0.6.0-linux] |
|  0.5.9 | [下载][0.5.9-win] | [下载][0.5.9-mac] | [下载][0.5.9-linux] |
|  0.5.8 | [下载][0.5.8-win] | [下载][0.5.8-mac] | [下载][0.5.8-linux] |

[1.1-win]:http://pan.baidu.com/s/1sjr1dpj
[1.1-mac]:http://pan.baidu.com/s/1mg0yHi4
[1.1-linux]:http://pan.baidu.com/s/1jGDubg6

[1.1rc1-win]:http://pan.baidu.com/s/1jG3QuV0
[1.1rc1-mac]:http://pan.baidu.com/s/1eQhDPPw
[1.1rc1-linux]:http://pan.baidu.com/s/1o6smUng

[1.1-b4-win]:http://pan.baidu.com/s/1ntMaSA1
[1.1-b4-mac]:http://pan.baidu.com/s/1bn2IyMN
[1.1-b4-linux]:http://pan.baidu.com/s/1qWPs9dy

[1.1-b3-win]:http://pan.baidu.com/s/1pJoMNSf
[1.1-b3-mac]:http://pan.baidu.com/s/1qWyoku4
[1.1-b3-linux]:http://pan.baidu.com/s/1jG24kv0

[1.1-b2-win]:http://pan.baidu.com/s/1gdCJ4H1
[1.1-b2-mac]:http://pan.baidu.com/s/1hqpaWa4
[1.1-b2-linux]:http://pan.baidu.com/s/1i3w0vT7

[1.1-b1-win]:http://pan.baidu.com/s/1dDo1b9Z
[1.1-b1-mac]:http://pan.baidu.com/s/1kT21VQv
[1.1-b1-linux]:http://pan.baidu.com/s/1gdrKGsb

[1.1-p2-win]:http://pan.baidu.com/s/1pJMCx79
[1.1-p2-mac]:http://pan.baidu.com/s/1eQd901k
[1.1-p2-linux]:http://pan.baidu.com/s/1sjuiarb

[1.1-p1-win]:http://pan.baidu.com/s/1kTFsJ9H
[1.1-p1-mac]:http://pan.baidu.com/s/1o6p4j8I
[1.1-p1-linux]:http://pan.baidu.com/s/1pJJouDl

[1.0.2-win]:http://pan.baidu.com/s/1pJA0b0n
[1.0.2-mac]:http://pan.baidu.com/s/1jGuvmuU
[1.0.2-linux]:http://pan.baidu.com/s/1qWCzSjM

[1.0.1-win]:http://pan.baidu.com/s/1cu76m
[1.0.1-mac]:http://pan.baidu.com/s/1hqoZCDe
[1.0.1-linux]:http://pan.baidu.com/s/1c0nLN6g

[1.0-win]:http://pan.baidu.com/s/1eQzmQDO
[1.0-mac]:http://pan.baidu.com/s/1dDitUFJ
[1.0-linux]:http://pan.baidu.com/s/1kTn7wLx

[1.0rc4-win]:http://pan.baidu.com/s/1pJkbwin
[1.0rc4-mac]:http://pan.baidu.com/s/1hq1QBVQ
[1.0rc4-linux]:http://pan.baidu.com/s/1eQBygj4

[1.0rc2-win]:http://pan.baidu.com/s/1sjx4rNJ
[1.0rc2-mac]:http://pan.baidu.com/s/1eQpJmqI
[1.0rc2-linux]:http://pan.baidu.com/s/1ntuUBvN

[1.0rc1-win]:http://pan.baidu.com/s/1sjsKtIl
[1.0rc1-mac]:http://pan.baidu.com/s/1gdrcRfX
[1.0rc1-linux]:http://pan.baidu.com/s/1sjO82st

[0.9.3-win]:http://pan.baidu.com/s/1o6JoLzc
[0.9.3-mac]:http://pan.baidu.com/s/1o69LsOq
[0.9.3-linux]:http://pan.baidu.com/s/1c0B1Gju

[0.9.2-win]:http://pan.baidu.com/s/1gdzkjgn
[0.9.2-mac]:http://pan.baidu.com/s/1sj17AJN
[0.9.2-linux]:http://pan.baidu.com/s/1c0hFuDi

[0.9.1-win]:http://pan.baidu.com/s/1gdgTnqF
[0.9.1-mac]:http://pan.baidu.com/s/1qW3B0Ck
[0.9.1-linux]:http://pan.baidu.com/s/1dDitjW1

[0.9.0-win]:http://pan.baidu.com/s/1eQ3VNMi
[0.9.0-mac]:http://pan.baidu.com/s/1bnCPy5x
[0.9.0-linux]:http://pan.baidu.com/s/1tUA5o

[0.8.14-win]:http://pan.baidu.com/s/1kT1d5JL
[0.8.14-mac]:http://pan.baidu.com/s/1jGj4Eu6
[0.8.14-linux]:http://pan.baidu.com/s/1gdgmYiR

[0.8.13-win]:http://pan.baidu.com/s/1mgE85Pu
[0.8.13-mac]:http://pan.baidu.com/s/1jGBoOiq
[0.8.13-linux]:http://pan.baidu.com/s/1hqJ0xhi

[0.8.12-win]:http://pan.baidu.com/s/1eQ3ps2I
[0.8.12-mac]:http://pan.baidu.com/s/1o6uR15g
[0.8.12-linux]:http://pan.baidu.com/s/1i3uvHid

[0.8.11-win]:http://pan.baidu.com/s/1c0lbPEK
[0.8.11-mac]:http://pan.baidu.com/s/1sjpveBN
[0.8.11-linux]:http://pan.baidu.com/s/1gdCGfgn

[0.8.10-win]:http://pan.baidu.com/s/1o6NWZuq
[0.8.10-mac]:http://pan.baidu.com/s/1o6E36um
[0.8.10-linux]:http://pan.baidu.com/s/1i3iPGtn

[0.8.9-win]:http://pan.baidu.com/s/1mggH8P6
[0.8.9-mac]:http://pan.baidu.com/s/1bnrjr0F
[0.8.9-linux]:http://pan.baidu.com/s/1c0ozyz2

[0.8.8-win]:http://pan.baidu.com/s/1o6hZneE
[0.8.8-mac]:http://pan.baidu.com/s/1gdh77nt
[0.8.8-linux]:http://pan.baidu.com/s/1dDgVDxn

[0.8.7-win]:http://pan.baidu.com/s/1ntt61xn
[0.8.7-mac]:http://pan.baidu.com/s/1eQCHAV4
[0.8.7-linux]:http://pan.baidu.com/s/1eQcPIcq

[0.8.6-win]:http://pan.baidu.com/s/1mg6zsGK
[0.8.6-mac]:http://pan.baidu.com/s/1nt5b0F3
[0.8.6-linux]:http://pan.baidu.com/s/1hq674bU

[0.8.5-win]:http://pan.baidu.com/s/1dDxQfh3
[0.8.5-mac]:http://pan.baidu.com/s/1bn6HEwR
[0.8.5-linux]:http://pan.baidu.com/s/1dDkYOMH

[0.8.4-win]:http://pan.baidu.com/s/1qWqbWyo
[0.8.4-mac]:http://pan.baidu.com/s/1i3Ia7Nv
[0.8.4-linux]:http://pan.baidu.com/s/1ntwTDqx

[0.8.3-win]:http://pan.baidu.com/s/1eQioNrs
[0.8.3-mac]:http://pan.baidu.com/s/1o6v5E6Q
[0.8.3-linux]:http://pan.baidu.com/s/1bnb9uiz

[0.8.2-win]:http://pan.baidu.com/s/1eQ1ln14
[0.8.2-mac]:http://pan.baidu.com/s/1pJkDQHl
[0.8.2-linux]:http://pan.baidu.com/s/1c0ncknA

[0.8.1-win]:http://pan.baidu.com/s/1o6LTxVG
[0.8.1-mac]:http://pan.baidu.com/s/1dD5qHjF
[0.8.1-linux]:http://pan.baidu.com/s/1kTqlzxH

[0.8.0-win]:http://pan.baidu.com/s/1eQ5oGaI
[0.8.0-mac]:http://pan.baidu.com/s/1kTHpLyR
[0.8.0-linux]:http://pan.baidu.com/s/1c0qzDao

[0.6.1-win]:http://pan.baidu.com/s/1hqqX2ba
[0.6.1-mac]:http://pan.baidu.com/s/1qWjpB9y
[0.6.1-linux]:http://pan.baidu.com/s/1qWBFTiG

[0.6.0-win]:http://pan.baidu.com/s/1sjJf0Pf
[0.6.0-mac]:http://pan.baidu.com/s/1jcixK
[0.6.0-linux]:http://pan.baidu.com/s/1hqpB7As

[0.5.9-win]:http://pan.baidu.com/s/1dDw3oYl
[0.5.9-mac]:http://pan.baidu.com/s/1c08a8y0
[0.5.9-linux]:http://pan.baidu.com/s/1hqeMmVU

[0.5.8-win]:http://pan.baidu.com/s/1qWLPqd2
[0.5.8-mac]:http://pan.baidu.com/s/1i3ECc9f
[0.5.8-linux]:http://pan.baidu.com/s/1i37QxBf


####ADT Plugin
离线安装ADT插件请戳[**项目wiki**](https://github.com/inferjay/AndroidDevTools/wiki/首页)

|    版本号   |
|:----------:|
|[ADT-23.0.4](http://pan.baidu.com/s/1i39UM7j)|
|[ADT-23.0.3](http://pan.baidu.com/s/1hqJyLTi)|
|[ADT-23.0.2](http://pan.baidu.com/s/1bnGkEvX)|
|[ADT-23.0.0](http://pan.baidu.com/s/1sjArX7J)|
|[ADT-22.6.3](http://pan.baidu.com/s/1jGMb5yQ)|
|[AdT-22.6.1](http://pan.baidu.com/s/1pJ185Rl)|

####SDK Tools

| 版本号 	     | Windows             |          Mac OSX        |          Linux         |
|:----------|:-------------:|:------|:----------:|
| sdk-tools-r24.0.2 | [installer_r24.0.2-windows.exe][installer_r24.0.2-win] [android-sdk_r24.0.2-windows.zip][android-sdk_r24.0.2-win] | [android-sdk_r24.0.2-macosx.zip][android-sdk_r24.0.2-mac] | [android-sdk_r24.0.2-linux.tgz][android-sdk_r24.0.2-linux] |
| sdk-tools-r24.0.1 | [installer_r24.0.1-windows.exe][installer_r24.0.1-win] [android-sdk_r24.0.1-windows.zip][android-sdk_r24.0.1-win] | [android-sdk_r24.0.1-macosx.zip][android-sdk_r24.0.1-mac] | [android-sdk_r24.0.1-linux.tgz][android-sdk_r24.0.1-linux] |
| sdk-tools-r24 | [installer_r24-windows.exe][installer_r24-win] [android-sdk_r24-windows.zip][android-sdk_r24-win] | [android-sdk_r24-macosx.zip][android-sdk_r24-mac] | [android-sdk_r24-linux.tgz][android-sdk_r24-linux] |
| sdk-tools-r23.0.5 | [android-sdk_r23.0.5-windows(非官方版).zip][android-sdk_r23.0.5-win] | [android-sdk_r23.0.5-macosx(非官方版).zip][android-sdk_r23.0.5-mac] |  |
| sdk-tools-r23.0.2 | [installer_r23.0.2-windows.exe][installer_r23.0.2-win] [android-sdk_r23.0.2-windows.zip][android-sdk_r23.0.2-win] | [android-sdk_r23.0.2-macosx.zip][android-sdk_r23.0.2-mac] | [android-sdk_r23.0.2-linux.tgz][android-sdk_r23.0.2-linux] |
| sdk-tools-r23 | [installer_r23-windows.exe][installer_r23-win] [android-sdk_r23-windows.zip][android-sdk_r23-win] | [android-sdk_r23-macosx.zip][android-sdk_r23-mac] | [android-sdk_r23-linux.tgz][android-sdk_r23-linux] |

> **备注：** `非官方版` 是在 `23.0.2` 的基础上进行了在线更新包含了 `Android 5.0 SDK` ，`SDK Tools 23.0.5` 、`Build Tools 21.0.1` 、`Support Library 21`等。

[installer_r24.0.2-win]:http://pan.baidu.com/s/1eQH3ZOI
[android-sdk_r24.0.2-win]:http://pan.baidu.com/s/1c0vnzMC

[android-sdk_r24.0.2-mac]:http://pan.baidu.com/s/1mgDnXMw

[android-sdk_r24.0.2-linux]:http://pan.baidu.com/s/1eQEglTS


[installer_r24.0.1-win]:http://pan.baidu.com/s/1gdgojhp
[android-sdk_r24.0.1-win]:http://pan.baidu.com/s/1gdEKclP

[android-sdk_r24.0.1-mac]:http://pan.baidu.com/s/1i3467DN

[android-sdk_r24.0.1-linux]:http://pan.baidu.com/s/1gdvNj83


[installer_r24-win]:http://pan.baidu.com/s/1jG5ks7c
[android-sdk_r24-win]:http://pan.baidu.com/s/1pJ4uk4r

[android-sdk_r24-mac]:http://pan.baidu.com/s/1pJ8xUgN

[android-sdk_r24-linux]:http://pan.baidu.com/s/1pJ4uk47



[android-sdk_r23.0.5-win]:http://pan.baidu.com/s/1bntmoqV

[android-sdk_r23.0.5-mac]:http://pan.baidu.com/s/1o6LWg10



[installer_r23.0.2-win]:http://pan.baidu.com/s/1jGj2xIA
[android-sdk_r23.0.2-win]:http://pan.baidu.com/s/1CiWSu

[android-sdk_r23.0.2-mac]:http://pan.baidu.com/s/1bny9Mk3

[android-sdk_r23.0.2-linux]:http://pan.baidu.com/s/1qWAu4o8


[installer_r23-win]:http://pan.baidu.com/s/1nt5Gwhb
[android-sdk_r23-win]:http://pan.baidu.com/s/1kTC6akZ

[android-sdk_r23-mac]:http://pan.baidu.com/s/1gdj7X3l

[android-sdk_r23-linux]:http://pan.baidu.com/s/1yBnSa

####SDK Platform-Tools

这是 adb, fastboot 等工具包。把解压出来的 `platform-tools` 文件夹放在 android sdk 根目录下，并把 `adb`所在的目录添加到系统 `PATH` 路径里，即可在命令行里直接访问了 adb, fastboot 等工具。

| 版本号        | Windows             |          Mac OSX        |          Linux         |
|:----------|:-------------:|:------|:----------:|
| platform-tools-r21 | [platform-tools_r21-windows.zip][platform-tools_r21-win] | [platform-tools_r21-mac.zip][platform-tools_r21-mac] | [platform-tools_r21-linux.zip][platform-tools_r21-linux] |
| platform-tools-r20 | [platform-tools_r20-windows.zip][platform-tools_r20-win] | [platform-tools_r20-mac.zip][platform-tools_r20-mac] | [platform-tools_r20-linux.zip][platform-tools_r20-linux] |

[platform-tools_r21-win]:http://pan.baidu.com/s/1gdF1fkZ
[platform-tools_r21-mac]:http://pan.baidu.com/s/1dDu6xC9
[platform-tools_r21-linux]:http://pan.baidu.com/s/1dDAL25j
[platform-tools_r20-win]:http://pan.baidu.com/s/1ntHqLZj
[platform-tools_r20-mac]:http://pan.baidu.com/s/1gdy6fzP
[platform-tools_r20-linux]:http://pan.baidu.com/s/173KQi

### Build-Tools
这是Android开发所需的Build-Tools，下载并解压后，将解压出的整个文件夹复制或者移动到 `your sdk 路径/build-tools` 文件夹即可。

| 版本号  |   Windows         |       Mac OSX     |       Linux     |
|:------:|:--------------:|:-----------------:|:------------------:|
|  21.1.2 | [下载][21.1.2-win] | [下载][21.1.2-mac] |  |
|  21.1.1 | [下载][21.1.1-win] | [下载][21.1.1-mac] |  |
|  21.1.0 | [下载][21.1.0-win] | [下载][21.1.0-mac] |  |
|  21.0.2 | [下载][21.0.2-win] | [下载][21.0.2-mac] |  |
|  21.0.1 | [下载][21.0.1-win] | [下载][21.0.1-mac] |  |
|  21.0.0 | [下载][21.0.0-win] | [下载][21.0.0-mac] |  |
|  20.0.0 | 				   | [下载][20.0.0-mac] |  |
|  19.1.0 | [下载][19.1.0-win] | [下载][19.1.0-mac] |  |
|  19.0.3 | [下载][19.0.3-win] | [下载][19.0.3-mac] |  |
|  19.0.2 | [下载][19.0.2-win] | [下载][19.0.2-mac] |  |
|  19.0.1 | [下载][19.0.1-win] | [下载][19.0.1-mac] |  |
|  19.0.0 | [下载][19.0.0-win] | [下载][19.0.0-mac] |  |

[21.1.2-win]:http://pan.baidu.com/s/1hqH1pZY
[21.1.2-mac]:http://pan.baidu.com/s/1hq1mml2

[21.1.1-win]:http://pan.baidu.com/s/1mgzFXW0
[21.1.1-mac]:http://pan.baidu.com/s/1i367FTz


[21.1.0-win]:http://pan.baidu.com/s/1pJ3DCGN
[21.1.0-mac]:http://pan.baidu.com/s/1hqIfeCW


[21.0.2-win]:http://pan.baidu.com/s/1kTDpnt9
[21.0.2-mac]:http://pan.baidu.com/s/1dDCf9TZ


[21.0.1-win]:http://pan.baidu.com/s/1eQreI6A
[21.0.1-mac]:http://pan.baidu.com/s/1eQCd5YE


[21.0.0-win]:http://pan.baidu.com/s/1i3y0mKd
[21.0.0-mac]:http://pan.baidu.com/s/1i3oWM01




[20.0.0-mac]:http://pan.baidu.com/s/1c0AfIOK


[19.1.0-win]:http://pan.baidu.com/s/1nttAyhV
[19.1.0-mac]:http://pan.baidu.com/s/1nt2vM21

[19.0.3-win]:http://pan.baidu.com/s/1qWCzdwC
[19.0.3-mac]:http://pan.baidu.com/s/1hq7VIgG

[19.0.2-win]:http://pan.baidu.com/s/1ntl0Qnf
[19.0.2-mac]:http://pan.baidu.com/s/1xY7PO

[19.0.1-win]:http://pan.baidu.com/s/1pJ1BJrt
[19.0.1-mac]:http://pan.baidu.com/s/1o65bAwa

[19.0.0-win]:http://pan.baidu.com/s/1o6I8NBs
[19.0.0-mac]:http://pan.baidu.com/s/1c0dBDvE

####SDK
这是Android开发所需的sdk，下载并解压后，将解压出的整个文件夹复制或者移动到`your sdk 路径/platforms`文件夹，然后打开SDK Manager，打开`Tools(工具)`菜单选择`Options(选项)`菜单项打开Android SDK Manager Setting对话框，点击`Clear Cache(清除缓存)`按钮，然后重启Eclipse(或Android Studio)和SDK Manager。

| 系统版本号 	 | Windows | Mac OSX  | Linux |
|:----------|:-------------:|:------:|:----------:|
| android 5.0  | [下载][android-21-win] | [下载][android-21-mac] | [下载][android-21-mac] |
| android L Rev3 | [下载][android-L-r3-win] | [下载][android-L-r3-mac] | [下载][android-L-r3-mac] |
| android L  | [下载][android-L-win] | [下载][android-L-mac] | [下载][android-L-mac] |
| android 4.4W | [下载][android-20-win] | [下载][android-20-mac] | [下载][android-20-mac] |
| android 4.4.2 | [下载][android-19-win] | [下载][android-19-mac] | [下载][android-19-mac] |
| android 4.3 | [下载][android-18-win] | [下载][android-18-mac] | [下载][android-18-mac] |
| android 4.2.2 | [下载][android-17-win] | [下载][android-17-mac] | [下载][android-17-mac] |
| android 4.1.2 | [下载][android-16-win] | [下载][android-16-mac] | [下载][android-16-mac] |
| android 4.0.3 | [下载][android-15-win] | [下载][android-15-mac] | [下载][android-15-mac] |
| android 4.0 | [下载][android-14-win] | [下载][android-14-mac] | [下载][android-14-mac] |
| android 3.2 | [下载][android-13-win] | [下载][android-13-mac] | [下载][android-13-mac] |
| android 3.1 | [下载][android-12-win] | [下载][android-12-mac] | [下载][android-12-mac] |
| android 3.0 | [下载][android-11-win] | [下载][android-11-mac] | [下载][android-11-mac] |
| android 2.3.3 | [下载][android-10-win] | [下载][android-10-mac] | [下载][android-10-mac] |
| android 2.2	 | [下载][android-8-win] | [下载][android-8-mac] | [下载][android-8-mac] |

[android-21-win]:http://pan.baidu.com/s/1i33Puo1
[android-21-mac]:http://pan.baidu.com/s/1o6v7E2I

[android-L-r3-win]:http://pan.baidu.com/s/1u8dhc
[android-L-r3-mac]:http://pan.baidu.com/s/1jG1duN8

[android-L-win]:http://pan.baidu.com/s/1i3tDDvZ
[android-L-mac]:http://pan.baidu.com/s/1ntHmhYx

[android-20-win]:http://pan.baidu.com/s/1eYPGE
[android-20-mac]:http://pan.baidu.com/s/1nt5GKWh

[android-19-win]:http://pan.baidu.com/s/1eQf8ZgI
[android-19-mac]:http://pan.baidu.com/s/1c03XoL6

[android-18-win]:http://pan.baidu.com/s/1o65bfV8
[android-18-mac]:http://pan.baidu.com/s/1bn1tNm3

[android-17-win]:http://pan.baidu.com/s/1mgICw9E
[android-17-mac]:http://pan.baidu.com/s/1pJJSlfl

[android-16-win]:http://pan.baidu.com/s/1nt3bpI5
[android-16-mac]:http://pan.baidu.com/s/1kTA6V8z

[android-15-win]:http://pan.baidu.com/s/1pJoegpd
[android-15-mac]:http://pan.baidu.com/s/1jGzdDxc

[android-14-win]:http://pan.baidu.com/s/1c0H6Ld2
[android-14-mac]:http://pan.baidu.com/s/1hqwzPTa

[android-13-win]:http://pan.baidu.com/s/1jGLvX6A
[android-13-mac]:http://pan.baidu.com/s/1qWqH9Q8

[android-12-win]:http://pan.baidu.com/s/1pJ0naTP
[android-12-mac]:http://pan.baidu.com/s/1jG62PSy

[android-11-win]:http://pan.baidu.com/s/1pJ0naTP
[android-11-mac]:http://pan.baidu.com/s/1bn2Duub

[android-10-win]:http://pan.baidu.com/s/1ngubc
[android-10-mac]:http://pan.baidu.com/s/1jGge2bk

[android-8-win]:http://pan.baidu.com/s/1qW8YzY8
[android-8-mac]:http://pan.baidu.com/s/1ntmJVmD

####SDK System images
这是在创建模拟器时需要的system image，也就是在创建模拟器时`CPU/ABI`项需要选择的，下载并解压后，将解压出的整个文件夹复制或者移动到`your sdk 路径/system-images`文件夹下即可， 如果没有`system-images`目录就先创建此文件夹，然后打开SDK Manager，打开`Tools(工具)`菜单选择`Options(选项)`菜单项打开Android SDK Manager Setting对话框，点击`Clear Cache(清除缓存)`按钮，然后重启Eclipse(或Android Studio)和SDK Manager。


| 系统版本号 	 | Windows | Mac OSX  | Linux |
|:----------|:-------------:|:------:|:----------:|
| android 5.0  | [下载][Images-5.0-win] | [下载][Images-5.0-mac] | [下载][Images-5.0-mac] |
| android L  | [下载][Images-L-win] | [下载][Images-L-mac] | [下载][Images-L-mac] |
| android 4.4W | [下载][Images-20-win] | [下载][Images-20-mac] | [下载][Images-20-mac] |
| android 4.4.2 | [下载][Images-19-win] | [下载][Images-19-mac] | [下载][Images-19-mac] |
| android 4.3 | [下载][Images-18-win] | [下载][Images-18-mac] | [下载][Images-18-mac] |
| android 4.2.2 | [下载][Images-17-win] | [下载][Images-17-mac] | [下载][Images-17-mac] |
| android 4.1.2 | [下载][Images-16-win] | [下载][Images-16-mac] | [下载][Images-16-mac] |
| android 4.0.3 | [下载][Images-15-win] | [下载][Images-15-mac] | [下载][Images-15-mac] |
| android 4.0 | [下载][Images-14-win] | [下载][Images-14-mac] | [下载][Images-14-mac] |

[Images-5.0-win]:http://pan.baidu.com/s/1ntwpDQL
[Images-5.0-mac]:http://pan.baidu.com/s/1D7glC

[Images-L-win]:http://pan.baidu.com/s/1hqIcqhA
[Images-L-mac]:http://pan.baidu.com/s/1ntFQlRV

[Images-20-win]:http://pan.baidu.com/s/1mgJVZfE
[Images-20-mac]:http://pan.baidu.com/s/1GmAE6

[Images-19-win]:http://pan.baidu.com/s/1i3Jwhed
[Images-19-mac]:http://pan.baidu.com/s/1qW0QWdm

[Images-18-win]:http://pan.baidu.com/s/1guLaQ
[Images-18-mac]:http://pan.baidu.com/s/1pJPp6dX

[Images-17-win]:http://pan.baidu.com/s/1pJO99hD
[Images-17-mac]:http://pan.baidu.com/s/1kTyZo27

[Images-16-win]:http://pan.baidu.com/s/1nMr4E
[Images-16-mac]:http://pan.baidu.com/s/1kT2xdxd

[Images-15-win]:http://pan.baidu.com/s/1i3Fsx6H
[Images-15-mac]:http://pan.baidu.com/s/1gdnCh2b

[Images-14-win]:http://pan.baidu.com/s/1gd3lhYF
[Images-14-mac]:http://pan.baidu.com/s/1hqoWcNM

[Images-10-win]:http://pan.baidu.com/s/1gd3lhYF
[Images-10-mac]:http://pan.baidu.com/s/1qWJhTwg

####GoogleMap APIs SDK
这是GoogleMap APIs SDK，下载并解压后，将解压出的整个文件夹复制或者移动到`your sdk 路径/add-ons`文件夹下，然后打开SDK Manager，打开`Tools(工具)`菜单选择`Options(选项)`菜单项打开Android SDK Manager Setting对话框，点击`Clear Cache(清除缓存)`按钮，然后重启Eclipse(或Android Studio)和SDK Manager。


| 系统版本号 	 | Windows | Mac OSX  | Linux |
|:----------|:-------------:|:------:|:----------:|
| android 4.4.2 | [下载ARM版][googlemap-19-win-arm] [下载x86版][googlemap-19-win-x86]| [下载ARM版][googlemap-19-mac-arm] [下载x86版][googlemap-19-mac-x86]| [下载ARM版][googlemap-19-mac-arm] [下载x86版][googlemap-19-mac-x86]|
| android 4.3 | [下载][googlemap-18-win] | [下载][googlemap-18-mac] | [下载][googlemap-18-mac] |
| android 4.2.2 |[下载][googlemap-17-win] |[下载][googlemap-17-mac] | [下载][googlemap-17-mac] |
| android 4.1.2 |[下载][googlemap-16-win] |[下载][googlemap-16-mac] | [下载][googlemap-16-mac] |
| android 4.0.3 | [下载][googlemap-15-win]| [下载][googlemap-15-mac]|[下载][googlemap-15-mac] |
| android 4.0 | [下载][googlemap-14-win] | [下载][googlemap-14-mac] | [下载][googlemap-14-mac] |
| android 3.2 | [下载][googlemap-13-win] | [下载][googlemap-13-mac] | [下载][googlemap-13-mac] |
| android 3.1 | [下载][googlemap-12-win] | [下载][googlemap-12-mac] | [下载][googlemap-12-mac] |
| android 3.0 | [下载][googlemap-11-win] | [下载][googlemap-11-mac] | [下载][googlemap-11-mac] |
| android 2.3.3 |[下载][googlemap-10-win] |[下载][googlemap-10-mac] | [下载][googlemap-10-mac] |
| android 2.2	| [下载][googlemap-8-win] | [下载][googlemap-8-mac] | [下载][googlemap-8-mac] |

[googlemap-19-win-arm]:http://pan.baidu.com/s/1bno0mFt
[googlemap-19-win-x86]:http://pan.baidu.com/s/1jGgKyZc

[googlemap-19-mac-arm]:http://pan.baidu.com/s/1bngsIkB
[googlemap-19-mac-x86]:http://pan.baidu.com/s/1eQDwCpG

[googlemap-18-win]:http://pan.baidu.com/s/1bnb9at5
[googlemap-18-mac]:http://pan.baidu.com/s/1gdJ0mqR

[googlemap-17-win]:http://pan.baidu.com/s/1jGl4hZw
[googlemap-17-mac]:http://pan.baidu.com/s/1dDmurr7

[googlemap-16-win]:http://pan.baidu.com/s/1ntK9Urf
[googlemap-16-mac]:http://pan.baidu.com/s/1mgIAcpa

[googlemap-15-win]:http://pan.baidu.com/s/1bnEiHiB
[googlemap-15-mac]:http://pan.baidu.com/s/1hqBWAIo

[googlemap-14-win]:http://pan.baidu.com/s/1gd68WtP
[googlemap-14-mac]:http://pan.baidu.com/s/1hqBWAIo

[googlemap-13-win]:http://pan.baidu.com/s/1o6Dgtse
[googlemap-13-mac]:http://pan.baidu.com/s/1gdf49Jt

[googlemap-12-win]:http://pan.baidu.com/s/1o6Dgtse
[googlemap-12-mac]:http://pan.baidu.com/s/1jGBS4rO

[googlemap-11-win]:http://pan.baidu.com/s/1c0CKIFA
[googlemap-11-mac]:http://pan.baidu.com/s/1c0iY68w

[googlemap-10-win]:http://pan.baidu.com/s/1hqHwsHA
[googlemap-10-mac]:http://pan.baidu.com/s/1dDvhHOt

[googlemap-8-win]:http://pan.baidu.com/s/1qWJNPyk
[googlemap-8-mac]:http://pan.baidu.com/s/1eQEc8SU

####Google Glass SDK
这是GDK，下载并解压后，将解压出的整个文件夹复制或者移动到`your sdk 路径/add-ons`文件夹下，然后打开SDK Manager，打开`Tools(工具)`菜单选择`Options(选项)`菜单项打开Android SDK Manager Setting对话框，点击`Clear Cache(清除缓存)`按钮，然后重启Eclipse(或Android Studio)和SDK Manager。

| 系统版本 | Windows | Mac OSX  | Linux |
|:----------|:-------------:|:------:|:----------:|
| android 4.4.2 | [下载][glass-win-19] | [下载][glass-mac-19] | [下载][glass-mac-19] |
| android 4.0.3 |  | [下载][glass-mac-15] |

[glass-win-19]:http://pan.baidu.com/s/1fENeu
[glass-mac-19]:http://pan.baidu.com/s/1eQpGaA2

[glass-mac-15]:http://pan.baidu.com/s/1hqikzUs


####Google TV Addon
这是Google TV Addon，下载并解压后，将解压出的整个文件夹复制或者移动到`your sdk 路径/add-ons`文件夹，然后打开SDK Manager，打开`Tools(工具)`菜单选择`Options(选项)`菜单项打开Android SDK Manager Setting对话框，点击`Clear Cache(清除缓存)`按钮，然后重启Eclipse(或Android Studio)和SDK Manager。


| 系统版本 | Windows | Mac OSX  | Linux |
|:----------|:-------------:|:------:|:----------:|
| android 3.2 | [下载][tv-win-13] | [下载][tv-mac-13] | [下载][tv-mac-13] |

[tv-win-13]:http://pan.baidu.com/s/1qWLPFfm
[tv-mac-13]:http://pan.baidu.com/s/1eQFy1KA

####Android Framework Source Code
这是Android Framework Source Code，下载并解压后，将解压出的整个文件夹复制或者移动到`your sdk 路径/sources`文件夹下，然后重启Eclipse(或Android Studio)，这样当你在Eclipse里面按住`Ctrl`键点击某个系统类时就可以打开该类的源码文件查看源码了。

| 系统版本 |
|:----------|
|[android 5.0][sources-21]|
|[android 4.4W][sources-20]|
|[android 4.4.2][sources-19]|
|[android 4.3][sources-18]|
|[android 4.2.2][sources-17]|
|[android 4.1.2][sources-16]|
|[android 4.0.3][sources-15]|
|[android 4.0][sources-14]|
|[android 3.0][sources-11]|
|[android 2.3.3][sources-10]|
|[android 2.2][sources-8]|

[sources-21]:http://pan.baidu.com/s/1dD5Z1Hf
[sources-20]:http://pan.baidu.com/s/1eQf6F0Q
[sources-19]:http://pan.baidu.com/s/1hqGGrVA
[sources-18]:http://pan.baidu.com/s/1pJI3YrD
[sources-17]:http://pan.baidu.com/s/1qWlXS9u
[sources-16]:http://pan.baidu.com/s/1qWv1spm
[sources-15]:http://pan.baidu.com/s/1jGGCpuu
[sources-14]:http://pan.baidu.com/s/1o61AZwQ
[sources-11]:http://pan.baidu.com/s/1pJt14En
[sources-10]:http://pan.baidu.com/s/1eQekIPW
[sources-8]:http://pan.baidu.com/s/1bny9E2b

#### Android SDK Extras
包含 `Android Support Library` 、 `Google Cloud Messaging for Android Library` 、`Google Play services` 、 `Google Play services for fit preview` 、`Google Play services for Froyo` 、`Google Play APK Expansion Library `、`Google Play Billing Library` 、`Google Play Licensing Library` 等，下载解压后将解压出的整个文件夹复制或者移动到`your sdk`根目录下下，如果已经存在`extras`文件夹就替换掉。

|    版本号  |
|:---------:|
| [21.0.3](http://pan.baidu.com/s/1kTmlB9d)   |
| [21.0.2](http://pan.baidu.com/s/1mgso8Y0)   |
| [21](http://pan.baidu.com/s/1o6v78Lk)   |
| [20](http://pan.baidu.com/s/1eQIMXMy)   |

####Support Library
包含support `v4`、`v7`、`v13`、`v17`、`multidex`和`m2repository`，下载解压后将解压出的整个文件夹复制或者移动到`your sdk 路径/extras`下，然后打开SDK Manager，打开`Tools(工具)`菜单选择`Options(选项)`菜单项打开Android SDK Manager Setting对话框，点击`Clear Cache(清除缓存)`按钮，然后重启Eclipse(或Android Studio)和SDK Manager。

|    版本号  |
|:---------:|
| [21.0.3](http://pan.baidu.com/s/1ntsoeE1)   |
| [21.0.2](http://pan.baidu.com/s/1kTzIkYV)   |
| [21](http://pan.baidu.com/s/1o6MBWIu)   |
| [20](http://pan.baidu.com/s/1o6OBlR8)   |

####SDK Samples
这是Android SDK自带的示例代码，下载并解压后，将解压出的整个文件夹复制或者移动到`your sdk 路径/samples`文件夹下，然后重启Eclipse(或Android Studio)。
。

| 系统版本 |
|:----------|
|[android 21][samples-21]|
|[android L][samples-L]|
|[android 4.4W][samples-20]|
|[android 4.4.2][samples-19]|
|[android 4.3][samples-18]|
|[android 4.2.2][samples-17]|
|[android 4.1.2][samples-16]|
|[android 4.0.3][samples-15]|
|[android 4.0][samples-14]|
|[android 3.2][samples-13]|
|[android 3.1][samples-12]|
|[android 3.0][samples-11]|
|[android 2.3.3][samples-10]|
|[android 2.2][samples-8]|

[samples-21]:http://pan.baidu.com/s/1dDD19XB
[samples-L]:http://pan.baidu.com/s/1gdpEan5
[samples-20]:http://pan.baidu.com/s/1ntLVN9B
[samples-19]:http://pan.baidu.com/s/1dDeSKt7
[samples-18]:http://pan.baidu.com/s/1pJHicjx
[samples-17]:http://pan.baidu.com/s/1hqGavMc
[samples-16]:http://pan.baidu.com/s/1eYPL8
[samples-15]:http://pan.baidu.com/s/1i3mScXv
[samples-14]:http://pan.baidu.com/s/1kTiKqZP
[samples-13]:http://pan.baidu.com/s/1eQpafgI
[samples-12]:http://pan.baidu.com/s/1haIPw
[samples-11]:http://pan.baidu.com/s/1ntx9qFR
[samples-10]:http://pan.baidu.com/s/1hqiQw1Q
[samples-8]:http://pan.baidu.com/s/1ntv7wut

####NDK
C/C++开发Android应用工具包,`Linux/Mac OS X 下NDK r10c`的安装方法请戳[这里](https://github.com/inferjay/AndroidDevTools/wiki/Installing-the-NDK-On-Linux-and-Mac-OS-X-(Darwin)

| 版本号 	  | Windows              |          Mac OSX        |          Linux         |
|:----------|:-------------:|:------:|:----------:|
| ndk-r10c | [32位][r10c-win-32] [64位][r10c-win-64] | [32位][r10c-mac-32] [64位][r10c-mac-64] | [32位][r10c-linux-32] [64位][r10c-linux-64]  |
| ndk64-r10 | [32位][ndk64-r10-win-32] [64位][ndk64-r10-win-64] | [32位][ndk64-r10-mac-32] [64位][ndk64-r10-mac-64] | [32位][ndk64-r10-linux-32] [64位][ndk64-r10-linux-64]  |
| ndk32-r10 | [32位][ndk32-r10-win-32] [64位][ndk32-r10-win-64] | [32位][ndk32-r10-mac-32] [64位][ndk32-r10-mac-64] | [32位][ndk32-r10-linux-32] [64位][ndk32-r10-linux-64]  |
| ndk-r9d | [32位][r9d-win-32] [64位][r9d-win-64] | [32位][r9d-mac-32] [64位][r9d-mac-64] | [32位][r9d-linux-32] [64位][r9d-linux-64]  |


| Additional Download (32-, 64-bit) |  Package |
|:----------|:-------------|
| r10 STL debug info | [android-ndk-r10-cxx-stl-libs-with-debug-info.zip](http://pan.baidu.com/s/1xWgUE) | 
| r9 STL debug info | [android-ndk-r9-cxx-stl-libs-with-debug-info.zip](http://pan.baidu.com/s/1c0EMn8O) |

[r10c-win-32]:http://pan.baidu.com/s/1bnGnKkB
[r10c-win-64]:http://pan.baidu.com/s/1ntmhjUL

[r10c-mac-32]:http://pan.baidu.com/s/1i37Ud8L
[r10c-mac-64]:http://pan.baidu.com/s/1eQ08GOa

[r10c-linux-32]:http://pan.baidu.com/s/1c0o11wk
[r10c-linux-64]:http://pan.baidu.com/s/1c0tljk0

[ndk64-r10-win-32]:http://pan.baidu.com/s/1qW0RtzI
[ndk64-r10-win-64]:http://pan.baidu.com/s/1ntypDpf

[ndk64-r10-mac-32]:http://pan.baidu.com/s/1o6G44Eu
[ndk64-r10-mac-64]:http://pan.baidu.com/s/1gd7pvJ9

[ndk64-r10-linux-32]:http://pan.baidu.com/s/1hql8AIo
[ndk64-r10-linux-64]:http://pan.baidu.com/s/1dDreuPz

[ndk32-r10-win-32]:http://pan.baidu.com/s/1bnB1o1T
[ndk32-r10-win-64]:http://pan.baidu.com/s/1gdmW6cj

[ndk32-r10-mac-32]:http://pan.baidu.com/s/1jGtBYyq
[ndk32-r10-mac-64]:http://pan.baidu.com/s/1gdADfaF

[ndk32-r10-linux-32]:http://pan.baidu.com/s/1V2Tg
[ndk32-r10-linux-64]:http://pan.baidu.com/s/1pJJQokV

[r9d-win-32]:http://pan.baidu.com/s/1dDxjl8t
[r9d-win-64]:http://pan.baidu.com/s/1jGgecXw

[r9d-mac-32]:http://pan.baidu.com/s/1eQnDNEE
[r9d-mac-64]:http://pan.baidu.com/s/1i3l5L8T

[r9d-linux-32]:http://pan.baidu.com/s/1jGr9w4A
[r9d-linux-64]:http://pan.baidu.com/s/1sjAXS41

####Android L Preview System Image
这个是Android L Preview系统的刷机镜像。

| 设备 | 下载 |
|:----------:|:-------------:|
|  Nexus 5 (GSM/LTE) "hammerhead" | [hammerhead-lpv79-preview-ac1d8a8e.tgz] [Nexus 5] |
|  Nexus 7 (Wifi) "razor"  | [razor-lpv79-preview-d0ddf8ce.tgz][Nexus 7] |

[Nexus 5]:http://pan.baidu.com/s/1kTsnxsF
[Nexus 7]:http://pan.baidu.com/s/1mgn1CyG

####JDK

| 版本号| Windows | Mac OSX  | Linux |
|:----------:|:-------------:|:------:|:----------:|
|  1.8 u5  | [32位][1.8u5-win-32] [64位][1.8u5-win-64] | [64位][1.8u5-mac-64] | [32位][1.8u5-linux-32] [64位][1.8u5-linux-64] |
|  1.7 u60 | [32位][1.7-win-32] [64位][1.7-win-64] | [64位][1.7-mac-64] | [32位][1.7-linux-32] [64位][1.7-linux-64] |
|  1.6 u45 | [32位][1.6-win-32] [64位][1.6-win-64] | [64位][1.6-mac-64] | [32位][1.6-linux-32] [64位][1.6-linux-64] |

[1.8u5-win-32]:http://pan.baidu.com/s/1bn2CVIB
[1.8u5-win-64]:http://pan.baidu.com/s/1eQtJyGq
[1.8u5-mac-64]:http://pan.baidu.com/s/1pJkD78R
[1.8u5-linux-32]:http://pan.baidu.com/s/1o64s0pc
[1.8u5-linux-64]:http://pan.baidu.com/s/1jG3KBjg

[1.7-win-32]:http://pan.baidu.com/s/1nt5a3jj
[1.7-win-64]:http://pan.baidu.com/s/1o61AAHc
[1.7-mac-64]:http://pan.baidu.com/s/1nt0qGfn
[1.7-linux-32]:http://pan.baidu.com/s/1eQd4wVK
[1.7-linux-64]:http://pan.baidu.com/s/1jGzGQLw

[1.6-win-32]:http://pan.baidu.com/s/1o67aooM
[1.6-win-64]:http://pan.baidu.com/s/1dDmtSZJ
[1.6-mac-64]:http://pan.baidu.com/s/1hqpB7Nm
[1.6-linux-32]:http://pan.baidu.com/s/1pJJj5Ib
[1.6-linux-64]:http://pan.baidu.com/s/1dDck3O9

####Gradle

|    版本号   |
|:----------|
| [gradle-2.2.1-all.zip](http://pan.baidu.com/s/1eQH39AE) |
| [gradle-2.2-all.zip](http://pan.baidu.com/s/1i3BXKYp) |
| [gradle-2.1-all.zip](http://pan.baidu.com/s/1bnF6jV5) |
| [gradle-2.0-all.zip](http://pan.baidu.com/s/1mgFTN7a) |
| [gradle-1.12-all.zip](http://pan.baidu.com/s/1Gmlx8)   |
| [gradle-1.11-all.zip](http://pan.baidu.com/s/1c0hCmdE) |
| [gradle-1.10-all.zip](http://pan.baidu.com/s/1qWtzaGW) |
| [gradle-1.9-all.zip](http://pan.baidu.com/s/1dDeSuXV)  |
| [gradle-1.8-all.zip](http://pan.baidu.com/s/1o6Npqqe)  |
| [gradle-1.7-all.zip](http://pan.baidu.com/s/1pJnvyWz)  |

#### Gradle Dependencies Configuration Generator

[Gradle, please](http://gradleplease.appspot.com)

#### 版本控制工具

##### Git

| 版本号       |         Windows         |       Mac OSX           |    Linux                |
|:------------|:-----------------------:|:-----------------------:|:-----------------------:|
|  Git-2.0.1  |                         | [下载][Git-2.0.1-mac]    | [下载][Git-for-Linux]|
|  Git-1.9.4  | [下载][Git-1.9.4-win]    |                         | [下载][Git-for-Linux]|
|  Git-1.8.5.2| [下载][Git-1.8.5.2-win] | [下载][Git-1.8.5.2-mac]  | [下载][Git-for-Linux] |

[Git-2.0.1-mac]:http://pan.baidu.com/s/1mgkM9BE

[Git-1.9.4-win]:http://pan.baidu.com/s/1ntjy9N7

[Git-1.8.5.2-win]:http://pan.baidu.com/s/1ntJWxeD
[Git-1.8.5.2-mac]:http://pan.baidu.com/s/1bncr1pX

[Git-for-Linux]:https://github.com/inferjay/AndroidDevTools/wiki/Download-for-Linux-and-Unix

##### SVN Plugin For Eclipse

|    版本号   |
|:-----------|
| [1.10.5](http://pan.baidu.com/s/1mg2x4Xq) |
| [1.8.22](http://pan.baidu.com/s/1hqswoGs) |
| [1.6.18](http://pan.baidu.com/s/1o60r6UA) |

#### 反编译工具

| 名称                           |         下载地址                  |    使用教程      |
|:------------------------------|:--------------------------------:|:---------------:|
| JEB Android Decompiler        | [下载][JEB]                       |                |
| Virtuous Ten Studio           | [下载][Virtuous Ten Studio]       |                |
| Apk文件修改工具Root Tools       | [下载][apk文件修改工具Root Tools]   |                |
| Dex文件反编译工具Dedexer        |  [下载][dex文件反编译工具Dedexer]    |                |
| APK+Dex文件反编译及回编译工具     | [下载][APK+Dex文件反编译及回编译工具] |                |
| android-apktool               | [下载][android-apktool]           |                |
| Onekey Decompile Apk]         | [下载][onekey-decompile-apk]      |                |
| Baksmali                      | [下载][baksmali]                  |                |
| Smali                         | [下载][smali]                     |                |
| AXMLPrinter2                  | [下载][AXMLPrinter2]              |                |
| JAD Java Decompiler           | [下载][JAD Java Decompiler]       |                |
| JD-GUI Decompiler             | [下载][JD-GUI Decompiler]         |                |
| XJad V2.2                     | [下载][XJad V2.2]                 |                |

[JEB]:http://www.android-decompiler.com/index.php
[Virtuous Ten Studio]:http://virtuous-ten-studio.com
[apk文件修改工具Root Tools]:https://github.com/Stericson/RootTools
[dex文件反编译工具Dedexer]:http://dedexer.sourceforge.net
[APK+Dex文件反编译及回编译工具]:http://idoog.me
[onekey-decompile-apk]:https://code.google.com/p/onekey-decompile-apk/
[android-apktool]:https://code.google.com/p/android-apktool/
[baksmali]:https://code.google.com/p/smali/downloads/detail?name=baksmali
[smali]:https://code.google.com/p/smali/
[AXMLPrinter2]:https://android4me.googlecode.com/files/AXMLPrinter2.jar
[JAD Java Decompiler]:http://varaneckas.com/jad/
[JD-GUI Decompiler]:http://
[XJad V2.2]:http://files.cnblogs.com/arix04/XJad_V2.2.rar

#### 安全工具

| 名称                           |         下载地址                  |    使用教程      |
|:------------------------------|:--------------------------------:|:---------------:|
| APKfuscator                   | [下载][APKfuscator]              |                 |
| ApkAnalyser                   | [下载][ApkAnalyser]              |                 |
| AppXplore                     | [下载][AppXplore]                |                 |
| Android analysis framework    | [下载][Android-analysis-framework]|                |
| Androguard                    | [下载][androguard]               |                 |
| Droidbox                      | [下载][droidbox]                 |                 |
| dsploit                       | [下载][dsploit]                  |                 |
| Androwarn                     | [下载][Androwarn]                |                 |
| Anubis                        | [下载][Anubis]                   |                 |
| Drozer                        | [下载][Drozer]                   |                 |
| VirusTotal                    | [下载][VirusTotal]               |                 |
| GDB for Android               | [下载][GDB-for-Android]          |                 |
| VisualGDB                     | [下载][VisualGDB]                |                 |

[APKfuscator]:https://github.com/strazzere/APKfuscator
[ApkAnalyser]:https://github.com/sonyxperiadev/ApkAnalyser/downloads
[AppXplore]:https://play.google.com/store/apps/details?id=com.sonyericsson.androidapp.AppExplore&feature=search_result#?t=W251bGwsMSwxLDEsImNvbS5zb255ZXJpY3Nzb24uYW5kcm9pZGFwcC5BcHBFeHBsb3JlIl0.
[Android-analysis-framework]:http://www.dexlabs.org
[androguard]:https://code.google.com/p/androguard/
[droidbox]:https://code.google.com/p/droidbox/
[dsploit]:https://github.com/evilsocket/dsploit
[Androwarn]:https://github.com/maaaaz/androwarn
[Anubis]:http://anubis.iseclab.org
[Drozer]:https://www.mwrinfosecurity.com/products/drozer/community-edition/
[VirusTotal]:https://www.virustotal.com
[GDB-for-Android]:http://gnutoolchains.com/android/
[VisualGDB]:http://visualgdb.com/?features=android

#### Eclipse/Android Studio/IDEA插件
##### Eclipse
| 名称                           |         下载地址                  |    使用教程      |
|:------------------------------|:--------------------------------:|:---------------:|
| SVN                           | [下载][SVN]                       |                 |
| Genymobile模拟器               | [下载][Genymobile]                |                 |
| Memory-Analyzer-Tools         | [下载][Memory-Analyzer-Tools]     |                 |
| Droidinspector                | [下载][Droidinspector]            |                 |
| SQLiteManager                 | [下载][SQLiteManager]             |                 |
| Color Theme                   | [下载][Color Theme Plugin]        |                 |
| RoboVM                   		 | [下载][RoboVM]                    |                 |
| Newrelic                      | [下载][newrelic]                  |                 |

[SVN]:http://pan.baidu.com/s/1sjqamOP
[Genymobile]:http://genymotion.com/
[Memory-Analyzer-Tools]:http://download.eclipse.org/mat/1.4/update-site/
[Droidinspector]:http://www.sriramramani.com/droidinspector/
[SQLiteManager]:https://dl.dropboxusercontent.com/u/91846918/sqlite%20manager/com.questoid.sqlitemanager_1.0.0.jar
[Color Theme Plugin]:http://eclipsecolorthemes.org/?view=plugin
[RoboVM]:http://download.robovm.org/eclipse/
[newrelic]:https://download.newrelic.com/android_agent/eclipse

##### Android Studio/IDEA
| 名称                                         |         下载地址                                  |    使用教程      |
|:--------------------------------------------|:------------------------------------------------:|:---------------:|
| Android Resource Resizer Plugin             | [下载][Android Resource Resizer]                  |                 |
| Gradle Dependencies Helper Plugin           | [下载][GradleDependenciesHelper]                  |                 |
| Android Parcelable code generation Plugin   | [下载][Parcelableboilerplatecodegen]              |                 |
| Android Holo Colors IDEA Plugin             | [下载][Droidinspector]                            |                 |
| Android Toolbox Plugin                      | [下载][Android Toolbox Plugin]                    |                 |
| Android Gradle Sign Plugin                  | [下载][AndroidGradleSignPlugin]                   |                 |
| Android Permissions Usage Plugin            | [下载][AndroidPermissionsUsage]                   |                 |
| Android Helper Plugin                       | [下载][AndroidHelper]                             |                 |
| Android Studio Prettify Plugin              | [下载][Android Studio Prettify]                   |                 |
| IDEA ADB Plugin                             | [下载][ADB-idea]                                  |                 |
| Otto Intellij Plugin                        | [下载][Otto-intellij-plugin]                      |                 |
| Dagger intellij Plugin                      | [下载][Dagger-intellij-plugin]                    |                 |
| Gradle Gui Plugin                           | [下载][gradle-intellij-gui]                       |                 |
| Android Studio Unit Test Plugin             | [下载][android-studio-unit-test-plugin]           |                 |
| Android Layout ID Converter Plugin          | [下载][Android Layout ID Converter]               |                 |
| IDEA protobuf Plugin                        | [下载][idea-plugin-protobuf]                      |                 |
| Simple Team Code Reviewer Plugin            | [下载][Simple Team Code Reviewer plugin]          |                 |
| Android XML Plugin                          | [下载][AndroidXML]                                |                 |
| ADF Plugin                                  | [下载][adf-intellijPlugin]                        |                 |
| Java2smali Plugin                           | [下载][intellij-java2smali]                       |                 |
| IDEA gitignore Plugin                       | [下载][idea-gitignore]                            |                 |
| IDEA Background Image Plugin                | [下载][Intellij-IDEA-Plugin-Background-Image]     |                 |
| IDEA Maven Plugin                           | [下载][idea-plugin-maven-plugin]                  |                 |
| Gradle GooglePlay Publisher Plugin          | [下载][gradle-play-publisher]                     |                 |
| Drawable Selectors Generates Plugin         | [下载][android-selector-chapek]                   |                 |
| Android Drawable Importer					  | [下载][android-drawable-importer-intellij-plugin] |                 |

[Android Resource Resizer]:https://github.com/walmyrcarvalho/android-resource-resizer
[GradleDependenciesHelper]:https://github.com/ligi/GradleDependenciesHelperPlugin
[Parcelableboilerplatecodegen]:https://github.com/mcharmas/android-parcelable-intellij-plugin
[Android Holo Colors IDEA Plugin]:https://github.com/jeromevdl/android-holo-colors-idea-plugin
[Android Toolbox Plugin]:https://github.com/idamobile/android-toolbox-plugin
[AndroidGradleSignPlugin]:https://github.com/alexvasilkov/AndroidGradleSignPlugin
[AndroidPermissionsUsage]:https://github.com/RomainPiel/AndroidPermissionsUsage
[AndroidHelper]:https://github.com/eunjae-lee/AndroidHelper
[Android Studio Prettify]:https://github.com/Haehnchen/idea-android-studio-plugin
[ADB-idea]:https://github.com/pbreault/adb-idea
[Otto-intellij-plugin]:https://github.com/square/otto-intellij-plugin
[Dagger-intellij-plugin]:https://github.com/square/dagger-intellij-plugin
[gradle-intellij-gui]:https://github.com/gradle-archive/gradle-intellij-gui
[android-studio-unit-test-plugin]:https://github.com/evant/android-studio-unit-test-plugin
[Android Layout ID Converter]:https://github.com/funnything/OffingHarbor
[idea-plugin-protobuf]:https://github.com/nnmatveev/idea-plugin-protobuf
[Simple Team Code Reviewer plugin]:https://github.com/syllant/idea-plugin-revu
[AndroidXML]:https://github.com/mironov-nsk/AndroidXML
[adf-intellijPlugin]:https://github.com/tizionario/adf-intellijPlugin
[intellij-java2smali]:https://github.com/ollide/intellij-java2smali
[idea-gitignore]:https://github.com/hsz/idea-gitignore
[Intellij-IDEA-Plugin-Background-Image]:https://github.com/kimptoc/Intellij-IDEA-Plugin-Background-Image
[CodeGlance]:https://github.com/Vektah/CodeGlance
[idea-plugin-maven-plugin]:https://github.com/born2snipe/idea-plugin-maven-plugin
[gradle-play-publisher]:https://github.com/Triple-T/gradle-play-publisher
[android-selector-chapek]:https://github.com/inmite/android-selector-chapek
[android-drawable-importer-intellij-plugin]:https://github.com/winterDroid/android-drawable-importer-intellij-plugin

#### Android资源/Themes/Style生成工具
| 名称                      |      简介        |         下载地址            |    使用教程      |
|:-------------------------|:-----------------|:--------------------------:|:---------------:|
| Android Asset Studio     |                  | [下载][AndroidAssetStudio]  |                 |
| Android Drawable Factory |                  | [下载][AndroidDrawableFactory]  |                 |
| Android Action Bar Style Generator  |       | [下载][ActionBarStyleGenerator]  |                 |
| Android Holo Colors Generator       |       | [下载][HoloColorsGenerator]  |                 |
| Android Simple Nine-patch Generator |       | [下载][Simple Nine-patch Generator]  |                 |
| Android Device Frame Generator |            | [下载][Device Frame Generator]  |                 |
| Android 9-patch shadow generator |            | [下载][Android shadow generator]  |                 |

[AndroidAssetStudio]:http://romannurik.github.io/AndroidAssetStudio/
[AndroidDrawableFactory]:https://github.com/tizionario/AndroidDrawableFactory
[ActionBarStyleGenerator]:http://jgilfelt.github.io/android-actionbarstylegenerator
[HoloColorsGenerator]:http://android-holo-colors.com
[Simple Nine-patch Generator]:http://romannurik.github.io/AndroidAssetStudio/nine-patches.html
[Device Frame Generator]:http://f2prateek.com/android-device-frame-generator/
[Android shadow generator]:http://inloop.github.io/shadow4android/

#### Android资源分析工具
| 名称                   |      简介        |         下载地址            |    使用教程      |
|:----------------------|:-----------------|:--------------------------:|:---------------:|
| Android Assets Viewer |                 | [下载][AndroidAssetsViewer]  |                 |

[AndroidAssetsViewer]:http://www.cellebellum.net/AndroidAssetsViewer/

#### Android Layout Parser工具
| 名称                   |      简介        |         下载地址               |    使用教程      |
|:----------------------|:-----------------|:----------------------------:|:---------------:|
| Android Layout Binder |                  | [下载][Android Layout Binder] |                 |

[Android Layout Binder]:http://android.lineten.net/layout.php

#### Android Content Provider代码生成工具
| 名称                            |      简介       |         下载地址                     |    使用教程      |
|:-------------------------------|:----------------|:----------------------------------:|:---------------:|
| Content Provider Code Generator|                 | [下载][ContentProviderCodeGenerator] |                 |

[ContentProviderCodeGenerator]:https://github.com/BoD/android-contentprovider-generator

#### Android Fragment Code Generator代码生成工具
| 名称                            |      简介       |         下载地址                     |    使用教程      |
|:-------------------------------|:----------------|:----------------------------------:|:---------------:|
| Android Fragment Code Generator |                 | [下载][FregmentCodeGenerator] |                 |

[FregmentCodeGenerator]:http://techisfun.github.io/pages/android-fragment-generator/

#### 代码生成工具
| 名称              |      简介        |         下载地址            |    使用教程      |
|:-----------------|:-----------------|:--------------------------:|:---------------:|
| Android KickstartR| AndroidKickstartR帮助您快速创建<br/>Android应用程序并使用最流行的库进行配置。<br/>它创建和配置你的项目给你。只专注于代码!                                 | [下载][AndroidKickstartR]   |                 |
| Android Button Maker| Android Button Maker是一个在线生成Android应用按钮代码的工具。<br/>Android的API提供可绘制资源，其中的XML文件定义的几何形状，包括颜色，边框和梯度。<br/>这些按钮是在shape drawable XML代码基础上产生的相比通常的PNG按钮加载速度更快。<br/>您可以在设置面板中自定义按钮的属性和获得源代码。                | [下载][Android Button Maker] |                 |
| DroidDraw         |                 | [下载][DroidDraw]           |                 |

[AndroidKickstartR]:http://androidkickstartr.com
[Android Button Maker]:http://angrytools.com/android/button/
[DroidDraw]:https://code.google.com/p/droiddraw/

#### Android Native开发工具
| 名称              |      简介         |         下载地址            |    使用教程      |
|:-----------------|------------------|:--------------------------:|:---------------:|
| Android++        |                  | [下载][Android++]           |                 |

[Android++]:http://android-plus-plus.com

#### Android测试工具
| 名称              |      简介         |         下载地址            |    使用教程      |
|:-----------------|------------------|:--------------------------:|:---------------:|
| Appurify         |                  | [下载][Appurify]            |                 |
| Monkey           |                  | [下载][Monkey]              |                 |
| Testin           |                  | [下载][Testin]              |                 |
| Spoon            |                  | [下载][Spoon]               |                 |
| Little Eye       |                  | [下载][Little Eye]          |                 |
| 易测云            |                  | [下载][易测云]               |                 |
| Emmagee          |                  | [下载][Emmagee]             |                 |
| Apk View Tracer  |                  | [下载][apk-view-tracer]     |                 |
| APT              |APT是一个Android平台高效性能测试组件，<br/>提供丰富实用的功能，适用于开发自测、<br/>定位性能瓶颈；<br/>测试人员完成性能基准测试、竞品对比测试。| [下载][APT]                 |   [教程][APT-use-guide]              |
| GT          | GT（随身调）是APP的随身调测平台，它是直接运行在手机上的“集成调测环境”(IDTE, Integrated Debug&Test Environment)。 | [下载][GT]             |    [教程][GT-use-guide]     |

[Appurify]:http://appurify.com
[Monkey]:http://developer.android.com/intl/zh-cn/tools/help/monkey.html
[Testin]:http://testin.cn
[Spoon]:http://square.github.io/spoon/
[Little Eye]:http://www.littleeye.co
[易测云]:http://www.yiceyun.com
[Emmagee]:https://code.google.com/p/emmagee/
[apk-view-tracer]:https://code.google.com/p/apk-view-tracer/
[APT]:https://code.csdn.net/Tencent/apt
[GT]:http://gt.tencent.com/index.html


[APT-use-guide]:http://www.eoeandroid.com/thread-497380-1-1.html
[GT-use-guide]:http://gt.tencent.com/docs.html

#### Android多渠道打包工具

| 名称              |      简介         |         下载地址            |    使用教程      |
|:-----------------|------------------|:--------------------------:|:---------------:|
| Umeng多渠道打包工具|                  | [下载][Umeng多渠道打包工具]   |                 |
| AppTools具       |                  | [下载][AppTools]            |                 |
| package_tool     |                  | [下载][package_tool]        |                 |
| RyApkTool        |                  | [下载][RyApkTool]           |                 |

[Umeng多渠道打包工具]:https://github.com/umeng/umeng-muti-channel-build-tool
[AppTools]:https://github.com/wubo/apptools
[package_tool]:https://github.com/ahui2823/package_tool
[RyApkTool]:http://blog.csdn.net/rydiy/article/details/7901564

#### Android Bug日志收集工具

| 名称              |      简介         |         下载地址            |    使用教程      |
|:-----------------|------------------|:--------------------------:|:---------------:|
| Crashlytics      |                  | [下载][Crashlytics]         |                 |
| ACRA             |                  | [下载][ACRA]                |                 |
| ChkBugReport     |                  | [下载][ChkBugReport]        |                 |
| Log Collector    |                  | [下载][Log Collector]       |                 |
| Android Crash Catcher|              | [下载][Android Crash Catcher] |                 |

[Crashlytics]:http://try.crashlytics.com
[ACRA]:https://github.com/ACRA/acra
[ChkBugReport]:https://github.com/sonyxperiadev/ChkBugReport
[Log Collector]:https://code.google.com/p/android-log-collector/
[Android Crash Catcher]:https://github.com/netcook/crash-catcher

#### 其他语言开发Android应用工具

| 名称              |      简介         |         下载地址            |    使用教程      |
|:-----------------|------------------|:--------------------------:|:---------------:|
| Xamarin          |                  | [下载][Xamarin]             |                 |
| Basic4android    |                  | [下载][Basic4android]       |                 |
| Scripting Layer  |                  | [下载][Scripting Layer]     |                 |
| Ruby Rhodes      |  移动设备上的Ruby  | [下载][RubyRhodes]          |                 |
| PHP for Android  |                  | [下载][PHP for Android]     |                 |
| Codename One     |                  | [下载][Codename One]        |                 |
| Touchqode        |                  | [下载][Codename One]        |                 |
| App Inventor     |                  | [下载][Codename One]        |                 |

[Xamarin]:http://xamarin.com
[Basic4android]:http://www.basic4ppc.com/index.html
[Scripting Layer]:https://code.google.com/p/android-scripting/
[RubyRhodes]:http://rhomobile.com
[PHP for Android]:http://www.phpforandroid.net/doku.php
[Codename One]:http://www.codenameone.com/index.html
[Touchqode]:http://www.touchqode.com/index.htm
[App Inventor]:https://code.google.com/p/app-inventor-releases/

#### 传感器模拟工具

| 名称              |      简介                                                        |         下载地址            |    使用教程      |
|:-----------------|------------------------------------------------------------------|:--------------------------:|:---------------:|
| Sensor Simulator | 独立的Java应用程序，它模拟传感器<br/>的数据并将它们传送到Android模拟器。 | [下载][Sensor Simulator]    |                 |

[Sensor Simulator]:http://www.openintents.org/en/node/23)

#### Android串口开发工具

| 名称                    |      简介         |         下载地址               |    使用教程      |
|:-----------------------|------------------|:------------------------------:|:---------------:|
| Android Serialport Api |                  | [下载][android-serialport-api]  |                 |

[android-serialport-api]:https://code.google.com/p/android-serialport-api/


#### 图片尺寸处理工具
| 名称                    |      简介         |         下载地址               |    使用教程      |
|:-----------------------|------------------|:------------------------------:|:---------------:|
| 9-Patch Resizer        |                  | [下载][9-Patch Resizer]         |                 |

[9-Patch Resizer]:https://github.com/redwarp/9-Patch-Resizer

#### 图片压缩工具

| 名称              |      简介         |         下载地址            |    使用教程      |
|:-----------------|------------------|:--------------------------:|:---------------:|
| OptiPNG          |                  | [下载][OptiPNG]             |                 |
| Pngcrush         |                  | [下载][Pngcrush]            |                 |
| ImageOptim       |                  | [下载][Xamarin]             |                 |

[OptiPNG]:http://optipng.sourceforge.net/
[Pngcrush]:http://pmt.sourceforge.net/pngcrush/
[ImageOptim]:https://imageoptim.com)
	
#### 资源清理工具

| 名称                      |      简介         |         下载地址                 |    使用教程      |
|:-------------------------|------------------|:--------------------------------:|:---------------:|
| Android Lint             |                  | [下载][Android Lint]              |                 |
| Android Resource Cleaner |                  | [下载][android-resource-cleaner]  |                 |
| Android Unused Resources |                  | [下载][android-unused-resources]  |                 |
| Android Resource Remover |                  | [下载][android-resource-remover]  |                 |

[Android Lint]:http://tools.android.com/tips/lint
[android-resource-cleaner]:https://code.google.com/p/android-resource-cleaner/
[android-unused-resources]:https://code.google.com/p/android-unused-resources/
[android-resource-remover]:https://github.com/KeepSafe/android-resource-remover

#### px和dp转换/计算工具

| 名称                      |      简介         |         下载地址                 |    使用教程      |
|:-------------------------|------------------|:--------------------------------:|:---------------:|
| Android dp px Calculator |                  | [下载][android dp px calculator] |                 |
| dp px converter          |                  | [下载][dp px converter]          |                 |
| pixelcalc                |                  | [下载][pixelcalc]                |                 |
| androidpixels            |                  | [下载][androidpixels]            |                 |
| android dpi calculator   |                  | [下载][android dpi calculator]   |                 |
| DPI Calculator           |                  | [下载][DPI Calculator]           |                 |

[android dp px calculator]:http://labs.rampinteractive.co.uk/android_dp_px_calculator/
[dp px converter]:http://pixplicity.com/dp-px-converter/
[pixelcalc]:http://angrytools.com/android/pixelcalc/
[androidpixels]:http://androidpixels.net
[android dpi calculator]:http://coh.io/adpi/
[DPI Calculator]:https://chrome.google.com/webstore/detail/dpi-calculator/dldofgjemhkpilajnlenfijjpkabilcg?hl=en

#### Java To iOS

| 名称              |      简介         |         下载地址            |    使用教程      |
|:-----------------|------------------|:--------------------------:|:---------------:|
| j2Objc           |                  | [下载][j2Objc]              |                 |
| RoboVM           |                  | [下载][RoboVM]              |                 |

[j2Objc]:https://github.com/google/j2objc
[RoboVM]:http://www.robovm.org

#### JSON/XML转换为POJO Class工具

| 名称                              |      简介         |         下载地址                          |    使用教程      |
|:---------------------------------|------------------|:-----------------------------------------:|:---------------:|
| jsonschema2pojo                  |                  | [下载][jsonschema2pojo]                    |                 |
| Convert XML or JSON to Java Pojo |                  | [下载][Convert XML or JSON to Java Pojo]   |                 |

[jsonschema2pojo]:http://www.jsonschema2pojo.org
[Convert XML or JSON to Java Pojo]:http://pojo.sodhanalibrary.com


#### Java DAO Generate工具

| 名称                                        |      简介         |         下载地址                                      |    使用教程      |
|:-------------------------------------------|------------------|:----------------------------------------------------:|:---------------:|
| Generate Java DAO for relational data table|                  | [下载][Generate Java DAO for relational data table]    |                 |

[Generate Java DAO for relational data table]:http://pojo.sodhanalibrary.com/GenerateDAO.html

#### Chrome插件
##### Android插件
| 名称                                                   |      简介           |         下载地址                            |    使用教程      |
|:------------------------------------------------------|---------------------|:------------------------------------------:|:---------------:|
| Android SDK Search                                    |                     | [下载][Android SDK Search]                  |                 |
| Android Resource Navigator                            |                     | [下载][Android Resource Navigator]          |                 |
| ADB Plugin for remote <br/>debugging Chrome on Android|                     | [下载][ADBPluginforremotedebugging]        |                 |
| Mobile/RWD Tester                                     |                     | [下载][Mobile/RWD Tester]                   |                 |
| ExtensionAndroid SDK Samples Search                   |                     | [下载][ExtensionAndroid SDK Samples Search] |                 |
| Android Developer Improvements                        |                     | [下载][Android Developer Improvements]      |                 |
| Android downloader                                    |                     | [下载][Android downloader]                  |                 |

[Android SDK Search]:https://chrome.google.com/webstore/detail/android-sdk-search/hgcbffeicehlpmgmnhnkjbjoldkfhoin
[Android Resource Navigator]:https://chrome.google.com/webstore/detail/android-resource-navigato/agoomkionjjbejegcejiefodgbckeebo?hl=en
[ADBPluginforremotedebugging]:https://chrome.google.com/webstore/detail/adb/dpngiggdglpdnjdoaefidgiigpemgage?hl=en
[Mobile/RWD Tester]:https://chrome.google.com/webstore/detail/mobilerwd-tester/elmekokodcohlommfikpmojheggnbelo?hl=en
[ExtensionAndroid SDK Samples Search]:https://chrome.google.com/webstore/detail/android-sdk-samples-searc/mbiobcenjhldinmnbpjihaemkfofnmgf?hl=en
[Android Developer Improvements]:https://chrome.google.com/webstore/detail/android-developer-improve/omakkdelnjjgfmohpfkejgfcckpkbhbj?hl=en
[Android downloader]:https://chrome.google.com/webstore/detail/android-downloader/pkffcfhlacdchhpahlgcajjiiljobbbb?hl=en

##### JSON/XML格式化插件

| 名称              |      简介         |         下载地址            |    使用教程      |
|:-----------------|------------------|:--------------------------:|:---------------:|
| JSONView         |                  | [下载][JSONView]            |                 |
| JSON Formatter   |                  | [下载][JSON Formatter]      |                 |
| JSON Viewer      |                  | [下载][JSON Viewer]         |                 |
| JSON Finder      |                  | [下载][JSON Finder]         |                 |

[JSONView]:https://chrome.google.com/webstore/detail/jsonview/chklaanhfefbnpoihckbnefhakgolnmc?hl=en		
[JSON Formatter]:https://chrome.google.com/webstore/detail/json-formatter/bcjindcccaagfpapjjmafapmmgkkhgoa?hl=en		
[JSON Viewer]:https://chrome.google.com/webstore/detail/json-viewer/gbmdgpbipfallnflgajpaliibnhdgobh?hl=en		
[JSON Finder]:https://chrome.google.com/webstore/detail/json-finder/flhdcaebggmmpnnaljiajhihdfconkbj?hl=en


[XML Tree]:https://chrome.google.com/webstore/detail/xml-tree/gbammbheopgpmaagmckhpjbfgdfkpadb?hl=en

##### Encode/Decode插件

| 名称                     |      简介         |         下载地址                  |    使用教程      |
|:------------------------|------------------|:---------------------------------:|:---------------:|
| Base64 Encode and Decode|                  | [下载][Base64 Encode and Decode]   |                 |

[Base64 Encode and Decode]:https://chrome.google.com/webstore/detail/base64-encode-and-decode/kcafoaahiffdjffagoegkdiabclnkbha?hl=en

##### Git

| 名称              |      简介         |         下载地址            |    使用教程      |
|:-----------------|------------------|:--------------------------:|:---------------:|
| Git Cheat Sheet  |                  | [下载][Git Cheat Sheet]    |                 |

[Git Cheat Sheet]:https://chrome.google.com/webstore/detail/git-cheat-sheet/mjdmgoiobnbkfcfjcceaodlcodhpokgn?hl=en

##Guides

#### Google Java编程风格指南中文版

英文地址：[http://google-styleguide.googlecode.com/svn/trunk/javaguide.html](http://google-styleguide.googlecode.com/svn/trunk/javaguide.html)

地址0：[http://hawstein.com/posts/google-java-style.html](http://hawstein.com/posts/google-java-style.html)

地址1：[https://github.com/codeset/google-java-styleguide](https://github.com/codeset/google-java-styleguide)

#### Android Api中文版
地址：[http://wikidroid.sinaapp.com/Android中文API](http://wikidroid.sinaapp.com/Android中文API))

####Android API指南中文版

地址：[http://wiki.eoeandroid.com/Android_API_Guides](http://wiki.eoeandroid.com/Android_API_Guides)

#### Android Proguard混淆配置指南

地址：[https://github.com/inferjay/AndroidProguardGuide/](https://github.com/inferjay/AndroidProguardGuide/)

#### Gradle插件使用指南中文版

地址：[http://avatarqing.github.io/Gradle-Plugin-User-Guide-Chinese-Verision](http://avatarqing.github.io/Gradle-Plugin-User-Guide-Chinese-Verision)

####Gradle User Guide
Gradle 1.12用户指南：[http://pan.baidu.com/s/1dD7sC2d](http://pan.baidu.com/s/1dD7sC2d)

##Tutorials

#### Android学习之路

地址：[http://stormzhang.github.io/android/2014/07/07/learn-android-from-rookie/](http://stormzhang.github.io/android/2014/07/07/learn-android-from-rookie/)

####Google Android官方培训课程中文版

地址：[http://hukai.me/android-training-course-in-chinese/index.html](http://hukai.me/android-training-course-in-chinese/index.html)

#### Developing Android Apps

地址：[https://www.udacity.com/course/ud853](https://www.udacity.com/course/ud853)

#### Java Design Patterns Samples in Java.

[Java Design Patterns](https://github.com/iluwatar/java-design-patterns)

# Design
---

## Design Tools

#### Photoshop插件

| 名称              |      简介         |         下载地址            |    使用教程      |
|:-----------------|------------------|:--------------------------:|:---------------:|
| Cut&Slice        |    切图神器       | [下载][Cut&Slice]              |                 |
| DevRocket        |    切图神器       | [下载][RoboVM]              |                 |
| Cutterman        |   最好用的切图工具 | [下载][Cutterman]              |                 |
| Ink              |                  | [下载][Ink]                 |                 |
| Corner Editor    |   路径圆角编辑工具 | [下载1][Corner Editor1] <br/>[下载1][Corner Editor2]      |                 |
| GuideGuide       |   辅助线工具      | [下载][GuideGuide]          |                 |
| Assistor PS      |                  | [下载][Assistor PS]         |                 |
| Skeuomorphism.it |                  | [下载][Skeuomorphism.it]    |                 |
| QuickGuide       |                  | [下载][QuickGuide]              |                 |
| Long Shadow Generator | 长投影效果生成插件 | [下载][Long Shadow Generator]         |                 |
| android_resizer_toolkit |          | [下载][android_resizer_toolkit] |             |
| android-ps-tools | 一些方便Android UI设计的PhototShop插件。 | [下载][android-ps-tools] |             |
| LayerCraft       |A Photoshop plugin to export UI assets from layers| [下载][LayerCraft]            |                 |

[Cut&Slice]:http://www.cutandslice.me
[DevRocket]:http://devrocket.uiparade.com
[Cutterman]:http://www.cutterman.cn
[Ink]:http://ink.chrometaphore.com
[Corner Editor1]:http://photoshopscripts.wordpress.com  
[Corner Editor2]:http://sourceforge.net/projects/cornereditor/
[GuideGuide]:http://guideguide.me
[Assistor PS]:http://assistor.net/en/assistor
[Skeuomorphism.it]:http://skeuomorphism.it
[QuickGuide]:http://guchitaka.com/project-view/quickguidepro/
[Long Shadow Generator]:http://lab.rayps.com/lsg2/
[android_resizer_toolkit]:https://github.com/marcosecchi/android_resizer_toolkit
[android-ps-tools]:https://github.com/timroes/android-ps-tools
[LayerCraft]:http://lab.rayps.com/lc/

#### 矢量图设计工具

| 名称              |      简介         |         下载地址            |    使用教程      |
|:-----------------|------------------|:--------------------------:|:---------------:|
| Sketch 3         |                  | [下载][Sketch 3]            |                 |
| Affinity Designer|                  | [下载][Affinity Designer]   |                 |
| Gravit           |                  | [下载][Gravit]              |                 |
| Adobe Illustrator|                  | [下载][Adobe Illustrator]   |                 |

[Sketch 3]:http://bohemiancoding.com/sketch/
[Affinity Designer]:https://affinity.serif.com
[Gravit]:http://gravit.io
[Adobe Illustrator]:https://www.adobe.com/cn/products/illustrator.html

#### 切图工具

| 名称              |      简介         |         下载地址            |    使用教程      |
|:-----------------|------------------|:--------------------------:|:---------------:|
| Slicy           |                  | [下载][Slicy]              |                 |

[Slicy]:http://macrabbit.com/slicy/

#### 设计稿尺寸标注工具

| 名称              |      简介         |         下载地址            |    使用教程      |
|:-----------------|------------------|:--------------------------:|:---------------:|
| 马克鳗            |                  | [下载][马克鳗]              |                 |

[马克鳗]:http://www.getmarkman.com

#### 原型设计工具

| 名称              |      简介         |         下载地址            |    使用教程      |
|:-----------------|------------------|:--------------------------:|:---------------:|
| Axure            |                  | [下载][Axure]               |                 |
| Fluid UI         |                  | [下载][Fluid UI]            |                 |
| Briefs           |                  | [下载][Briefs]              |                 |
| Flinto           |                  | [下载][Flinto]              |                 |
| Balsamiq Mockups |                  | [下载][Balsamiq Mockups]    |                 |
| AppCooker        |                  | [下载][AppCooker]           |                 |
| Proto.io         |                  | [下载][Proto.io]            |                 |
| UXPin            |                  | [下载][UXPin]               |                 |
| InVision         |                  | [下载][InVision]            |                 |
| POP              |                  | [下载][POP]                 |                 |
| 快现              |                  | [下载][快现]                |                 |
| Composite        |                  | [下载][Composite]           |                 |
| OmniGraffle      |                  | [下载][OmniGraffle]         |                 |
| Marvelapp        |                  | [下载][Marvelapp]           |                 |
| Justinmind       |                  | [下载][Justinmind]          |                 |
| Form             |                  | [下载][Form]                |                 |
| Prott            |                  | [下载][Prott]               |                 |
| Composite        |                  | [下载][Composite]           |                 |
| Avocado          |                  | [下载][Avocado]             |                 |
| Pixate           |                  | [下载][Pixate]              |                 |

[Axure]:http://www.axure.com
[Fluid UI]:https://chrome.google.com/webstore/detail/fluid-ui/obgmmkbgpilmggfkhganmcmpemnhimgg?hl=en
[Briefs]:http://giveabrief.com
[Flinto]:https://www.flinto.com
[Balsamiq Mockups]:http://balsamiq.com/products/mockups/
[AppCooker]:http://www.appcooker.com
[Proto.io]:https://proto.io/en/signup/
[UXPin]:http://uxpin.com/#
[InVision]:http://www.invisionapp.com
[POP]:https://popapp.in
[快现]:http://www.ikuaixian.com
[Composite]:http://www.getcomposite.com
[OmniGraffle]:https://www.omnigroup.com/omnigraffle
[Marvelapp]:https://marvelapp.com
[Justinmind]:http://www.justinmind.com/
[Form]:http://www.relativewave.com/form.html
[Prott]:https://prottapp.com
[Composite]:http://www.getcomposite.com/
[Avocado]:https://github.com/ideo/avocado
[Pixate]:http://www.pixate.com/

#### 交互设计工具

| 名称              |      简介         |         下载地址            |    使用教程      |
|:-----------------|------------------|:--------------------------:|:---------------:|
| Framer Studio    |                  | [下载][Framer Studio]       |                 |
| Quartz Composer  |                  | [下载][Quartz Composer]     |                 |
| Origami          |                  | [下载][Origami]             |                 |
| jQC              |                  | [下载][jQC]                 |                 |

[Framer Studio]:http://framerjs.com
[Quartz Composer]:http://adcdownload.apple.com/Developer_Tools/graphics_tools_for_xcode__march_2014/graphics_tools_for_xcode_5.1__march_2014.dmg
[Origami]:http://facebook.github.io/origami/
[jQC]:http://qcdesigners.com/index.php/forums

#### UI效果预览工具

| 名称                     |      简介         |         下载地址               |    使用教程      |
|:------------------------|------------------|:------------------------------:|:---------------:|
| Android Design Preview  |                  | [下载][Android Design Preview]  |                 |
| PS Play                 |                  | [下载][PS Play]                 |                 |
| Pixl Preview            |                  | [下载][Pixl Preview]            |                 |
| Skala Preview           |                  | [下载][Skala Preview]           |                 |
| LiveView                |                  | [下载][LiveView]                |                 |

[Android Design Preview]:https://github.com/romannurik/AndroidDesignPreview/releases
[PS Play]:http://isux.tencent.com/app/psplay
[Pixl Preview]:https://play.google.com/store/apps/details?id=at.markushi.pixl
[Skala Preview]:http://bjango.com/mac/skalapreview/
[LiveView]:http://www.zambetti.com/projects/liveview/

#### 配色工具

| 名称                                 |      简介         |         下载地址                            |    使用教程      |
|:------------------------------------|------------------|:-------------------------------------------:|:---------------:|
| Android Material Design可视化调色板   |                  | [下载][Android Material Design可视化调色板]   |                 |
| Android Material Design Colours.xml |                  | [下载][Android Material Design Colours.xml]  |                 |
| Colorube配色神器                     |                  | [下载][Colorube配色神器]                      |                 |
| Adobe Kuler                         |                  | [下载][Adobe Kuler]                          |                 |
| ColorSchemer Studio                 |                  | [下载][ColorSchemer Studio]                  |                 |
| Piknik                              |                  | [下载][Android Material Design Colours.xml]  |                 |

[Android Material Design可视化调色板]:https://github.com/HozakaN/MaterialDesignColorPalette
[Android Material Design Colours.xml]:https://gist.github.com/daniellevass/b0b8cfa773488e138037
[Colorube配色神器]:http://www.fancynode.com/colorcube/
[Adobe Kuler]:https://kuler.adobe.com/zh/create/color-wheel/
[ColorSchemer Studio]:http://www.colorschemer.com
[Piknik]:http://color.aurlien.net

#### 设计稿版本控制工具

| 名称              |      简介         |         下载地址            |    使用教程      |
|:-----------------|------------------|:--------------------------:|:---------------:|
| LayerVault       |                  | [下载][LayerVault]          |                 |

[LayerVault]:https://layervault.com

#### 图标处理工具

| 名称              |      简介         |         下载地址            |    使用教程      |
|:-----------------|------------------|:--------------------------:|:---------------:|
| Icon Slate       |                  | [下载][Icon Slate]          |                 |

[Icon Slate]:http://www.kodlian.com/apps

#### 在线Icon库

| 名称              |      简介         |         下载地址            |    使用教程      |
|:-----------------|------------------|:--------------------------:|:---------------:|
| IconFont         |                  | [下载][IconFont]            |                 |
| NounProject      |                  | [下载][NounProject]         |                 |

[IconFont]:http://iconfont.cn
[NounProject]:http://thenounproject.com

#### 取色工具

| 名称              |      简介         |         下载地址            |    使用教程      |
|:-----------------|------------------|:--------------------------:|:---------------:|
| ColorSnapper     |                  | [下载][ColorSnapper]        |                 |

[ColorSnapper]:http://colorsnapper.com

#### 不透明度16进制值

| 不透明度 | 16进制值 |
|:------:|:-------:|
| 100%   |    FF   |
| 95%    |    F2   |
| 90%    |    E6   |
| 85%    |    D9   |
| 80%    |    CC   |
| 75%    |    BF   |
| 70%    |    B3   |
| 65%    |    A6   |
| 60%    |    99   |
| 55%    |    8C   |
| 50%    |    80   |
| 45%    |    73   |
| 40%    |    66   |
| 35%    |    59   |
| 30%    |    4D   |
| 25%    |    40   |
| 20%    |    33   |
| 15%    |    26   |
| 10%    |    1A   |
| 5%     |    0D   |
| 0%     |    00   |

出自：[http://stackoverflow.com/questions/5445085/understanding-colors-in-android-6-chars](http://stackoverflow.com/questions/5445085/understanding-colors-in-android-6-chars)

#### 手机To电脑同步预览工具

| 名称              |      简介         |         下载地址            |    使用教程      |
|:-----------------|------------------|:--------------------------:|:---------------:|
| Reflector        |                  | [下载][Reflector]           |                 |
| x-Mirage         |                  | [下载][x-Mirage]            |                 |
| AirServer        |                  | [下载][AirServer]           |                 |

[Reflector]:http://www.airsquirrels.com/reflector/download/
[x-Mirage]:http://x-mirage.com/x-mirage/
[AirServer]:http://www.airserver.com

#### Gif图片录制工具

| 名称              |      简介         |         下载地址            |    使用教程      |
|:-----------------|------------------|:--------------------------:|:---------------:|
| LICEcap          |                  | [下载][LICEcap]             |                 |

[LICEcap]:http://www.cockos.com/licecap/

## UI Programming Language

[UILang](http://uilang.com)

## Tutorials

[HackDesign](https://hackdesign.org/lessons)

## Games

[The Bezier Game](http://bezier.method.ac)

一个帮助你练习PS里钢笔工具的小游戏。

## Guides

####Android设计指南非官方简体中文版

Topfun镜像地址：[http://www.topfun.us/adchs/index.html](http://www.topfun.us/adchs/index.html)

Github镜像地址：[http://adchs.github.io](http://adchs.github.io)

ApkBus镜像地址：[http://www.apkbus.com/design/](http://www.apkbus.com/design/)

Segmentfault镜像地址：[http://mirrors.segmentfault.com/adchs/](http://mirrors.segmentfault.com/adchs/)

多看阅读镜像地址：[http://www.duokan.com/book/47790](http://www.duokan.com/book/47790)

####Android Cheatsheet for Graphic Designers

地址:[http://petrnohejl.github.io/Android-Cheatsheet-For-Graphic-Designers/](http://petrnohejl.github.io/Android-Cheatsheet-For-Graphic-Designers/)

####Google Material Design 中文版

地址：[http://design.1sters.com](http://design.1sters.com)

地址： [http://www.ui.cn/Material/](http://www.ui.cn/Material/)

#### Designer's Guide To dpi

地址：[http://sebastien-gabriel.com/designers-guide-to-dpi/home](http://sebastien-gabriel.com/designers-guide-to-dpi/home#)

#### Email Design Guide

地址：[http://mailchimp.com/resources/email-design-guide/](http://mailchimp.com/resources/email-design-guide/)

## Free Design Resources

[Google Material Design 素材](http://pan.baidu.com/s/1i35iBNv)(感谢 [@SanityD](http://weibo.com/sanityd))

[Material Design Icon Templates](https://dribbble.com/shots/1617724)

[Material Design的图标集](https://github.com/google/material-design-icons)

[Material Design UI Kit for Sketch](https://www.behance.net/gallery/20514895/Material-Design-UI-Kit)

[Nexus 5 template for Sketch](http://tristanremy.com/nexus-5/)

[Free Design Resources](http://androiduiux.com/free-design-resources/?blogsub=confirming#blog_subscription-2)

[434 SVG icons](https://dl.dropboxusercontent.com/u/8067075/System%20Icons.zip)

[UI Cloun](http://ui-cloud.com)

[161个国内外社交网站矢量图标](http://github.com/nullice/NViconsLib_Silhouette)

[250 free icons in 5 sizes and 14 colors](http://www.androidicons.com)

# Books
---

[Free Programming Books](https://github.com/vhf/free-programming-books/blob/master/free-programming-books.md#android)

一堆免费的Android开发相关的电子书。

[50 Android Hacks](http://www.it-ebooks.info/book/2445/)

50 Android Hacks这本书分12个部分介绍了50个Android开发的小技巧。

# License
---

```
Copyright 2014 inferjay (http://www.androiddevtools.cn)
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

	http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```