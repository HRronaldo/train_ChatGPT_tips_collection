from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from english_trainner_with_chatgpt.models import User

auth = Blueprint('auth', __name__)


# 注册视图函数
@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # 从表单中获取用户名和密码
        username = request.form['username']
        password = request.form['password']

        # 对密码进行哈希并创建用户对象
        user = User(username=username, password=generate_password_hash(password))

        # 保存用户对象到数据库
        user.save()

        # 显示注册成功的消息并重定向到登录页面
        flash('You have successfully registered! Please login.')
        return redirect(url_for('auth.login'))

    # 显示注册页面
    return render_template('register.html')


# 登录视图函数
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # 从表单中获取用户名和密码
        username = request.form['username']
        password = request.form['password']

        # 根据用户名在数据库中查找用户
        user = User.query.filter_by(username=username).first()

        # 如果找到了用户，就验证密码并设置 session
        if user and check_password_hash(user.password, password):
            session.clear()
            session['user_id'] = user.id
            session['username'] = user.username

            # 显示登录成功的消息并重定向到主页
            flash('You have successfully logged in.')
            return redirect(url_for('index'))

        # 如果用户名或密码无效，则显示错误消息
        flash('Invalid username or password.')

    # 显示登录页面
    return render_template('login.html')


# 注销视图函数
@auth.route('/logout')
def logout():
    session.clear()
    flash('You have successfully logged out.')
    return redirect(url_for('auth.login'))
