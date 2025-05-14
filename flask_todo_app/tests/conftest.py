import pytest
from app import create_app, db
from app.models.user import User
from app.models.task import Task
from app.models.category import Category
from config import TestConfig


@pytest.fixture(scope='module')
def test_app():
    app = create_app(TestConfig)
    with app.app_context():
        yield app


@pytest.fixture(scope='module')
def test_client(test_app):
    return test_app.test_client()


@pytest.fixture(scope='module')
def init_database(test_app):
    db.create_all()

    # Тестовый пользователь
    user = User(username='testuser', email='test@example.com')
    user.set_password('password')
    db.session.add(user)

    # Тестовая категория
    category = Category(name='Test Category', user_id=1)
    db.session.add(category)

    # Тестовая задача
    task = Task(title='Test Task', user_id=1, category_id=1)
    db.session.add(task)

    db.session.commit()

    yield db

    db.drop_all()