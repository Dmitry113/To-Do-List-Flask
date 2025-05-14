from app import create_app, db
from app.models.user import User
from app.models.task import Task
from app.models.category import Category

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {
        'db': db,
        'User': User,
        'Task': Task,
        'Category': Category
    }


if __name__ == '__main__':
    app.run(debug=True)