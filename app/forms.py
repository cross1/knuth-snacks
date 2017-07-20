from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired

CHOICES=[('In Fridge', 'In Fridge'),
         ('Under Microwave', 'Under Microwave'),
         ('Above Microwave', 'Above Microwave'),
	 ('On Table', 'On Table'),
	 ('In Freezer', 'In Freezer'),
         ('Other', 'Other')]

class AddSnackForm(FlaskForm):
    question = StringField('''Please enter snack requests here. They will be added
     to the shopping list.''', [DataRequired()])

class AddALocation(FlaskForm):
    location = SelectField(u'Select a Location', choices=CHOICES)
