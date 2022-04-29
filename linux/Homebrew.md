---
title: "Homebrew"
slug: test
tag: 
    - "wordpress"
    - "python"
category:
    - "Linux"
status: publish
thumbnail: "images/2.jpg"
---

## clone repo
```bash
git clone https://github.com/Homebrew/brew.git ~/.linuxbrew  
```
## 更新环境变量
```bash
# Until LinuxBrew is fixed, the following is required.
# See: https://github.com/Homebrew/linuxbrew/issues/47
export PKG_CONFIG_PATH=/usr/local/lib/pkgconfig:/usr/local/lib64/pkgconfig:/usr/lib64/pkgconfig:/usr/lib/pkgconfig:/usr/lib/x86_64-linux-gnu/pkgconfig:/usr/lib64/pkgconfig:/usr/share/pkgconfig:$PKG_CONFIG_PATH
## Setup linux brew
export LINUXBREWHOME=$HOME/.linuxbrew  # install directory,can changed
export PATH=$LINUXBREWHOME/bin:$PATH
export MANPATH=$LINUXBREWHOME/man:$MANPATH
export PKG_CONFIG_PATH=$LINUXBREWHOME/lib64/pkgconfig:$LINUXBREWHOME/lib/pkgconfig:$PKG_CONFIG_PATH
export LD_LIBRARY_PATH=$LINUXBREWHOME/lib64:$LINUXBREWHOME/lib:$LD_LIBRARY_PATH33
```
## 更换源
### 替换brew.git
```bash
cd "$(brew --repo)"
git remote set-url origin https://mirrors.ustc.edu.cn/brew.git
```
### 替换homebrew-core.git
```bash
cd "$(brew --repo)/Library/Taps/homebrew/homebrew-core"
git remote set-url origin https://mirrors.ustc.edu.cn/homebrew-core.git
```
### 替换Homebrew Bottles源
```bash
echo 'export HOMEBREW_BOTTLE_DOMAIN=https://mirrors.ustc.edu.cn/homebrew-bottles' >> ~/.bash_profile
source ~/.bash_profile
```
## aliases
```bash
alias bi='brew install'
alias bu='brew update'
alias bs='brew search'
```
[**refence**](https://www.cnblogs.com/hongdada/p/9528560.html)  
## 注意
- 必须自己安装ruby, 否则会出现177line exec 错误
- 自己建立homebrew-core目录

