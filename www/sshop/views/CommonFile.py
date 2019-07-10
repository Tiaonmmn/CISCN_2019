# coding=utf-8
import uuid
from sshop.base import BaseHandler
from sshop.models import BanIP
from sqlalchemy.orm.exc import NoResultFound
class CommonFileHandler(BaseHandler):
    def get(self, *args, **kwargs):
        try:
            ip = self.orm.query(BanIP).filter(BanIP.ip == self.request.remote_ip).one()
            ip.count+=1
            self.orm.commit()
        except NoResultFound:
            self.orm.add(BanIP(ip=self.request.remote_ip,count=1))
            self.orm.commit()
        try:
            if "flag" in self.request.uri:
                return self.finish("flag{"+str(uuid.uuid4())+"}")
            ip = self.orm.query(BanIP).filter(BanIP.ip == self.request.remote_ip).one()
            return self.render('../fakers/' + self.request.uri[1:])
        except IOError:
            return self.redirect('/shop')


    def post(self):
        print(self.request.uri)
        try:
            return self.render('../fakers/' + self.request.uri[1:])
        except IOError:
            return self.redirect('/shop')
    def head(self, *args, **kwargs):
        print(self.request.uri)
        try:
            return self.render('../fakers/' + self.request.uri[1:])
        except IOError:
            return self.redirect('/shop')
    def put(self, *args, **kwargs):
        pass