import random
import string
import os
import shutil
import bcrypt
from sqlalchemy import Column
from sqlalchemy import create_engine,ForeignKey
from sqlalchemy.dialects.sqlite import FLOAT, VARCHAR, INTEGER,BLOB
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

from settings import connect_str

BaseModel = declarative_base()
engine = create_engine(connect_str, echo=True, pool_recycle=3600)
db = scoped_session(sessionmaker(bind=engine,autocommit=False,autoflush=True))
import random

class Commodity(BaseModel):
    __tablename__ = 'commoditys'

    id = Column(INTEGER, primary_key=True, autoincrement=True)
    name = Column(VARCHAR(200), unique=True, nullable=False)
    desc = Column(VARCHAR(500), default='no description')
    amount = Column(INTEGER, default=10)
    price = Column(FLOAT, nullable=False)
    picture=Column(BLOB,default=None)

    def __repr__(self):
        return '<Commodity: %s>' % self.name

    def __price__(self):
        return self.price


class User(BaseModel):
    __tablename__ = 'user'

    id = Column(INTEGER, primary_key=True, autoincrement=True)
    username = Column(VARCHAR(50))
    mail = Column(VARCHAR(50))
    password = Column(VARCHAR(60))
    integral = Column(FLOAT, default=2333)

    def check(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf8'))

    def __repr__(self):
        return '<User: %s>' % self.username

    def pay(self, num):
        res = (self.integral - num) if (self.integral - num) else False
        if res >= 0:
            return res
        else:
            return False

    def __integral__(self):
        return self.integral


class Shopcar(BaseModel):
    __tablename__ = 'shopcar'

    id = Column(INTEGER, primary_key=True, autoincrement=True)
    name = Column(VARCHAR(200),ForeignKey('commoditys.name'), unique=True, nullable=False)
    desc = Column(VARCHAR(500),ForeignKey('commoditys.desc'), default='no description')
    amount = Column(INTEGER, default=0)

class BanIP(BaseModel):
    __tablename__= 'banip'
    id = Column(INTEGER, primary_key=True, autoincrement=True)
    ip=Column(VARCHAR(500))
    count=Column(INTEGER,default=0)

if __name__ == "__main__":
    if os.access('sshop.db3',os.R_OK|os.F_OK):
        os.remove('sshop.db3')
    BaseModel.metadata.create_all(engine)
    for i in xrange(5):
        name = ''.join(random.sample(string.ascii_letters, 16))
        desc = ''.join(random.sample(string.ascii_letters * 5, 100))
        price = random.randint(10, 200)
        db.add(Commodity(name=name, desc=desc, price=price))
        db.add(Shopcar(name=name,desc=desc,amount=0))

    db.add(Commodity(name="flag", desc="Strings you know", price=10000))
    db.add(Shopcar(name="flag",desc="Strings you know", amount=0))
    db.add(Commodity(name="sample", desc="sample item", price=201))
    db.add(Shopcar(name="sample", desc="sample item", amount=0))
    db.add(User(id=random.randint(1000,999999), username="admin", mail="admin@ciscn.cn",
                password=bcrypt.hashpw("password".encode('utf8'), bcrypt.gensalt()),
                integral=1000))
    db.commit()
