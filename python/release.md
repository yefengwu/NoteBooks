---
title: Python自动发布markdown文章到WordPress网站
date: 2018-09-27 16:57
url: Python-auto-publish-markdown-post-to-WordPress
slug: test
tag: 
    - "wordpress"
    - "python"
category: 博客
status: publish
thumbnail: "./test.jpg"
---


# 安装：
```bash
pip install python-markdown
# 直接pip install frontmatter会报错
pip install python-frontmatter 
pip install python-wordpress-xmlrpc
```

# 带有自定义栏目字段的发布文章代码

```bash
#coding:utf-8
from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import GetPosts, NewPost
from wordpress_xmlrpc.methods.users import GetUserInfo
from wordpress_xmlrpc.methods import posts
from wordpress_xmlrpc.methods import taxonomies
from wordpress_xmlrpc import WordPressTerm
from wordpress_xmlrpc.compat import xmlrpc_client
from wordpress_xmlrpc.methods import media, posts
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

wp = Client('http://您的域名/xmlrpc.php', '后台账号', '后台密码')

post = WordPressPost()
post.title = '文章标题'
post.content = '文章内容'
post.post_status = 'publish' #文章状态，不写默认是草稿，private表示私密的，draft表示草稿，publish表示发布

post.terms_names = {
    'post_tag': ['test', 'firstpost'], #文章所属标签，没有则自动创建
    'category': ['Introductions', 'Tests'] #文章所属分类，没有则自动创建
 }

post.custom_fields = []   #自定义字段列表
post.custom_fields.append({  #添加一个自定义字段
        'key': 'price',
        'value': 3
})
post.custom_fields.append({ #添加第二个自定义字段
        'key': 'ok',
        'value': '天涯海角'
})
post.id = wp.call(posts.NewPost(post))</pre>
```

# 带有特色图像缩略图的发布文章

```bash
#coding:utf-8
from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import GetPosts, NewPost
from wordpress_xmlrpc.methods.users import GetUserInfo
from wordpress_xmlrpc.methods import posts
from wordpress_xmlrpc.methods import taxonomies
from wordpress_xmlrpc import WordPressTerm
from wordpress_xmlrpc.compat import xmlrpc_client
from wordpress_xmlrpc.methods import media, posts
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

wp = Client('http://您的域名/xmlrpc.php', '后台账号', '后台密码')

filename = './my.jpg' #上传的图片文件路径

# prepare metadata
data = {
        'name': 'picture.jpg',
        'type': 'image/jpeg',  # mimetype
}

# read the binary file and let the XMLRPC library encode it into base64
with open(filename, 'rb') as img:
        data['bits'] = xmlrpc_client.Binary(img.read())

response = wp.call(media.UploadFile(data))
# response == {
#       'id': 6,
#       'file': 'picture.jpg'
#       'url': 'http://www.example.com/wp-content/uploads/2012/04/16/picture.jpg',
#       'type': 'image/jpeg',
# }
attachment_id = response['id']

post = WordPressPost()
post.title = '文章标题'
post.content = '文章正文'
post.post_status = 'publish'  #文章状态，不写默认是草稿，private表示私密的，draft表示草稿，publish表示发布
post.terms_names = {
    'post_tag': ['test', 'firstpost'], #文章所属标签，没有则自动创建
    'category': ['Introductions', 'Tests'] #文章所属分类，没有则自动创建
 }
post.thumbnail = attachment_id #缩略图的id
post.id = wp.call(posts.NewPost(post))
```

# 除了可以发布文章，这个模块也可以单独创建新的分类和标签

```bash
#coding:utf-8
from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc import WordPressTerm
from wordpress_xmlrpc.methods import taxonomies

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

wp = Client('http://您的域名/xmlrpc.php', '后台账号', '后台密码')

#新建标签
tag = WordPressTerm()
tag.taxonomy = 'post_tag'
tag.name = 'My New Tag12'#标签名称
tag.slug = 'bieming12'#标签别名，可以忽略
tag.id = wp.call(taxonomies.NewTerm(tag))#返回的id

#新建分类
cat = WordPressTerm()
cat.taxonomy = 'category'
cat.name = 'cat1'#分类名称
cat.slug = 'bieming2'#分类别名，可以忽略
cat.id = wp.call(taxonomies.NewTerm(cat))#新建分类返回的id

#新建子分类
parent_cat = client.call(taxonomies.GetTerm('category', 20))#20是父分类的id

child_cat = WordPressTerm()
child_cat.taxonomy = 'category'
child_cat.parent = parent_cat.id
child_cat.name = 'My Child Category'#分类名称
child_cat.slug = 'beidongdui'#分类别名，可以忽略
child_cat.id = wp.call(taxonomies.NewTerm(child_cat))#新建分类返回的id
```
