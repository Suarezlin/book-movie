from flask import render_template, redirect, url_for, request,flash
from . import auth
from .forms import LoginForm, SignForm
from ..models import User, db
from ..email import send_email
from flask_login import current_user, login_required, login_user


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user != None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return render_template('auth/ls.html')
        flash('邮箱或密码错误')
    return render_template('auth/login.html', form=form)

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignForm()
    if form.validate_on_submit():
        user = User(email=form.email.data, netid=form.netid.data, name=form.name.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        token = user.generate_confirmation_token()
        send_email(user.email, '确认账户', 'auth/confirm', user=user, token=token)
        return render_template('auth/com_sign.html')
    return render_template('auth/dean.html', form=form)


@auth.route('/confirm/<token>')
@login_required
def confirm(token):
    if current_user.confirmed:
        return redirect(url_for('auth.login'))
    if current_user.confirm(token):
        return redirect(url_for('auth.login'))
    return redirect(url_for('auth.signup'))




@auth.route('/unconfirmed')
def unconfirmed():
    if current_user.is_anonymous() or current_user.confirmed:
        return redirect(url_for('auth/ls.html'))
    return render_template('auth/unconfirmed.html')


@auth.route('/confirm')
def resend():
    token = current_user.generate_confirmation_token()
    send_email(current_user.email, '确认账户', 'auth/confirm', user=current_user, token=token)
    return redirect(url_for('auth.login'))
