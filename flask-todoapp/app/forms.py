from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from app.models import ToDoItem

class ItemForm(FlaskForm):
    item = StringField('Item', validators=[DataRequired()])
    completed = BooleanField('Completed')
    submit = SubmitField('Register')
