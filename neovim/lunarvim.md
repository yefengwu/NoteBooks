---
title: "lunarvim shortkeys"
slug: test
tag: 
    - "wordpress"
    - "python"
category: 博客
status: publish
thumbnail: "./test.jpg"
---
| 命令                       | 描述                    |
|----------------------------|-------------------------|
| `:enew\|pu=execute('map')` | 将map的信息显示到buffer |

---
## 插件
---
### 文件目录[nvim-tree](https://github.com/kyazdani42/nvim-tree.lua)
---
| key       | actions                                                                                        |
|:-----------|:------------------------------------------------------------------------------------------------|
| <CR\> or o | on the root folder will cd in the above directory                                              |
| <c-]\>     | will cd in the directory under the cursor                                                      |
| <BS\>      | will close current opened directory or parent                                                  |
| r         | to rename a file
| <C-r\>     | to rename a file and omit the filename on input
| x         | to add/remove file/directory to cut clipboard
| c         | to add/remove file/directory to copy clipboard
| y         | will copy name to system clipboard
| Y         | will copy relative path to system clipboard
| gy        | will copy absolute path to system clipboard
| p         | to paste from clipboard. Cut clipboard has precedence over copy (will prompt for confirmation)
| d         | to delete a file (will prompt for confirmation)
| D         | to trash a file (configured in setup())
| ]c        | to go to next git item
| [c        | to go to prev git item
| -         | to navigate up to the parent directory of the current file/directory
| <C-v\>     | open the file in a vertical split
| <C-x\>     | open the file in a horizontal split
| <C-t\>     | open the file in a new tab
| <Tab\>     | open the file as a preview (keeps the cursor in the tree)
| I         | toggle visibility of hidden folders / files
| H         | toggle visibility of dotfiles (files/folders starting with a .)
| R         | refresh the tree
| W         | will collapse the whole tree
| S         | will prompt the user to enter a path and then expands the tree to match the path
| .         | will enter vim command mode with the file the cursor is on
| C-k       | will toggle a popup with file infos about the file under the cursor

Double left click acts like <CR>
Double right click acts like <C-]>

type **s**  to open a file with default system application or a folder with default file manager (if you want to change the command used to do it see :h nvim-tree.setup under system_open)

if the file is a directory, <CR> will open the directory otherwise it will open the file in the buffer near the tree
if the file is a symlink, <CR> will follow the symlink (if the target is a file)

type **a** to add a file. Adding a directory requires leaving a leading / at the end of the path.
you can add multiple directories by doing foo/bar/baz/f and it will add foo bar and baz directories and f as a file
