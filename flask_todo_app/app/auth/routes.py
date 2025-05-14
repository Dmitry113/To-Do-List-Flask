from flask import render_template, redirect, url_for, flash, current_app
from flask_login import login_user, logout_user, current_user
import os
from app.auth.forms import LoginForm, RegistrationForm
from app.models.user import User
from app import db

# Сначала создаем blueprint
bp = None  # Инициализация переменной


def init_auth_routes(auth_bp):
    global bp
    bp = auth_bp

    @bp.route('/register', methods=['GET', 'POST'])
    def register():
        if current_user.is_authenticated:
            return redirect(url_for('main.index'))

        form = RegistrationForm()
        if form.validate_on_submit():
            user = User(username=form.username.data, email=form.email.data)
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()
            flash('Регистрация прошла успешно!', 'success')
            return redirect(url_for('auth.login'))

        return render_template('auth/register.html', title='Регистрация', form=form)

    @bp.route('/login', methods=['GET', 'POST'])
    def login():
        if current_user.is_authenticated:
            return redirect(url_for('main.index'))

        form = LoginForm()
        if form.validate_on_submit():
            user = User.query.filter_by(email=form.email.data).first()
            if user is None or not user.check_password(form.password.data):
                flash('Неверный email или пароль', 'danger')
                return redirect(url_for('auth.login'))
            login_user(user, remember=form.remember.data)
            return redirect(url_for('main.index'))

        # Отладочная проверка пути
        template_path = os.path.join(current_app.root_path, current_app.template_folder, 'auth/login.html')
        if not os.path.exists(template_path):
            raise RuntimeError(f"Template not found at: {template_path}")

        return render_template('auth/login.html', title='Вход', form=form)

    @bp.route('/logout')
    def logout():
        logout_user()
        return redirect(url_for('main.index'))