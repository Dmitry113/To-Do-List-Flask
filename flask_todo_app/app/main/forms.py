from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, SelectField, SubmitField, DateField
from wtforms.validators import DataRequired, Optional
from flask_login import current_user
from app.models.category import Category

class TaskForm(FlaskForm):
    title = StringField('Название', validators=[DataRequired()])
    description = TextAreaField('Описание')
    due_date = DateField('Срок выполнения', format='%Y-%m-%d', validators=[Optional()])
    is_urgent = BooleanField('Срочная задача')
    is_completed = BooleanField('Выполнено')
    category = SelectField('Категория', coerce=int)
    submit = SubmitField('Сохранить')

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.category.choices = [(0, 'Без категории')] + [
            (cat.id, cat.name) for cat in
            Category.query.filter_by(user_id=current_user.id).all()
        ]
