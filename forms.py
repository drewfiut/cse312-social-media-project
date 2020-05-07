from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField, IntegerField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    first_name = StringField('First name',
                           validators=[DataRequired()])
    last_name = StringField('Last name',
                           validators=[DataRequired()])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    image = FileField('Image', validators=[FileAllowed(['jpg'])])
    submit = SubmitField('Join')

class CommentForm(FlaskForm):
    comment = TextAreaField('Comment', validators=[DataRequired()])
    post = SubmitField('Submit')

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    number = IntegerField('Desired Number of Members', validators=[DataRequired()])
    types = SelectField('Type of Project', validators=[DataRequired()], choices=[
                                                    ('General', 'General'),
                                                    ('Computer Programming', 'Computer Programming'),
                                                    ('Business', 'Business'),
                                                    ('Creative', 'Creative'),
                                                    ('Manufacturing/Products', 'Manufacturing/Products'),
                                                    ('Other', 'Other')])
    image = FileField('Image', validators=[DataRequired(), FileAllowed(['jpg'])])
    post = SubmitField('Post')

class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')

