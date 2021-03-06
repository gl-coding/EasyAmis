#encoding=utf8
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

import json
import os

class GetHandler(tornado.web.RequestHandler):
    def get(self):
        res = self.get_argument("args")
        print res
        res_json = { "status": 0, "msg": "ok", "data": { "a": res } }
        res_json = json.dumps(res_json)
        print res_json
        self.write(res_json)

class PostHandler(tornado.web.RequestHandler):
    #process for post json
    def post(self):
        res = self.request.body
        print res
        res_json = { "status": 0, "msg": "ok", "data": { "a": res } }
        res_json = json.dumps(res_json)
        self.write(res_json)

class ErrorHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("template_500.html", msg="后台有错")

class InitApiHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("templete_action_page.html")

class FormHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("templete_action_form.html")

class FormProcesser(tornado.web.RequestHandler):
    def post(self):
        res = self.request.body
        print res
        res_json = { "status": 0, "msg": "ok", "data": { "a": res } }
        res_json = json.dumps(res_json)
        self.write(res_json)

class FileUploadHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("templete_action_file.html")

class FileUploadProcesser(tornado.web.RequestHandler):
    def get(self):
        self.render("templete_action_form.html")

class TableProcesser(tornado.web.RequestHandler):
    def get(self):
        self.render("templete_action_table.html")

class TableApiProcesser(tornado.web.RequestHandler):
    def get(self):
        res = self.get_argument("args")
        print res
        res_json = { "status": 0, "msg": "ok", "data": { "rows": [{"engine":"1", "version":"2"}] } }
        res_json = json.dumps(res_json)
        print res_json
        self.write(res_json)

class AudioProcesser(tornado.web.RequestHandler):
    def get(self):
        self.render("templete_action_audio.html")

class AudioApiProcesser(tornado.web.RequestHandler):
    def get(self):
        res = self.get_argument("args")
        print res
        res_json = { "status": 0, "msg": "ok", "data": [{"engine":"1", "audio":"https://amis.bj.bcebos.com/amis/2019-7/1562137295708/chicane-poppiholla-original-radio-edit%20(1).mp3"}] }
        res_json = json.dumps(res_json)
        print res_json
        self.write(res_json)

def make_app():
    return tornado.web.Application([
        (r"/get",      GetHandler),
        (r"/post",     PostHandler),
        (r"/500",      ErrorHandler),
        (r"/initApi",  InitApiHandler),
        (r"/form",     FormHandler),
        (r"/form_pro", FormProcesser),
        (r"/file",     FileUploadHandler),
        (r"/file_pro", FileUploadProcesser),
        (r"/table",    TableProcesser),
        (r"/table_api",TableApiProcesser),
        (r"/audio",    AudioProcesser),
        (r"/audio_api",AudioApiProcesser),
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
