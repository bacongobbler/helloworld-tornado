import tornado.ioloop
import tornado.web
import os

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

application = tornado.web.Application([
    (r"/", MainHandler),
])

if __name__ == "__main__":
    port = os.environ['PORT'] if os.environ['PORT'] else 8888
    application.listen(port)
    tornado.ioloop.IOLoop.instance().start()
