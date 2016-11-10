#!/usr/bin/python3 python3
import os
import json
from gevent import monkey
from app import create_app,db
from app.models import User,Book,Comment
from flask_script import Manager,Shell
from flask_migrate import Migrate,MigrateCommand
monkey.patch_all()
app=create_app('default')
app.secret_key='abcdefghijklmn'
manager=Manager(app)
migrate=Migrate(app,db)
def make_shell_context():
    return dict(app=app,db=db,User=User,Book=Book,Comment=Comment)
manager.add_command("shell",Shell(make_context=make_shell_context))
manager.add_command('db',MigrateCommand)
if __name__=='__main__':
    #app.run(debug=True)
    manager.run()