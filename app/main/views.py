from datetime import datetime
from .decorators import async
from flask import render_template, session, redirect, url_for, flash,request,copy_current_request_context,jsonify
from . import main
from flask_login import AnonymousUserMixin
from sqlalchemy import or_
#from .forms import
from .. import db
from ..models import User
from .dean import DEAN
from  .Pingjiao import Pingjiao
import time
import xlrd
import xlwt
import random
from flask_login import login_required,login_user,current_user,logout_user

@main.route('/')
def secret():
    return render_template('test.html')
@main.route('/login',methods=['GET','POST'])
def login():
    email=request.form.get("email", None)
    password=request.form.get("password", None)
    remember_me=request.form.get("remember_me", None)
    user = User.query.filter_by(email=email).first()
    if user is not None and user.verify_password(password):
        login_user(user, remember_me)
        return jsonify(result='success')
    else:
        return jsonify(result='fail')
@main.route('/islogin',methods=['GET','POST'])
def islogin():
    a=request.form.get("islogin",None)
    print(current_user)
    if current_user.is_anonymous is True:
        return jsonify(result='not')
    else:
        return jsonify(result=current_user.email)
@main.route('/logout',methods=['GET','POST'])
@login_required
def logout():
    logout_user()
    return jsonify(result='success')