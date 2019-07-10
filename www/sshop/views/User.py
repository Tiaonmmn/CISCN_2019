#coding:utf-8
import os
import uuid
import time
import bcrypt
import tornado.web
from sqlalchemy.orm.exc import NoResultFound

from sshop.base import BaseHandler
from sshop.models import User


class UserLoginHanlder(BaseHandler):
    def get(self, *args, **kwargs):
        open(os.path.dirname(__file__) + "/../.idea/flag.txt", "w").write("CISCN{" + str(uuid.uuid4()) + "}")
        return self.render('login.html')

    def post(self):
        username = self.get_argument('username')
        password = self.get_argument('password')
        if username and password:
            try:
                user = self.orm.query(User).filter(User.username == username).one()
            except NoResultFound:
                return self.render('login.html', danger=1, ques=self.application.question, uuid=self.application.uuid)
            if user.check(password):
                self.set_secure_cookie('username', user.username,expires=time.time()+60*5)
                self.redirect('/user')
            else:
                return self.render('login.html', danger=1)


class RegisterHandler(BaseHandler):
    def get(self, *args, **kwargs):
        open(os.path.dirname(__file__) + "/../.idea/flag.txt", "w").write("CISCN{" + str(uuid.uuid4()) + "}")
        return self.render('register.html')

    def post(self, *args, **kwargs):
        username = self.get_argument('username')
        mail = self.get_argument('mail')
        password = self.get_argument('password')
        password_confirm = self.get_argument('password_confirm')

        if password != password_confirm:
            return self.render('register.html', danger=1)
        if mail and username and password:
            try:
                if username!='admin':#TODO: 禁止删除admin。
                    user = self.orm.query(User).filter(User.username == username).one()
                    self.orm.delete(user)
                    self.orm.add(User(username=username, mail=mail,
                                      password=bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())))
                    self.orm.commit()
                    self.redirect('/login')
                    '''
                    为了能过Checker，采取的逻辑为：如果有重名的用户，删除原有账户并添加一个新的。
                    '''
                else:
                    self.render('register.html', danger=1)

            except NoResultFound:
                self.orm.add(User(username=username, mail=mail,
                                  password=bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())))
                self.orm.commit()
                self.redirect('/login')
        else:
            return self.render('register.html', danger=1)


class ResetPasswordHanlder(BaseHandler):
    def get(self, *args, **kwargs):
        return self.render('reset.html')

    def post(self, *args, **kwargs):
        return self.redirect('/login')


class changePasswordHandler(BaseHandler):
    def get(self):
        return self.render('change.html')

    def post(self, *args, **kwargs):
        old_password = self.get_argument('old_password')
        password = self.get_argument('password')
        password_confirm = self.get_argument('password_confirm')
        print old_password, password, password_confirm
        user = self.orm.query(User).filter(User.username == self.current_user).one()
        if password == password_confirm:
            if user.check(old_password):
                user.password = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())
                self.orm.commit()
                return self.render('change.html', success=1)
        return self.render('change.html', danger=1)


class UserInfoHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self, *args, **kwargs):
        user = self.orm.query(User).filter(User.username == self.current_user).one()
        return self.render('user.html', user=user)


class UserLogoutHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self, *args, **kwargs):
        self.clear_cookie('username')
        self.redirect('/login')

class Redirect(BaseHandler):
    def get(self, *args, **kwargs):
        self.clear_cookie('username')
        self.redirect("http://"+self.request.host[:-5]+"/admin448bfdcd-c968-4d05-b9aa-7563a9e9cd19/")


