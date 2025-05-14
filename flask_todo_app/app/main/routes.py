from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app import db
from app.models.task import Task
from app.models.category import Category
from app.main.forms import TaskForm
from app.main import main_bp  # Используем main_bp вместо bp


@main_bp.route('/')  # Исправлено с @bp.route на @main_bp.route
@login_required
def index():
    page = request.args.get('page', 1, type=int)
    category_id = request.args.get('category_id', type=int)
    show_completed = request.args.get('show_completed', False, type=bool)
    sort_by = request.args.get('sort_by', 'created_at')
    order = request.args.get('order', 'desc')

    query = Task.query.filter_by(user_id=current_user.id)

    if category_id:
        query = query.filter_by(category_id=category_id)

    if not show_completed:
        query = query.filter_by(is_completed=False)

    if order == 'desc':
        query = query.order_by(getattr(Task, sort_by).desc())
    else:
        query = query.order_by(getattr(Task, sort_by))

    tasks = query.paginate(page=page, per_page=10)
    categories = Category.query.filter_by(user_id=current_user.id).all()

    return render_template('main/index.html',
                         tasks=tasks,
                         categories=categories,
                         current_category=category_id,
                         show_completed=show_completed,
                         sort_by=sort_by,
                         order=order)


@main_bp.route('/add', methods=['GET', 'POST'])
@login_required
def add_task():
    form = TaskForm()
    if form.validate_on_submit():
        task = Task(
            title=form.title.data,
            description=form.description.data,
            is_completed=form.is_completed.data,
            user_id=current_user.id,
            category_id=form.category.data if form.category.data != 0 else None
        )
        db.session.add(task)
        db.session.commit()
        flash('Задача успешно добавлена', 'success')
        return redirect(url_for('main.index'))
    return render_template('main/add_task.html', form=form)


@main_bp.route('/edit/<int:task_id>', methods=['GET', 'POST'])
@login_required
def edit_task(task_id):
    task = Task.query.filter_by(id=task_id, user_id=current_user.id).first_or_404()
    form = TaskForm(obj=task)
    if form.validate_on_submit():
        task.title = form.title.data
        task.description = form.description.data
        task.is_completed = form.is_completed.data
        task.category_id = form.category.data if form.category.data != 0 else None
        db.session.commit()
        flash('Задача успешно обновлена', 'success')
        return redirect(url_for('main.index'))
    return render_template('main/edit_task.html', form=form, task_id=task_id)


@main_bp.route('/delete/<int:task_id>')
@login_required
def delete_task(task_id):
    task = Task.query.filter_by(id=task_id, user_id=current_user.id).first_or_404()
    db.session.delete(task)
    db.session.commit()
    flash('Задача успешно удалена', 'success')
    return redirect(url_for('main.index'))


@main_bp.route('/complete/<int:task_id>')
@login_required
def complete_task(task_id):
    task = Task.query.filter_by(id=task_id, user_id=current_user.id).first_or_404()
    task.is_completed = not task.is_completed
    db.session.commit()
    flash('Статус задачи изменен', 'success')
    return redirect(url_for('main.index'))