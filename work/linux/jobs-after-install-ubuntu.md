#  After install Ubuntu 16.04
> [荒岛书生](http://www.lidaxiang.cn/)  
> StartTime: 2017-12-15,ModifyTime:2017-12-15

# The jobs needed after installing Ubuntu 16.04
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
