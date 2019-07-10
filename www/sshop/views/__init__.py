from tornado.web import *

from CommonFile import *
from NotFound import *
from Shop import *
from User import *

root_path = os.path.dirname(__file__)
handlers = [

    (r'/', ShopIndexHandler),
    (r'/shop', ShopListHandler),
    (r'/info/(\d+)', ShopDetailHandler),
    (r'/pay', ShopPayHandler),
    (r'/user', UserInfoHandler),
    (r'/user/change', changePasswordHandler),
    (r'/pass/reset', ResetPasswordHanlder),
    (r'/charge',ChargeHandler),
    (r'/login', UserLoginHanlder),
    (r'/logout', UserLogoutHandler),
    (r'/register', RegisterHandler),
    (r"/.idea/(.*)", StaticFileHandler, {"path": os.path.join(root_path, '../.idea')}),
    (r"/index.php", CommonFileHandler),
    (r'/flag(.*)',CommonFileHandler),
    (r"/index", CommonFileHandler),
    (r"(?i)/account", CommonFileHandler),
    (r"(?i)/debug", CommonFileHandler),
    (r"(?i)/admin", CommonFileHandler),
    (r"(?i)/houtai", CommonFileHandler),
    (r"(?i)/include", CommonFileHandler),
    (r"(?i)/private", CommonFileHandler),
    (r"(?i)/super", CommonFileHandler),
    (r"/admin448bfdcd-c968-4d05-b9aa-7563a9e9cd19/(.*)",Redirect),
    (r".*", ShopIndexHandler)
]
