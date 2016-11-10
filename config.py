import os
basedir=os.path.abspath(os.path.dirname(__file__))
class Config:
    SECRET_KEY = 'hardcto guess string'
    SQLALCHEMY_DATABASE_URI= 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    MAIL_SERVER='smtp.163.com'
    MAIL_PORT=465
    MAIL_USE_TLS=True
    MAIL_USERNAME='17791652478@163.com'
    MAIL_PASSWORD='Lzn19971012'
    @staticmethod
    def init_app(app):
        pass

config={'default':Config}