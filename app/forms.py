from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired

CHOICES=[('infridge', 'In Fridge'),
         ('undermircowave', 'Under Microwave'),
         ('abovemicrowave', 'Above Microwave'),
         ('other', 'Other')]

class AddSnackForm(FlaskForm):
    question = StringField('''Please enter snack requests here. They will be added
     to the shopping list.''', [DataRequired()])

class AddALocation(FlaskForm):
    location = SelectField(u'Select a Location', choices=CHOICES)
