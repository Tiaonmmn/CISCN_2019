# coding=utf-8

from sshop.base import BaseHandler


class NotFoundHandler(BaseHandler):
    def get(self, *args, **kwargs):
        print(self.request.uri)
        return self.render('../fakers/' + self.request.uri[1:])

    def post(self):
        pass
