from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from market.models import User


class RegisterForm(FlaskForm):

    def validate_user_name(self, username_to_check):
        user = User.query.filter_by(user_name=username_to_check.data).first()
        if user:
            raise ValidationError('user_name already exists!please try a different one')

    def validate_email_address(self, email_address_to_check):
        email_address = User.query.filter_by(email_address=email_address_to_check.data).first()
        if email_address:
            raise ValidationError('email_address already exists! please try a different one')

    user_name = StringField(label="username:", validators=[Length(min=2, max=10), DataRequired()])
    email_address = StringField(label="EmailAddress:", validators=[Email(), DataRequired()])
    password1 = PasswordField(label="Password:", validators=[Length(min=5), DataRequired()])
    password2 = PasswordField(label="Confirm password:", validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label="Create Account")


class LoginForm(FlaskForm):
    username = StringField(label="User Name:", validators=[DataRequired()])
    password = PasswordField(label="Password:", validators=[DataRequired()])
    submit = SubmitField(label="Sign In")




