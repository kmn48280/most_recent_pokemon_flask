from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, RadioField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from app.models import User
from jinja2 import Markup

class LoginForm(FlaskForm):
    email = StringField('Email Address', validators =[DataRequired(), Email()])
    password = PasswordField('Password', validators =[DataRequired()])
    submit = SubmitField('Login')

class RegisterForm(FlaskForm):
    first_name = StringField("First Name", validators=[DataRequired()])
    last_name = StringField("Last Name", validators=[DataRequired()])
    email = StringField("Email Address", validators = [DataRequired(), Email()])
    password = PasswordField("Password", validators= [DataRequired()])
    confirm_password = PasswordField("Confirm Password", validators= [DataRequired(), 
        EqualTo("password", message="Passwords MUST match")])
    favorite = StringField("What's your favorite Pokemon?", default=None)
    submit = SubmitField("Register")

    #AVATARS:
    a1_img=Markup('<img src="/static/images/svg/bulbasaur.svg" style="height:75px">')
    a2_img=Markup('<img src="/static/images/svg/chikorita.svg" style="height:75px">')
    a3_img=Markup('<img src="/static/images/svg/eevee.svg" style="height:75px">')
    a4_img=Markup('<img src="/static/images/svg/jigglypuff.svg" style="height:75px">')
    a5_img=Markup('<img src="/static/images/svg/pokemon.svg" style="height:75px">')
    a6_img=Markup('<img src="/static/images/svg/poliwag.svg" style="height:75px">')
    a7_img=Markup('<img src="/static/images/svg/squirtle.svg" style="height:75px">')
    a8_img=Markup('<img src="/static/images/svg/victini.svg" style="height:75px">')

    a1 = a1_img
    a2 = a2_img
    a3 = a3_img
    a4 = a4_img
    a5 = a5_img
    a6 = a6_img
    a7 = a7_img
    a8 = a8_img
 
    icon = RadioField('Please choose your avatar!', validators = [DataRequired()],
            choices = [(a1, a1_img),(a2, a2_img),(a3, a3_img),
            (a4, a4_img),(a5, a5_img),(a6, a6_img),(a7, a7_img),(a8, a8_img)])
    
    def validate_email(form, field):
        same_email_user = User.query.filter_by(email=field.data).first()
        if same_email_user:
            raise ValidationError("Sorry, the Email is already in use")

class EditProfileForm(FlaskForm):
    first_name = StringField("First Name", validators=[DataRequired()])
    last_name = StringField("Last Name", validators=[DataRequired()])
    email = StringField("Email Address", validators = [DataRequired(), Email()])
    password = PasswordField("Password", validators= [DataRequired()])
    confirm_password = PasswordField("Confirm Password", validators= [DataRequired(), 
        EqualTo("password", message="Passwords MUST match")])
    favorite = StringField("What's your favorite Pokemon?", default=None)
    submit = SubmitField("Update")
    #AVATARS:
    a1_img=Markup('<img src="/static/images/svg/bulbasaur.svg" style="height:75px">')
    a2_img=Markup('<img src="/static/images/svg/chikorita.svg" style="height:75px">')
    a3_img=Markup('<img src="/static/images/svg/eevee.svg" style="height:75px">')
    a4_img=Markup('<img src="/static/images/svg/jigglypuff.svg" style="height:75px">')
    a5_img=Markup('<img src="/static/images/svg/pokemon.svg" style="height:75px">')
    a6_img=Markup('<img src="/static/images/svg/poliwag.svg" style="height:75px">')
    a7_img=Markup('<img src="/static/images/svg/squirtle.svg" style="height:75px">')
    a8_img=Markup('<img src="/static/images/svg/victini.svg" style="height:75px">')

    a0 = "Don't Change"
    a1 = a1_img
    a2 = a2_img
    a3 = a3_img
    a4 = a4_img
    a5 = a5_img
    a6 = a6_img
    a7 = a7_img
    a8 = a8_img
 
    icon = RadioField('Please choose your avatar!', validators = [DataRequired()],
            choices = [(a0,"Don't Change"),(a1, a1_img),(a2, a2_img),(a3, a3_img),
            (a4, a4_img),(a5, a5_img),(a6, a6_img),(a7, a7_img),(a8, a8_img)])


