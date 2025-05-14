# 🚀 Flask To-Do List Application

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Flask](https://img.shields.io/badge/Flask-3.1.0-green)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0.40-red)

Полнофункциональное веб-приложение для управления задачами с аутентификацией пользователей, категориями задач и сроками выполнения.

## 📌 Содержание
- [Особенности](#-особенности)
- [Технологический стек](#-технологический-стек)
- [Установка](#-установка)
- [Структура проекта](#-структура-проекта)
- [Конфигурация](#-конфигурация)
- [Использование](#-использование)
- [Разработчикам](#-разработчикам)
- [Лицензия](#-лицензия)

## 🌟 Особенности

### Основной функционал
- 🔐 Система аутентификации (регистрация/вход/выход)
- 📝 CRUD операции с задачами
- 🗂 Категории задач
- ⏱ Сроки выполнения с валидацией
- ✅ Отметка о выполнении
- 🔍 Фильтрация и сортировка

### Дополнительно
- 📱 Адаптивный интерфейс (Bootstrap 5)
- 📊 Пагинация списка
- 🔄 Миграции базы данных
- 🧪 Тестовое покрытие

## 🛠 Технологический стек

### Основные компоненты
| Компонент | Версия | Назначение |
|-----------|--------|------------|
| Flask | 3.1.0 | Бэкенд-фреймворк |
| Flask-SQLAlchemy | 3.1.1 | ORM для работы с БД |
| Flask-Login | 0.6.3 | Аутентификация |
| Flask-WTF | 1.2.2 | Формы и валидация |
| SQLAlchemy | 2.0.40 | Ядро ORM |

### Зависимости
Полный список зависимостей смотрите в [requirements.txt](requirements.txt)

## ⚙️ Установка

### 1. Клонирование репозитория
```bash
git clone https://github.com/ваш-username/flask-todo-list.git
cd flask-todo-list

2. Настройка окружения

python -m venv .venv
# Для Windows:
.venv\Scripts\activate
# Для Linux/Mac:
source .venv/bin/activate

3. Установка зависимостей

pip install -r requirements.txt

4. Настройка базы данных

flask db init
flask db migrate -m "Initial migration"
flask db upgrade

5. Запуск приложения

flask run

📁 Структура проекта

flask_todo_app/
├── app/
│   ├── auth/               # Аутентификация
│   │   ├── forms.py        # Формы входа/регистрации
│   │   └── routes.py       # Маршруты аутентификации
│   ├── main/               # Основные функции
│   │   ├── forms.py        # Формы задач
│   │   └── routes.py       # Маршруты задач
│   ├── models/             # Модели данных
│   │   ├── user.py         # Модель пользователя
│   │   └── task.py         # Модель задачи
│   ├── templates/          # Шаблоны
│   ├── __init__.py         # Инициализация приложения
│   └── commands.py         # CLI команды
├── migrations/             # Миграции базы данных
├── tests/                  # Тесты
├── config.py               # Конфигурация
├── requirements.txt        # Зависимости
└── run.py                  # Точка входа

⚡ Быстрый старт

1. Создайте тестового пользователя:

flask create-test-user

2. Войдите в систему:

Логин: test@example.com

Пароль: test123

3. Начните добавлять задачи через веб-интерфейс

🛠 Конфигурация
Создайте файл .env в корне проекта:

SECRET_KEY=ваш_секретный_ключ
DATABASE_URL=sqlite:///todo.db
FLASK_ENV=development

Доступные параметры конфигурации:

SECRET_KEY - Обязательный секретный ключ

DATABASE_URL - Путь к БД (по умолчанию SQLite)

FLASK_ENV - Режим работы (development/production)

🧪 Тестирование

pytest tests/ -v

Покрытие тестами:

pytest --cov=app tests/

📦 Развертывание в продакшн
1. Использование Gunicorn

pip install gunicorn
gunicorn -w 4 -b :8000 'run:app'

2. Конфигурация Nginx
Пример конфига для Ubuntu:

server {
    listen 80;
    server_name yourdomain.com;

    location / {
        proxy_pass http://localhost:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
Планируемые улучшения
REST API для мобильных приложений

Уведомления по email

Прикрепление файлов к задачам

Экспорт в PDF/Excel