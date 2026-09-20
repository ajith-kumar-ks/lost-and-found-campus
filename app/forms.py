from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Email, Length


class RegistrationForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(), Length(min=2, max=100)])
    email = EmailField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=8, max=16)])
    submit = SubmitField("Sign Up")


class LoginForm(FlaskForm):
    email = EmailField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=8, max=16)])
    submit = SubmitField("Sign In")


class ItemForm(FlaskForm):
    name = StringField("Item Name", validators=[DataRequired(), Length(max=100)])
    category = StringField("Category", validators=[DataRequired(), Length(max=50)])
    location = StringField("Location", validators=[DataRequired(), Length(max=100)])
    description = TextAreaField("Description")
    type = SelectField("Type", choices=[
        ("lost", "Lost"),
        ("found", "Found")
    ],
    validators=[DataRequired()])
    submit = SubmitField("Submit")


class Claimform(FlaskForm):
    message = TextAreaField("Why do you think this item matches?", validators=[DataRequired()])
    verification_details = TextAreaField("Provide the identifying details", validators=[DataRequired()])
    submit = SubmitField("Submit Claim")