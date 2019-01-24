from flask_wtf import Form
from wtforms import TextField
from wtforms.validators import Required
from app import app

app.config['SECRET_KEY'] = 'hard to guess string'
class NameForm(Form):
    name = TextField('What is your name?',validators =[ Required() ])
