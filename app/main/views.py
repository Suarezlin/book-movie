from datetime import datetime
from .decorators import async
from flask import render_template, session, redirect, url_for, flash,request,copy_current_request_context
from . import main
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
from flask_login import login_required

@main.route('/secret')
@login_required
def secret():
    return '只有登录才能查看的页面'