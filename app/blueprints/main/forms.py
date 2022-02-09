from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired 
from flask_wtf import FlaskForm

class SearchForm(FlaskForm):
    poke_name = StringField('Type in the name of the Pokemon:', validators=[DataRequired()])
    submit = SubmitField('Submit')


    

