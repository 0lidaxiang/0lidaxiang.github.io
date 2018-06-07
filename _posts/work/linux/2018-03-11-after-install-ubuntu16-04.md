---
layout: post
title:  "After Install Ubuntu 16-04"
rootCate: "work"
categories:
- Linux
tags:
- work
- Linux
- Ubuntu
- Ubuntu-Install
---

> StartTime: 2018-03-11,ModifyTime: 2018-03-12
<!---more--->

## 1.firefox
firefox account settings：login to the account and change search energering

## 2.gnome
sudo apt install gnome gnome-shell
https://extensions.gnome.org/extension/307/dash-to-dock/  
setting:  
1. dash extension 位置和大小：所有显示屏显示，左侧显示，智能隐藏关闭，Dock大小限制，图标大小
2. dash extension 外观：收缩dash，自定义颜色和透明度固定
3. 电源页面修改，窗口以及顶部栏的修改

## 3.sogou
First to ensure the fctix is installed. [download link](https://pinyin.sogou.com/linux/?r=pinyin)
 and then install by the deb.

[install sogou-input more info](http://blog.csdn.net/iamplane/article/details/70447517)

## 4.chrome & atom
[install google-chrome more info](https://askubuntu.com/questions/510056/how-to-install-google-chrome)
```
wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add
echo 'deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main' | sudo tee /etc/apt/sources.list.d/google-chrome.list
sudo add-apt-repository ppa:webupd8team/atom  
sudo apt-get update
sudo apt-get install google-chrome-stable atom
```
### [atom setting](../tools/editor-tools.html)

**atom installed more info:**  
 [first way is the method above](http://tipsonubuntu.com/2016/08/05/install-atom-text-editor-ubuntu-16-04/)  
another way:  
```
sudo snap install atom --classic;sudo snap refresh atom
```

## 5.sudo apt install
```
sudo apt install python3-pip vim git
```

## 6.mysql-server
[install mysql more info](https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-16-04)
```
sudo apt-get install mysql-server
```

## 7.pip3
```
pip3 install --upgrade pip;sudo pip3 install numpy django pandas tensorflow mysqlclient
```

## 8.local machine
```
cd ~;ssh-keygen -t rsa -b 4096 -C "0lidaxiang@gmail.com"
cat .ssh/id_rsa.pub
```
then copy this string,open [this github link](https://github.com/settings/keys), create a new ssh-key.

```
cd ~;mkdir github
```
then to git clone the repositorys needed.

## change language
change language for english  
reboot  
change language for chinese  
```
sudo apt update;sudo apt upgrade
```

## More software install
[python3.6](http://blog.csdn.net/lzzyok/article/details/77413968)


## The jobs needed after installing Ubuntu 16.04
enter root and look the disks:
```
sudo -i
fdisk -l
```

check is or not active:
```
pvscan
vgchange -a y
lvscan
```

mount :
```
mount /dev/ubuntu-vg/root /mnt/
```

## If you need to save your error ubuntu, you can try:
```
chroot /mnt
sudo add-apt-repository ppa:yannubuntu/boot-repair
apt-get install -y boot-repair
boot-repair
```
