# Ubuntu 配置

[TOC]

## 1. 软件安装

## 1.1. 常用命令
1. 压缩解压缩
```bash
# zip文件
zip books.zip
zip -r books.zip folder1 folder2
```

## 1.2. 玩客云

1. 安装samba服务、nfs服务
```bash
sudo apt install samba-client samba-common
sudo apt install nfs-common
```
2. 查看Samba服务磁盘
```bash
smbclient -L 192.168.1.99 -N
```
3. 在mnt下创建文件
```bash
sudo mkdir -p /mnt/onecloud
```
4. 挂载分区
```bash
sudo mount -t cifs //192.168.1.99/F401/onecloud /mnt/onecloud -o username="root",password="xiachang"
```
5. 卸载NAS
```bash
sudo umount /mnt/onecloud
```
