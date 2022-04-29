#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import frontmatter
import markdown
from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods import posts, media
from wordpress_xmlrpc.compat import xmlrpc_client
from wordpress_xmlrpc.methods.posts import GetPosts,NewPost

import json 

# 读取data.json，获取用户名和密码
def GetUserInfo():
    try:
        f = open("data.json", 'r')
        data = json.load(f)
        print(data)
        username = data["username"]
        passwd = data["passwd"]
    except FileNotFoundError:
        print("config File is not found")
        username = input("please input your username: ")
        passwd = input("please input your passwd: ")
    except PermissionError:
        print("You don't have permission to access this file")
    return username,passwd
    

if __name__ == "__main__":
    username,passwd = GetUserInfo()
    dir_md = sys.argv[1]
    postinfo = frontmatter.load(dir_md)
    post = WordPressPost()
    post.title = postinfo.metadata['title']
    post.slug = postinfo.metadata['slug']
    # 将markdown文章转换为html
    post_content_html = markdown.markdown(postinfo.content, extensions=['markdown.extensions.fenced_code', 'markdown.extensions.tables'])
    post_content_html = post_content_html.encode("utf-8") #转换编码格式，修正中文乱码
    post.content = post_content_html
    post.terms_names = {
      'post_tag': postinfo.metadata['tag'],
      'category': postinfo.metadata['category']
    }
    print(post.terms_names)
    # post.post_status有publish发布、draft草稿、private隐私状态可选，默认草稿。如果是publish会直接发布
    post.post_status = postinfo.metadata['status']
    # 推送文章到WordPress网站
    try:        # 登录WordPress后台
        client = Client('https://yefengx.top/xmlrpc.php',username,passwd)
    except ServerConnectionError:
        print('登录失败')
    else:
        print('登录成功')
        post_list = client.call(posts.GetPosts()) #所有的xml-rpc方法都是要通过call方法调用才能执行
        for p in post_list:
            if p.title == post.title:
                print("更新文章: "+ p.title)
                client.call(posts.EditPost(p.id, post))
                sys.exit()
        # 添加特色图片
        # read the binary file and let the XMLRPC library encode it into base64
        imgfile = postinfo.metadata['thumbnail']
        data = {
            'name': imgfile,
            'type': 'image/jpeg',  # mimetype
        }
        with open(imgfile, 'rb') as img:
                data['bits'] = xmlrpc_client.Binary(img.read())
        response = client.call(media.UploadFile(data))
        attachment_id = response['id']
        post.thumbnail = attachment_id
        print("发布新文章: " + post.title)
        client.call(NewPost(post))
