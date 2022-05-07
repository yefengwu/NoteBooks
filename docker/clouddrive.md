---
title: clouddrive 
slug: cloud 
tag:
    - cloud 
    - drive
category:
    - linux
status: publish
thumbnail: images/13.jpg
---

## dockerhub
```bash
docker pull cloudnas/clouddrive
```

## Build
```bash
docker run -d \
      --name clouddrive \
      --restart unless-stopped \
      -v $HOME/clouddrive:/CloudNAS:shared \
      -v $HOME/clouddrive/config:/Config \
      -v $HOME/clouddrive/media:/media:shared \
      -e PUID=$UID \
      -e PGID=$GID \
      --network host \
      --pid host \
     --privileged \
     --device /dev/fuse:/dev/fuse \
     cloudnas/clouddrive
```
