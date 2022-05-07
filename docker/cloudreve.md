---
title: cloudreve
slug: cloudreve 
tag:
    - cloud 
    - 
category:
    - docker
status: publish
thumbnail: images/14.jpg
---

## dockerhub 
```bash
docker pull xavierniu/cloudreve   
```

## volume
```bash
mkdir -p $HOME/{cloudreve/uploads,cloudreve/downloads,cloudreve/config,cloudreve/db,cloudreve/avatar}
```

## Build
```bash
docker run -d \
  --name cloudreve \
  -e PUID=1001 \
  -e PGID=1001 \
  -e TZ="Asia/Shanghai" \
  -p 5212:5212 \
  --restart=unless-stopped \
  -v /home/frank/cloudreve/uploads:/cloudreve/uploads \
  -v /home/frank/cloudreve/config:/cloudreve/config \
  -v /home/frank/cloudreve/db:/cloudreve/db \
  -v /home/frank/cloudreve/avatar:/cloudreve/avatar \
  -v /home/frank/aria2/downloads:/downloads \
  xavierniu/cloudreve
```

## config
1. 使用`docker logs -f cloudreve`查看初始用户名和密码
2. 点击头像管理面板→存储策略→添加存储策略onedriver→应用授权第三步中选择
  ![](https://raw.githubusercontent.com/yefengwu/mdimg/main/20220507154942.png)
3. 其他的按照默认选择即可，最后用户组→存储策略选择成onedrive即可。
4. 添加ariad2节点，新版本需要编辑自带的主机节点改为aria2。
  ![](https://raw.githubusercontent.com/yefengwu/mdimg/main/20220507155033.png)
5. 填写相关的数据即可。特别注意地址需要eth0具体地址，不能为localhost/127.0.0.1. 可以为http/ws://ip:6800。注意第5项地址如果使用 p3terx/aria2-pro 必须填写/downloads。
  ![](https://raw.githubusercontent.com/yefengwu/mdimg/main/20220507155107.png)
