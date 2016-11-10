from flask_mail import Message
from flask import render_template
import app
def send_email(to,subject,template,**kwargs):
    msg=Message('[图书借阅]'+subject,sender='图书借阅<17791652478@163.com>',recipients=[to])
    #msg.body=render_template(template+'.txt',**kwargs)
    msg.body=render_template(template+'.html',**kwargs)
    app.mail.send(msg)