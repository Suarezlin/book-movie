from flask_sqlalchemy import SQLAlchemy
from flask import current_app
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import db,login_manager
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model,UserMixin):
    __tablename__='user'
    id=db.Column(db.Integer,primary_key=True)
    netid=db.Column(db.String(10),index=True)
    name=db.Column(db.String(32),nullable=False,index=True)
    email=db.Column(db.String(64),nullable=False,unique=True,index=True)
    password_hash=db.Column(db.String(128))
    book=db.relationship('Book',backref='people')
    comment = db.relationship('Comment', backref='people')
    comfirmed=db.Column(db.Boolean,default=False)
    def __repr__(self):
        return '%s %s' %(self.name,self.netid)
    def generate_confirmation_token(self,expiration=3600):
        s=Serializer(current_app.config['SECRET_KEY'],expiration)
        return s.dumps({'confirm':self.id})
    def confirm(self,token):
        s=Serializer(current_app.config['SECRET_KEY'])
        try:
            data=s.loads(token)
        except:
            return False
        if data.get('confirm')!=self.id:
            return False
        self.comfirmed=True
        db.session.add(self)
        return True
    def set_password(self,password):
        self.password_hash=generate_password_hash(password)
    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)
class Book(db.Model):
    __tablename__='book'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String,index=True)
    book_id=db.Column(db.String,index=True,unique=True)
    people_id=db.Column(db.String,db.ForeignKey('user.netid'))
    comment=db.relationship('Comment',backref='book')
    def __repr__(self):
        return '书名: %s 借阅人: %s' %(self.name,self.people_id)
class Comment(db.Model):
    __tablename__='comment'
    id=db.Column(db.Integer,primary_key=True)
    book_id=db.Column(db.String,db.ForeignKey('book.book_id'))
    people_id=db.Column(db.String,db.ForeignKey('user.netid'))
    comment=db.Column(db.String)
    def __repr__(self):
        return '%s %s %s' %(self.book_id,self.people_id,self.comment)
