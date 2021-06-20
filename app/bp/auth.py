from flask import render_template, request, redirect, url_for, flash, get_flashed_messages
from flask_login import login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from . import bp
from ..db import save_user, get_user


"""Authen & Author"""


@bp.route('/login')
def login():
    return render_template('login.html')


@bp.route('/login', methods=['POST'])
def login_post():
    email = request.form.get("email")
    password = request.form.get("password")
    remember = True if request.form.get("remember") else False

    if len(email) == 0 or len(password) == 0:
        flash('email hoặc pass không được để trống')

    user = get_user(email)

    if not user:
        flash("Email không tồn tại !")
        return redirect(url_for('bp.login'))
    if not check_password_hash(user.password, password):
        flash("Sai mật khẩu !")
        return redirect(url_for('bp.login'))

    login_user(user, remember)

    return redirect(url_for('bp.profile'))


@bp.route('/signup')
def signup():
    return render_template('signup.html')


@bp.route('/signup', methods=['POST'])
def signup_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    user = get_user(email)     # check user

    if user:
        flash('Email đã tồn tại !')
        return redirect(url_for('bp.signup'))

    new_user = {'email':email, 'name':name, 'password':generate_password_hash(password, method='sha256')}

    save_user(new_user)

    return redirect(url_for('bp.login'))


@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return render_template('home.html')