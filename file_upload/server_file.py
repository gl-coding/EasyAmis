#!/usr/bin/env python
#coding:utf-8

import tornado.ioloop
import tornado.web                                              #导入tornado模块下的web文件

import json
import os

class uploadPage(tornado.web.RequestHandler):
    def get(self):
        self.render("templete_action_file.html")

class uploadReciever(tornado.web.RequestHandler):
    def post(self):
        #print self.request.files
        file_metas = self.request.files["file"]                 #获取上传文件信息
        for meta in file_metas:                                 #循环文件信息
            file_name = meta['filename']                        #获取文件的名称
            print file_name
            with open(os.path.join('statics', 'img', file_name), 'wb') as up:            #os拼接文件保存路径，以字节码模式打开
                up.write(meta['body'])                                                  #将文件写入到保存路径目录

        res_json = { "status": 0, "msg": "ok", "data": { "a": 1 } }
        res_json = json.dumps(res_json)
        self.write(res_json)

settings = {                                            #html文件归类配置，设置一个字典
    "template_path": "views",                           #键为template_path固定的，值为要存放HTML的文件夹名称
    "static_path":   "statics",                         #键为static_path固定的，值为要存放js和css的文件夹名称
}

#路由映射
application = tornado.web.Application(
    [                                                   #创建一个变量等于tornado.web下的Application方法
    (r"/upload",   uploadPage),
    (r"/reciever", uploadReciever),
    ],
    **settings)                                          #将html文件归类配置字典，写在路由映射的第二个参数里

if __name__ == "__main__":
    #内部socket运行起来
    application.listen(8888)                            #设置端口
    tornado.ioloop.IOLoop.instance().start()
