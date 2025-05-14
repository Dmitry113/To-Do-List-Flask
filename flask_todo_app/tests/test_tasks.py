import pytest
from app.models.user import User
from app.models.task import Task
from app.models.category import Category


def test_task_creation(test_app, test_client, init_database):
    with test_app.app_context():
        user = User(username='testuser', email='test@example.com')
        user.set_password('password')
        db.session.add(user)
        db.session.commit()

        category = Category(name='Work', user_id=user.id)
        db.session.add(category)
        db.session.commit()

        task = Task(
            title='Test task',
            description='Test description',
            user_id=user.id,
            category_id=category.id
        )
        db.session.add(task)
        db.session.commit()

        assert task.title == 'Test task'
        assert task.category.name == 'Work'
        assert task.author == user