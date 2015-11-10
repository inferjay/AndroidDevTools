AndroidDevTools
===============

[![Gitter](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/inferjay/AndroidDevTools?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

**Android Dev Tools官网地址：[www.androiddevtools.cn](http://www.androiddevtools.cn)**

收集整理Android开发所需的Android SDK、开发中用到的工具、Android开发教程、Android设计规范，免费的设计素材等。

欢迎大家推荐自己在Android开发过程中用的好用的工具、学习开发教程、用到设计素材，欢迎Star、Fork 😄。

#Android Tools
---

####Android SDK在线更新镜像服务器

1. 中国科学院开源协会镜像站地址:

   * IPV4/IPV6: `http://mirrors.opencas.cn` 端口：80

   * IPV4/IPV6: `http://mirrors.opencas.org` 端口：80

   * IPV4/IPV6: `http://mirrors.opencas.ac.cn` 端口：80

	
1. 上海GDG镜像服务器地址:

	* `http://sdk.gdgshanghai.com `  端口：8000	

1. 北京化工大学镜像服务器地址: 
   	
   * IPv4: `http://ubuntu.buct.edu.cn/` 端口：80
   
   * IPv4: `http://ubuntu.buct.cn/`   端口：80
   
   * IPv6: `http://ubuntu.buct6.edu.cn/`  端口：80
	
1. 大连东软信息学院镜像服务器地址: 

	* `http://mirrors.neusoft.edu.cn` 端口：80

1. 腾讯Bugly 镜像:

	* `http://android-mirror.bugly.qq.com` 端口：8080

	腾讯镜像使用方法: [http://android-mirror.bugly.qq.com:8080/include/usage.html](http://android-mirror.bugly.qq.com:8080/include/usage.html)

**使用方法**：
	
1. 启动 Android SDK Manager ，打开主界面，依次选择『**Tools**』、『**Options...**』，弹出『**Android SDK Manager - Settings**』窗口；

2. 在『**Android SDK Manager - Settings**』窗口中，在『**HTTP Proxy Server」和「HTTP Proxy Port**』输入框内填入上面镜像服务器地址(**不包含http://**，如下图)和端口，并且选中『**Force https://... sources to be fetched using http://...**』复选框。设置完成后单击『**Close**』按钮关闭『**Android SDK Manager - Settings**』窗口返回到主界面；

3. 依次选择『**Packages**』、『**Reload**』。

	<img src="static/image/sdk-manager-proxy-settings.png" width="40%" height="20%" alt="SDK Manager Proxy Settings">

####Android Studio
| 版本号  |   Windows         |       Mac OSX     |       Linux     |       SHA-1校验码     |       官方SHA-1校验码截图     |
|:------:|:--------------:|:-----------------:|:------------------:|:------------------|:------------------:|
|  1.5 Preview 2 | [下载][1.5-p2-win] | [下载][1.5-p2-mac] | [下载][1.5-p2-linux] | Win: c2cee3431c46f5ed0a8d63b782dda03ea47a01b8 <br/> Mac:  4597821e2a5c77d6746d834d78aeacb198d698ee <br/> Linux:  2730200226c35f2fb19ffbf1e24275478cab69d6 |  [查看][1.5-p2-sha1] |
|  1.5 Preview 1 | [下载][1.5-p1-win] | [下载][1.5-p1-mac] | [下载][1.5-p1-linux] | Win: 0451f37afbedde5f902b32ca3fc1a6347ff2c399 <br/> Mac:  2c22b58ff6158cd90bbad54aefeb273f632df3c0 <br/> Linux:  acdae82efe8e4c0b4f903764b50c7064d47c7910 |  [查看][1.5-p1-sha1] |
|  1.4 | [下载][1.4-win] | [下载][1.4-mac] | [下载][1.4-linux] | Win: a2f0141d35f8f0c24dad2ff390e7f6231c5f7625 <br/> 82d0d9c78ec23834956f941a07821be347fcb7bf <br/> c0851dc9a506ba9f4c1379a3e9b4019c08478220 <br/> Mac:  27068d59d5a78717d31bdedd054082b5c50d3897 <br/> d99c4b3efce46edba97a2cb8f53fc62d267b9015 <br/> Linux: 137e3734f2e8e285bd7c1d2fae2e8548d0f164bd  | [查看][1.4-sha1]  |
|  1.4 RC3 | [下载][1.4-rc3-win] | [下载][1.4-rc3-mac] | [下载][1.4-rc3-linux] |  Win: 8f0ef33afb026b6cb513c8736c8218584f5721da <br/> Mac: 5a2f5bb23511e2422b9268ef234503cc6bc887b6 <br/>Linux: 8aa32a4603c576d7b4691c34028e3e97490b5dfd |  [查看][1.4-rc3-sha1] |
|  1.4 RC2 | [下载][1.4-rc2-win] | [下载][1.4-rc2-mac] | [下载][1.4-rc2-linux] |  Win: 0ba2a568e74cd6c5e24608db7665392feeb46dba <br/> Mac: 1736ba5ff1779ea762e42c60300985748652af30 <br/>Linux: 9976f16d6183f907229a84c48ac185259bd1b115 |  [查看][1.4-rc2-sha1] |
|  1.4 RC1 | [下载][1.4-rc1-win] | [下载][1.4-rc1-mac] | [下载][1.4-rc1-linux] |  Win: abc3144bae19459a87fe42056e13dc9508e08266 <br/> Mac: 8cd5a56139abe2661bd1315502449014e40d0c59 <br/>Linux: 2ddbd659221df5396535cfedc6305c1fb5a3c7ba |  [查看][1.4-rc1-sha1] |
|  1.4 Beta4 | [下载][1.4-beta4-win] | [下载][1.4-beta4-mac] | [下载][1.4-beta4-linux] |Win: cae242811dd4c61a4eaa20b9ba5f1d95b1720cd8 <br/> Mac: d529c563c217afcad042d6e8428ba7196a1e4bd2 <br/> Linux: 38999c08fb8093ec118bf52b93587743c954c648 |  [查看][1.4-beta4-sha1] |
|  1.4 Beta3 | [下载][1.4-beta3-win] | [下载][1.4-beta3-mac] | [下载][1.4-beta3-linux] | Win: ec2a401632011ccba5aef3370395285b615ec23a <br/> Mac: 45092982541590f3d99012626081db2ac189e222 <br/> Linux: 000c98423b2ec7b6b622fc2d0d79a54de810414e | [查看][1.4-beta3-sha1]  |
|  1.4 Beta2 | [下载][1.4-beta2-win] | [下载][1.4-beta2-mac] | [下载][1.4-beta2-linux] | Win: 30ba711637a7826f818ef11b45461ad76f63067d <br/> Mac: 29a17be0d7dcd7e0271acea1f3fad0a357fcd916 <br/>Linux: 03725ca59e3b4b0ab13ab29bf723c1d77087a3ed | [查看][1.4-beta2-sha1]  |
|  1.4 Beta | [下载][1.4-beta-win] | [下载][1.4-beta-mac] | [下载][1.4-beta-linux] | Win: db741cff551c6ef88f2282e9f011d02f4a0641ff <br/> Mac:  7e54e67a0cef430f7d9675d106f6ab5a3d6c24d1 <br/> Linux: 660051f68c57e6cd9c9175894e1ac17f4410805d |  [查看][1.4-beta-sha1] |
|  1.4 Preview 3 | [下载][1.4-p3-win] | [下载][1.4-p3-mac] | [下载][1.4-p3-linux] | Win: 0a312b3c49af0bd13a83c55bf4f59a135c436d01 <br/> Mac: 89d177cc025d486db47dda1aae5e2d7848e4c2ec <br/> Linux: 0c71ac09574f29c8accee52b7fef2073c78c1d61 | [查看][1.4-p3-sha1]  |
|  1.4 Preview 2 | [下载][1.4-p2-win] | [下载][1.4-p2-mac] | [下载][1.4-p2-linux] | Win: 1e44e215ba27a29501e6eb986a239572d27fbe0f <br/> Mac: fea4bb6101f82aaaea6252aefb0049587822abb5 <br/> Linux:  084ed3f84290b8807a3a4f0aba6ac9abfe65e6ab | [查看][1.4-p2-sha1]  |
|  1.4 Preview 1 | [下载][1.4-p1-win] | [下载][1.4-p1-mac] | [下载][1.4-p1-linux] | Win: e16a2827a340d610414b08e0ee9342d1404cf71b <br/> Mac:  057371941a085f78c2e62a5e06abf36a89624c32 <br/> Linux:  6e906c6c79e66440da2dd1b5c70477f564b64ef3 |  [查看][1.4-p1-sha1] |
|  1.3.2 | [下载][1.3.2-win] | [下载][1.3.2-mac] | [下载][1.3.2-linux] | Win:  c7d39c529dd434489da9d086ff689d34dc791526 <br/> b5d1aaa000729c03a3cf980add79d1b93121c56d <br/> 3134f226b5f3c3f74d4fc2d9cff03a4458f01d69 <br/> Mac: 75b67eb15a34a152a40e7189484ab0ebc375b877 <br/> Linux: cf780413f8c8223eb348bd27c19a9c04b75eaeb2
  | [查看][1.3.2-sha1]  |
|  1.3.1 | [下载][1.3.1-win] | [下载][1.3.1-mac] | [下载][1.3.1-linux] | Win: 8cff590f2e08e339f8c2491b287a840ae87c7383 <br/> d70fb49d03db9dded19c891a92452601e39272f4 <br/> 3b4c4924cb9495e56db61ca0e8c8d2bf588c4b97 <br/> Mac:  9fc12b5657ff52c761b7e7c115feade2a9728386 <br/> 3c7f934f257ab09c1ea0d88a816ec83702171e75 <br/> Linux: 51e5f5de2b82883d87f85ee38cf7b7b8b2e7debf  | [查看][1.3.1-sha1]  |

[1.5-p2-win]:http://pan.baidu.com/s/1o6rKRxC
[1.5-p2-mac]:http://pan.baidu.com/s/1eQsHgI2
[1.5-p2-linux]:http://pan.baidu.com/s/1kTJBu3X

[1.5-p1-sha1]:http://ww1.sinaimg.cn/large/8a41f469gw1excc7f1kgvj21do0ui49h.jpg

[1.5-p1-win]:http://pan.baidu.com/s/1mg3tEnm
[1.5-p1-mac]:http://pan.baidu.com/s/1hquEqLQ
[1.5-p1-linux]:http://pan.baidu.com/s/1ntCfdn7

[1.5-p1-sha1]:http://ww3.sinaimg.cn/large/8a41f469gw1ex285gx6hsj21ea0uctju.jpg

[1.4-win]:http://pan.baidu.com/s/1mg0BjMo
[1.4-mac]:http://pan.baidu.com/s/1eQAWLZs
[1.4-linux]:http://pan.baidu.com/s/1dDnsuA1

[1.4-sha1]:http://ww4.sinaimg.cn/large/8a41f469jw1ewsvf0xsumj21ki15mnce.jpg

[1.4-rc3-win]:http://pan.baidu.com/s/1kTKVYC3
[1.4-rc3-mac]:http://pan.baidu.com/s/1pJ1QVZd
[1.4-rc3-linux]:http://pan.baidu.com/s/1eQhQ7Hw

[1.4-rc3-sha1]:http://ww2.sinaimg.cn/large/8a41f469jw1ewsw2mqv0xj21cw0uswpj.jpg

[1.4-rc2-win]:http://pan.baidu.com/s/1kT1ZiuF
[1.4-rc2-mac]:http://pan.baidu.com/s/1c0nuqY0
[1.4-rc2-linux]:http://pan.baidu.com/s/1sjFugVz

[1.4-rc2-sha1]:http://ww4.sinaimg.cn/large/8a41f469jw1ewsvodjmlwj21dw0tw7eo.jpg

[1.4-rc1-win]:http://pan.baidu.com/s/1dDi7zcX
[1.4-rc1-mac]:http://pan.baidu.com/s/1ntCJpGX
[1.4-rc1-linux]:http://pan.baidu.com/s/1dD2QkCx

[1.4-rc1-sha1]:http://ww2.sinaimg.cn/large/8a41f469jw1ewbn2n3vlij21dm0tstiz.jpg

[1.4-beta4-win]:http://pan.baidu.com/s/1o65psmA
[1.4-beta4-mac]:http://pan.baidu.com/s/1dDJeMtF
[1.4-beta4-linux]:http://pan.baidu.com/s/1ntIO4Q1

[1.4-beta4-sha1]:http://ww4.sinaimg.cn/large/8a41f469jw1ewbn0se5r1j21ck0tktjh.jpg

[1.4-beta3-win]:http://pan.baidu.com/s/1qWQjExQ
[1.4-beta3-mac]:http://pan.baidu.com/s/1eQlm5yi
[1.4-beta3-linux]:http://pan.baidu.com/s/1jGH83e2

[1.4-beta3-sha1]:http://ww3.sinaimg.cn/large/8a41f469jw1ewbmozwnt4j21gm0tmgw6.jpg

[1.4-beta2-win]:http://pan.baidu.com/s/1gdg0lQr
[1.4-beta2-mac]:http://pan.baidu.com/s/1eQqB9se
[1.4-beta2-linux]:http://pan.baidu.com/s/1hqJDL8C

[1.4-beta2-sha1]:http://ww4.sinaimg.cn/large/8a41f469jw1ew9e0gtyntj21f80twqe0.jpg

[1.4-beta-win]:http://pan.baidu.com/s/1dDqDuEl
[1.4-beta-mac]:http://pan.baidu.com/s/1hqwCRKo
[1.4-beta-linux]:http://pan.baidu.com/s/1pJKfmVx

[1.4-beta-sha1]:http://ww2.sinaimg.cn/large/8a41f469jw1ew9dxlylocj21dm0to13p.jpg

[1.4-p3-win]:http://pan.baidu.com/s/1mg1UbRM
[1.4-p3-mac]:http://pan.baidu.com/s/1dDhj81j
[1.4-p3-linux]:http://pan.baidu.com/s/1eQEr6q2

[1.4-p3-sha1]:http://ww1.sinaimg.cn/large/8a41f469jw1ew9cq9msraj21h80uoqe8.jpg

[1.4-p2-win]:http://pan.baidu.com/s/1eQm6690
[1.4-p2-mac]:http://pan.baidu.com/s/1dDBBfYp
[1.4-p2-linux]:http://pan.baidu.com/s/1dD99jpf

[1.4-p2-sha1]:http://ww2.sinaimg.cn/large/8a41f469jw1ew9b2lxcfqj21kw0taaip.jpg

[1.4-p1-win]:http://pan.baidu.com/s/1i3fEP8p
[1.4-p1-mac]:http://pan.baidu.com/s/1o6kovdK
[1.4-p1-linux]:http://pan.baidu.com/s/1pJ5ldl5

[1.4-p1-sha1]:http://ww2.sinaimg.cn/large/8a41f469jw1ew9chgvb3nj21kw0xjwqw.jpg

[1.3.2-win]:http://pan.baidu.com/s/1pJ7n7WR
[1.3.2-mac]:http://pan.baidu.com/s/1sjomEJz
[1.3.2-linux]:http://pan.baidu.com/s/1ntDxrVb

[1.3.2-sha1]:http://ww4.sinaimg.cn/large/8a41f469jw1ew9cddat55j21kw0xmk2v.jpg

[1.3.1-win]:http://pan.baidu.com/s/1ntCamKx
[1.3.1-mac]:http://pan.baidu.com/s/1i3KVNLF
[1.3.1-linux]:http://pan.baidu.com/s/1o6wzdBO

[1.3.1-sha1]:http://ww3.sinaimg.cn/large/8a41f469jw1ew9c9nk7j7j21k2160tnv.jpg

####SDK Tools

| 版本号 	     | Windows             |          Mac OSX        |          Linux         |       SHA-1校验码     |       官方SHA-1校验码截图     |
|:----------|:-----------:|:------|:----------:|:------|:----------:|
| 24.3.4 | [installer_r24.3.4-windows.exe][installer_r24.3.4-win] [android-sdk_r24.3.4-windows.zip][android-sdk_r24.3.4-win] | [android-sdk_r24.3.4-macosx.zip][android-sdk_r24.3.4-mac] | [android-sdk_r24.3.4-linux.tgz][android-sdk_r24.3.4-linux] | Win: 094dd45f98a31f839feae898b48f23704f2878dd <br/> 4a8718fb4a2bf2128d34b92f23ddd79fc65839e7 <br/> Mac: 128f10fba668ea490cc94a08e505a48a608879b9 <br/> Linux: fb293d7bca42e05580be56b1adc22055d46603dd | [查看][sdk-tools-24.3.4] |


[installer_r24.3.4-win]:http://pan.baidu.com/s/1eQppdPC
[android-sdk_r24.3.4-win]:http://pan.baidu.com/s/1mg08f2K

[android-sdk_r24.3.4-mac]:http://pan.baidu.com/s/1dDlTqBB

[android-sdk_r24.3.4-linux]:http://pan.baidu.com/s/1gdsALt5

[sdk-tools-24.3.4]:http://ww1.sinaimg.cn/large/8a41f469gw1ewbnhql68uj21k20jkjw4.jpg

####SDK Platform-Tools

这是 adb, fastboot 等工具包。把解压出来的 `platform-tools` 文件夹放在 android sdk 根目录下，并把 `adb`所在的目录添加到系统 `PATH` 路径里，即可在命令行里直接访问了 adb, fastboot 等工具。

| 版本号        | Windows             |          Mac OSX        |          Linux         |
|:----------|:-------------:|:------|:----------:|
| platform-tools-r22 | [platform-tools_r22-windows.zip][platform-tools_r22-win] | [platform-tools_r22-mac.zip][platform-tools_r22-mac] | [platform-tools_r22-linux.zip][platform-tools_r22-linux] |
| platform-tools-r21 | [platform-tools_r21-windows.zip][platform-tools_r21-win] | [platform-tools_r21-mac.zip][platform-tools_r21-mac] | [platform-tools_r21-linux.zip][platform-tools_r21-linux] |
| platform-tools-r20 | [platform-tools_r20-windows.zip][platform-tools_r20-win] | [platform-tools_r20-mac.zip][platform-tools_r20-mac] | [platform-tools_r20-linux.zip][platform-tools_r20-linux] |

[platform-tools_r22-win]:http://pan.baidu.com/s/1sj4ZfTb
[platform-tools_r22-mac]:http://pan.baidu.com/s/1jG3l6Ea
[platform-tools_r22-linux]:http://pan.baidu.com/s/1c0GUTxA

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
|  22.0.0 | [下载][22.0.0-win] | [下载][22.0.0-mac] | [下载][22.0.0-linux] |
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


[22.0.0-win]:http://pan.baidu.com/s/1i3kqFHV
[22.0.0-mac]:http://pan.baidu.com/s/1jGquuqU
[22.0.0-linux]:http://pan.baidu.com/s/1dDdDne5

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

[android-11-win]:http://pan.baidu.com/s/1c0hi7Ck
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

[Images-14-win]:http://pan.baidu.com/s/1pJzIXZl
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
C/C++开发Android应用工具包,`Linux/Mac OS X 下NDK r10c`的安装方法请戳 [这里](install-method-url)

| 版本号 	  | Windows              |          Mac OSX        |          Linux         |       SHA-1校验码     |       官方SHA-1校验码截图     |
|:----------|:-------------:|:------:|:----------:|:------|:----------:|
| ndk-r10e | [32位][r10e-win-32] [64位][r10e-win-64] | [64位][r10e-mac-64] | [32位][r10e-linux-32] [64位][r10e-linux-64]  | Win: 1a82445baaf62aec3a46386ab1e5772c <br/>  8412bb4991a95e08fda50b5a44d95df7 <br/> Mac: 2cb8893a5701603519d38a7e04c50e81 <br/> Linux: c3edd3273029da1cbd2f62c48249e978 <br/> 19af543b068bdb7f27787c2bc69aba7f | [查看][ndk-r10e-sha1] |


| Additional Download (32-, 64-bit) |  Package |
|:----------|:-------------|
| r10 STL debug info | [android-ndk-r10-cxx-stl-libs-with-debug-info.zip](http://pan.baidu.com/s/1xWgUE) | 
| r9 STL debug info | [android-ndk-r9-cxx-stl-libs-with-debug-info.zip](http://pan.baidu.com/s/1c0EMn8O) |


[r10e-win-32]:http://pan.baidu.com/s/1jG7Yacm
[r10e-win-64]:http://pan.baidu.com/s/1jG5WjL8

[r10e-mac-64]:http://pan.baidu.com/s/1DKkfc

[r10e-linux-32]:http://pan.baidu.com/s/1sjoneRr
[r10e-linux-64]:http://pan.baidu.com/s/1dDAqnK1

[ndk-r10e-sha1]:http://ww1.sinaimg.cn/large/8a41f469gw1ewboorr3czj21kk0vgdmn.jpg

[install-method-url]:https://github.com/inferjay/AndroidDevTools/wiki/Installing-the-NDK-On-Linux-and-Mac-OS-X-(Darwin)

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

####ADT Plugin
离线安装ADT插件请戳[**项目wiki**](https://github.com/inferjay/AndroidDevTools/wiki/首页)

|    版本号   |
|:----------:|
|[ADT-23.0.7](http://pan.baidu.com/s/1bngDm6V)|
|[ADT-23.0.6](http://pan.baidu.com/s/1jGraNEQ)|
|[ADT-23.0.4](http://pan.baidu.com/s/1i39UM7j)|
|[ADT-23.0.3](http://pan.baidu.com/s/1hqJyLTi)|
|[ADT-23.0.2](http://pan.baidu.com/s/1bnGkEvX)|
|[ADT-23.0.0](http://pan.baidu.com/s/1sjArX7J)|
|[ADT-22.6.3](http://pan.baidu.com/s/1jGMb5yQ)|
|[AdT-22.6.1](http://pan.baidu.com/s/1pJ185Rl)|

####Gradle

|    版本号  |
|:----------|
| [gradle-2.8-all.zip](http://pan.baidu.com/s/1qW25Ndy) |
| [gradle-2.7-all.zip](http://pan.baidu.com/s/1c0g9D5m) |
| [gradle-2.6-all.zip](http://pan.baidu.com/s/1mg8JAbA) |
| [gradle-2.5-all.zip](http://pan.baidu.com/s/1jGrmKx4) |
| [gradle-2.4-all.zip](http://pan.baidu.com/s/1c0dcgfe) |
| [gradle-2.3-all.zip](http://pan.baidu.com/s/1dDEnQr3) |
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

| 名称                           |      简介        |         下载地址                  |    使用教程      |
|:------------------------------|:------------------------------|:--------------------------------:|:---------------:|
| Enjarify   					|Enjarify 是一个用 Python 写的， Google 官方开源的可以将 Dalvik 字节码转换为 Java 字节码的工具。| [下载][Enjarify]                  |                
| JEB Android Decompiler   		|                   | [下载][JEB]                       |                |
| Virtuous Ten Studio     		|                   | [下载][Virtuous Ten Studio]       |                |
| Apk文件修改工具Root Tools 		|                   | [下载][apk文件修改工具Root Tools]   |                |
| Dex文件反编译工具Dedexer  		|                   | [下载][dex文件反编译工具Dedexer]     |                |
| APK+Dex文件反编译及回编译工具 	|                   | [下载][APK+Dex文件反编译及回编译工具] |                |
| android-apktool     			|                   | [下载][android-apktool]           |                |
| Onekey Decompile Apk]			|                   | [下载][onekey-decompile-apk]      |                |
| Baksmali    					|                   | [下载][baksmali]                  |                |
| Smali     					|                   | [下载][smali]                     |                |
| AXMLPrinter2 					|                   | [下载][AXMLPrinter2]              |                |
| JAD Java Decompiler 			|                   | [下载][JAD Java Decompiler]       |                |
| JD-GUI Decompiler 			|                   | [下载][JD-GUI Decompiler]         |                |
| XJad V2.2   					|                   | [下载][XJad V2.2]                 |                |
| Android APK Decompiler		|   在线反编译工具    | [下载][Android APK Decompiler]    |  |
| JADX - Dex to Java decompiler|                   | [下载][JADX]                      |                |
| dex2jar  						|                   | [下载][dex2jar]                   |                |
| SmaliViewer 					|是一款免费的APK分析软件，无论从分析的深度<br/>还是广度来看，都是一款能够满足用户需求的产品，<br/>使您在APK分析的过程中，更加得心应手。 | [下载][SmaliViewer]               |      [使用指南][SmaliViewer-guide]          |
| Android逆向助手 					|Android逆向助手是一功能强大的逆向辅助软件。<br/>该软件可以帮助用户来进行apk反编译打包签名；<br/>dex/jar互转替换提取修复；so反编译；<br/>xml、txt加密；字符串编码等等，操作简单<br/>，只需要直接将文件拖放到源和目标文件。 | [下载][Android逆向助手]               |            [使用指南][Android逆向助手-guide]    |
| Android Killer 			|Android Killer 是一款可视化的安卓应用逆向工具，<br/>集Apk反编译、Apk打包、Apk签名，编码互转，<br/>ADB通信（应用安装-卸载-运行-设备文件管理）<br/>等特色功能于一 身，支持logcat日志输出，<br/>语法高亮，基于关键字（支持单行代码或多行代码段）<br/>项目内搜索，可自定义外部工具；吸收融汇多种工具功能与特点，<br/>打造一站 式逆向工具操作体验，大大简化了用户在<br/>安卓应用/游戏修改过程中的各类繁琐工作。| [下载1][Android-Killer-pd521]<br/>[下载2][Android-Killer-baidu]|[使用指南][Android-Killer-guide]    |
| DexExtractor |android dex extractor ，anti-shell，android 脱壳。| [下载][DexExtractor]                |               |

[JEB]:http://www.android-decompiler.com/index.php
[Virtuous Ten Studio]:http://virtuous-ten-studio.com
[apk文件修改工具Root Tools]:https://github.com/Stericson/RootTools
[dex文件反编译工具Dedexer]:http://dedexer.sourceforge.net
[APK+Dex文件反编译及回编译工具]:http://idoog.me
[onekey-decompile-apk]:https://code.google.com/p/onekey-decompile-apk/
[android-apktool]:http://ibotpeaches.github.io/Apktool/
[baksmali]:https://code.google.com/p/smali/downloads/detail?name=baksmali
[smali]:https://code.google.com/p/smali/
[AXMLPrinter2]:https://android4me.googlecode.com/files/AXMLPrinter2.jar
[JAD Java Decompiler]:http://varaneckas.com/jad/
[JD-GUI Decompiler]:http://
[XJad V2.2]:http://files.cnblogs.com/arix04/XJad_V2.2.rar
[Android APK Decompiler]:http://www.decompileandroid.com/
[JADX]:https://github.com/skylot/jadx
[dex2jar]:https://code.google.com/p/dex2jar/
[SmaliViewer]:http://blog.avlyun.com/wp-content/uploads/2014/04/SmaliViewer.zip
[Android逆向助手]:http://enjoycode.info/uploads/Androidnxzs.zip
[Android-Killer-pd521]:http://www.pd521.com/thread-136-1-1.html
[Android-Killer-baidu]:http://pan.baidu.com/share/home?uk=4099707276#category/type=6
[Enjarify]:https://github.com/google/enjarify
[DexExtractor]:https://github.com/bunnyblue/DexExtractor


[SmaliViewer-guide]:http://blog.avlyun.com/show/《sv用户指南》/
[Android逆向助手-guide]:http://www.sanwho.com/620.html
[Android-Killer-guide]:http://www.pd521.com/thread-509-1-1.html


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

#### 静态代码分析工具
| 名称                      |      简介        |         下载地址            |    使用教程      |
|:-------------------------|:-----------------|:--------------------------:|:---------------:|
| infer | Facebook 开源的静态代码分析工具，用于在发布移动应用之前对代码进行分析，找出潜在的问题。 | [下载][infer]  |                 |

[infer]:https://github.com/facebook/infer

#### 搜索工具
| 名称                      |      简介        |         下载地址            |    使用教程      |
|:-------------------------|:-----------------|:--------------------------:|:---------------:|
| Structural Java Exception Search| Java异常搜索工具  | [下载][Structural-Java-Exception-Search]  |                 |
| Android Library Finder | 最快的方式获取依赖库  |          [下载][AFLI]      |                 |
| Codota                 |     示例代码搜索网站  |           [下载][codota]  |                 |

[Structural-Java-Exception-Search]:http://www.brainleg.com/search
[AFLI]:https://github.com/cesarferreira/alfi
[codota]:http://www.codota.com


#### Debug调试工具
| 名称                      |      简介        |         下载地址            |    使用教程      |
|:-------------------------|:-----------------|:--------------------------:|:---------------:|
| Stetho        | Stetho 是Facebook推出的Android 调试平台，基于 Chrome Developer Tools ，调试网络请求方面特别方便。 | [下载][Stetho]             |    [教程][Stetho-use-guide]     |
|Augmented Traffic Control|Facebook宣布开源移动网络测试工具ATC，该工具支持利用Wi-Fi网络模拟2G、2.5G、3G以及LTE 4G移动网络环境，让测试工程师们能够快速对智能手机和App在不同国家地区和应用环境下的性能表现进行测试。| [下载][Augmented-Traffic-Control]  |                 |

[Stetho]:https://github.com/facebook/stetho
[Augmented-Traffic-Control]:https://github.com/facebook/augmented-traffic-control

### Api测试工具
| 名称                      |      简介        |         下载地址            |    使用教程      |
|:-------------------------|:-----------------|:--------------------------:|:---------------:|
| 	bat 					| 一个用Go写的命令行API测试利器，支持文件下载，<br/>文件上传，支持Linux的pipe方式，总之就是炫酷。 | [下载][Structural-Java-Exception-Search]  | [使用指南][bat-guide] |

[bat]:https://github.com/astaxie/bat

[bat-guide]:https://github.com/astaxie/bat#installation

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
| Android Holo Colors IDEA Plugin             | [下载][Android Holo Colors IDEA Plugin]                            |                 |
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
| Color themes for IntelliJ IDEA       	   | [下载][android-drawable-importer-intellij-plugin] |                 |
| GsonFormat       	   | [下载][GsonFormat] |                 |
| ormlite-android-gradle-plugin       	   | [下载][ormlite-android-gradle-plugin] |                 |

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
[Color-themes-for-IntelliJ-IDEA]:http://www.ideacolorthemes.org/home/
[GsonFormat]:https://github.com/zzz40500/GsonFormat
[ormlite-android-gradle-plugin]:https://github.com/stephanenicolas/ormlite-android-gradle-plugin

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
|Android SVG to VectorDrawable|一个可以将SVG图片转换为Vector Drawable xml文件的在线工具。| [下载][Android-SVG-to-VectorDrawable]  |                 |

[AndroidKickstartR]:http://androidkickstartr.com
[Android Button Maker]:http://angrytools.com/android/button/
[DroidDraw]:https://code.google.com/p/droiddraw/
[Android-SVG-to-VectorDrawable]:http://inloop.github.io/svg2android/ 

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
| Mobile-Checker | 移动端页面检查工具,可以选择三种屏幕规格，通过工具发现网站在移动端存在的问题。 | [下载][Mobile-Checker]             |         |


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
[Mobile-Checker]:https://github.com/w3c/Mobile-Checker


[APT-use-guide]:http://www.eoeandroid.com/thread-497380-1-1.html
[GT-use-guide]:http://gt.tencent.com/docs.html
[Stetho-use-guide]:http://facebook.github.io/stetho/

#### Android多渠道打包工具

| 名称              |      简介         |         下载地址            |    使用教程      |
|:-----------------|------------------|:--------------------------:|:---------------:|
| Umeng多渠道打包工具|                  | [下载][Umeng多渠道打包工具]   |                 |
| AppTools具       |                  | [下载][AppTools]            |                 |
| package_tool     |                  | [下载][package_tool]        |                 |
| RyApkTool        |                  | [下载][RyApkTool]           |                 |
| 兰贝壳儿          |                  | [下载][兰贝壳儿]             |  [教程][兰贝壳教程]         |

[Umeng多渠道打包工具]:https://github.com/umeng/umeng-muti-channel-build-tool
[AppTools]:https://github.com/wubo/apptools
[package_tool]:https://github.com/ahui2823/package_tool
[RyApkTool]:http://blog.csdn.net/rydiy/article/details/7901564
[兰贝壳儿]:http://www.orchidshell.com


[兰贝壳教程]:http://www.orchidshell.com/Instructions/OchidShellInstructions.htm

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
| ImageOptim       |                  | [下载][ImageOptim]             |                 |
| Tinypng          |                  | [下载][tinypng]             |                 |

[OptiPNG]:http://optipng.sourceforge.net/
[Pngcrush]:http://pmt.sourceforge.net/pngcrush/
[ImageOptim]:https://imageoptim.com)
[tinypng]:https://tinypng.com/
	
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
| Android DPI Calculator插件|                  | [下载][Android DPI Calculator]   |                 |

[android dp px calculator]:http://labs.rampinteractive.co.uk/android_dp_px_calculator/
[dp px converter]:http://pixplicity.com/dp-px-converter/
[pixelcalc]:http://angrytools.com/android/pixelcalc/
[androidpixels]:http://androidpixels.net
[android dpi calculator]:http://coh.io/adpi/
[DPI Calculator]:https://chrome.google.com/webstore/detail/dpi-calculator/dldofgjemhkpilajnlenfijjpkabilcg?hl=en
[Android DPI Calculator]:https://github.com/JerzyPuchalski/Android-DPI-Calculator

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

#### Android Developers 国内镜像站

地址: [Android Developers 国内镜像站](http://androiddoc.qiniudn.com/)

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
| PxCook像素大厨    |UI设计师效率提升利器，让你专注于设计本质，<br/>不再为标注切图而烦恼，从设计到实现一气呵成| [下载][PxCook]              |      [使用教程][PxCook-guide]     |

[马克鳗]:http://www.getmarkman.com
[PxCook]:http://www.fancynode.com.cn

[PxCook-guide]:http://www.fancynode.com.cn/tutorial

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
| BBQScreen        |                  | [下载][BBQScreen]           |                 |

[Reflector]:http://www.airsquirrels.com/reflector/download/
[x-Mirage]:http://x-mirage.com/x-mirage/
[AirServer]:http://www.airserver.com
[BBQScreen]:http://screen.bbqdroid.org

#### Gif图片录制工具

| 名称              |      简介         |         下载地址            |    使用教程      |
|:-----------------|------------------|:--------------------------:|:---------------:|
| LICEcap          |                  | [下载][LICEcap]             |                 |
| GifCam           |                  | [下载][GifCam]              |                 |
| Android Tool     |                  | [下载][androidtool-mac]     |                 |

[LICEcap]:http://www.cockos.com/licecap/
[GifCam]:http://blog.bahraniapps.com/gifcam/
[androidtool-mac]:https://github.com/mortenjust/androidtool-mac

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

[MINIMALISTIC EVERYDAY ICONS](http://matt-cooper.com/minimalistic-icons/)

[Icons4Android](http://www.icons4android.com)

# Books
---

[Free Programming Books](https://github.com/vhf/free-programming-books/blob/master/free-programming-books.md#android)

一堆免费的Android开发相关的电子书。

[50 Android Hacks](http://www.it-ebooks.info/book/2445/)

50 Android Hacks这本书分12个部分介绍了50个Android开发的小技巧。

[免费的编程中文书籍索引](http://siberiawolf.com/free_programming/index.html)

# Disclaimer
---

	版权归原作者所有，这里仅做收集整理，欢迎自由转载-非商用-非衍生-保持署名和链接。
