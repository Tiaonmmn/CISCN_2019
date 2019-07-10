# -*- coding:utf-8 -*-
import tornado.web
from sqlalchemy.orm.exc import NoResultFound
import urllib
import unicodedata
from sshop.base import BaseHandler
from sshop.models import Commodity, User, Shopcar, BanIP
from sshop.settings import limit
import traceback
import random
import sys
reload(sys)
sys.setdefaultencoding('utf8')

class ShopIndexHandler(BaseHandler):
    def get(self, *args, **kwargs):
        try:
            ip = self.orm.query(BanIP).filter(BanIP.ip == self.request.remote_ip).one()
            ip.count += 1
            self.orm.commit()
        except NoResultFound:
            self.orm.add(BanIP(ip=self.request.remote_ip, count=1))
            self.orm.commit()
        try:
            ip = self.orm.query(BanIP).filter(BanIP.ip == self.request.remote_ip).one()
            if ip.count >= 50000:
                return self.finish("Get out here.F**k you!")
        except:
            pass
        return self.redirect('/shop')


class ShopListHandler(BaseHandler):
    def get(self):
        try:
            ip = self.orm.query(BanIP).filter(BanIP.ip == self.request.remote_ip).one()
            ip.count += 1
            self.orm.commit()
        except NoResultFound:
            self.orm.add(BanIP(ip=self.request.remote_ip, count=1))
            self.orm.commit()
        try:
            ip = self.orm.query(BanIP).filter(BanIP.ip == self.request.remote_ip).one()
            if ip.count >= 50000:
                return self.finish("Get out here.F**k you!")
        except:
            pass

        page = self.get_argument('page', 1)
        page = int(page) if int(page) else 1
        commoditys = self.orm.query(Commodity) \
            .filter(Commodity.amount > 0) \
            .order_by(Commodity.price.desc()) \
            .limit(limit).offset((page - 1) * limit).all()
        return self.render('index.html', commoditys=commoditys, preview=page - 1, next=page + 1, limit=limit)


class ShopDetailHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self, id=1):
        try:
            commodity = self.orm.query(Commodity) \
                .filter(Commodity.id == int(id)).one()
        except NoResultFound:
            return self.redirect('/')
        return self.render('info.html', commodity=commodity)


class ShopPayHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        return self.finish("F**k you!")

    def post(self):
        try:
            price = self.get_argument('price')
            user = self.orm.query(User).filter(User.username == self.current_user).one()
            if user.integral < float(price):
                return self.render('pay.html', danger=1)
            user.integral = user.pay(float(price))
            self.orm.commit()
            shopcar = Shopcar()
            shopcar.name = self.orm.query(Commodity).filter(Commodity.price == price).one()
            shopcar.amount = self.orm.query(Shopcar).filter(Shopcar.name == shopcar.name.name).first()
            shopcar.amount.amount += 1
            self.orm.commit()
            if shopcar.name.name == 'flag':
                return self.render('pay.html', success=1, flag=True)
            else:
                return self.render('pay.html', success=1)
        except:
            traceback.print_exc()
            return self.render('pay.html', danger=1)


class ShopCarHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self, *args, **kwargs):
        return self.render('shopcar.html',danger=1,dangermessage="It's deprecated.No use.")

    @tornado.web.authenticated
    def post(self, *args, **kwargs):
        return self.render('shopcar.html',danger=1,dangermessage="It's deprecated.No use.")


class ShopCarAddHandler(BaseHandler):
    def post(self, *args, **kwargs):
        id = self.get_argument('id')
        self.set_secure_cookie('commodity_id', id)
        return self.redirect('/shopcar')


class ChargeHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self, *args, **kwargs):
        page = self.get_argument('page', 1)
        page = int(page) if int(page) else 1
        commoditys = self.orm.query(Commodity) \
            .filter(Commodity.amount > 0) \
            .order_by(Commodity.price.desc()) \
            .limit(limit).offset((page - 1) * limit).all()
        return self.render('charge.html', commoditys=commoditys, preview=page - 1, next=page + 1, limit=limit)

    def post(self, *args, **kwargs):
        page = self.get_argument('page', 1)
        page = int(page) if int(page) else 1
        commoditys = self.orm.query(Commodity) \
            .filter(Shopcar.amount > 0) \
            .order_by(Shopcar.id.desc()) \
            .limit(limit).offset((page - 1) * limit).all()
        id = self.get_argument('id')
        price = str(self.get_argument('price'))
        try:
            price = urllib.unquote(price).decode('utf-8')
        except UnicodeDecodeError:
            return self.render('charge.html', danger=1, commoditys=commoditys, preview=page - 1, next=page + 1,
                               limit=limit,
                               dangermessage="汝听，人言乎？")
        if len(price) > 1:
            return self.render('charge.html', danger=1, commoditys=commoditys, preview=page - 1, next=page + 1,
                               limit=limit, dangermessage="ATM机坏了，只能收一位数的钱。")
        try:
            unicodedata.numeric(price)
        except ValueError:
            return self.render('charge.html', danger=1, commoditys=commoditys, preview=page - 1, next=page + 1,
                               limit=limit,
                               dangermessage="汝听，人言乎？")

        # return self.render('charge.html', danger=1, commoditys=commoditys, preview=page - 1, next=page + 1,
        #                    limit=limit,
        #                    dangermessage="测试专用。当前输入字符为：{0}，其Unicode名称为：{1}，其Unicode numeric为：{2}".format(price,
        #                                                                                                  unicodedata.name(
        #                                                                                                      price),unicodedata.numeric(price)))
        try:
            commoditys = self.orm.query(Commodity).filter(Commodity.id == id).one()
        except NoResultFound:
            return self.render('charge.html', danger=1, commoditys=commoditys, preview=page - 1, next=page + 1,
                               limit=limit,
                               dangermessage="亲，这边建议您不要搞事情哦。ヽ(✿ﾟ▽ﾟ)ノ")
        if commoditys.name=='flag':
            if unicodedata.numeric(price)>=commoditys.price:
                return self.render('pay.html', success=1, flag=True)
            else:
                page = self.get_argument('page', 1)
                page = int(page) if int(page) else 1
                commoditys = self.orm.query(Commodity) \
                    .filter(Shopcar.amount > 0) \
                    .order_by(Shopcar.id.desc()) \
                    .limit(limit).offset((page - 1) * limit).all()
                return self.render('charge.html', danger=1, commoditys=commoditys, preview=page - 1, next=page + 1,
                                   limit=limit,
                                   dangermessage="充钱才能变得更强。")
        else:
            page = self.get_argument('page', 1)
            page = int(page) if int(page) else 1
            commoditys = self.orm.query(Commodity) \
                .filter(Shopcar.amount > 0) \
                .order_by(Shopcar.id.desc()) \
                .limit(limit).offset((page - 1) * limit).all()
            return self.render('charge.html', danger=1, commoditys=commoditys, preview=page - 1, next=page + 1,
                               limit=limit,
                               dangermessage="买错商品了，亲。")
