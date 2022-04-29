## Install
```bash
cd /usr/local/bin
sudo wget -q --show-pregress https://github.com/neovim/neovim/releases/latest/download/nvim.appimage 
sudo chmod +x ./nvim.appimage
sudo ./nvim.appimage --appimage-extract
sudo ln -s /usr/local/bin/squashfs-root/usr/bin/nvim /usr/local/bin/nvim
cd
```
## some plugins
### Tabular
`:Tabularize 可简化为 :Tab，以下都省略了选中区域后自动生成的 '<,'>：` 
```bash
冒号对齐：:Tab /:
逗号对齐 :Tabularize /,
运行上一个对齐命令 :Tab
// 对齐（需要 escape）: :Tab /\/\/
:Tabularize /,/r1c1l0 含义是：对齐指定区域的文本，以逗号分割。将第一个逗号前的所有文本右对齐，然后添加一个空格；将逗号居中对齐，然后添加一个空格；然后将逗号后所有文本左对齐，不添加空格（添加 0 个空格）。
```
### dein.vim
```bash
curl -fsSL https://raw.githubusercontent.com/Shougo/dein.vim/master/bin/installer.sh | bash -s ~/.cache/dein
```
### 复制到windows剪切板
```bash
func! GetSelectedText()
    normal gv"xy
    let result = getreg("x")
    return result
endfunc
if !has("clipboard") && executable("clip.exe")
    noremap <C-C> :call system('clip.exe', GetSelectedText())<CR>
    noremap <C-X> :call system('clip.exe', GetSelectedText())<CR>gvx
endif
```
