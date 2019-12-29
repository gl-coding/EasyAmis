#encoding=utf8
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options

import json
import os

#just for ajax，实现跨域请求Server
class BaseHandler(tornado.web.RequestHandler):
    #blog.csdn.net/moshowgame 解决跨域问题
    def set_default_headers(self):
        print("setting headers!!!")
        #self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header('Access-Control-Allow-Origin', 'http:127.0.0.1:5501')
        #self.set_header('Access-Control-Allow-Origin', 'http:127.0.0.1:5500')
        self.set_header('Access-Control-Allow-Headers', '*')
        #self.set_header('Access-Control-Allow-Credentials', 'true')
        self.set_header('Access-Control-Max-Age', 1000)
        #self.set_header('Content-type', 'application/json')
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        self.set_header('Access-Control-Allow-Headers',#'*')
                        'authorization, Authorization, Content-Type, Access-Control-Allow-Origin, Access-Control-Allow-Headers, X-Requested-By, Access-Control-Allow-Methods')

    def post(self):
        self.write('some post')

    def get(self):
        self.write('some get')

    def options(self):
        # no body
        self.set_status(204)
        self.finish()

class PageHandler(BaseHandler):
    def get(self):
        self.render("500.html",msg="后台有错")

class GetHandler(BaseHandler):
    def get(self):
        res = self.get_argument("args")
        print res
        res_json = { "status": 0, "msg": "ok", "data": { "a": res } }
        res_json = json.dumps(res_json)
        print res_json
        self.write(res_json)

class PostHandler(BaseHandler):
    #process for post json
    def post(self):
        res = self.request.body
        print res
        res_json = { "status": 0, "msg": "ok", "data": { "a": res } }
        res_json = json.dumps(res_json)
        self.write(res_json)

def make_app():
    return tornado.web.Application([
        (r"/",     PostHandler),
        (r"/test", GetHandler),
        (r"/500",  PageHandler),
        ],
        template_path = os.path.join(
            os.path.dirname(__file__), "templates" # 索引到templates文件夹中的html
        ),
        debug = True
    )

if __name__ == "__main__":
    app = make_app()
    app.listen(8000)
    tornado.ioloop.IOLoop.instance().start()
