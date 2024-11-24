from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length


# Example updated form
class ExampleForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(), Length(min=3, max=50)])
    password = PasswordField(
        "Password", validators=[DataRequired(), Length(min=6, max=30)]
    )
    submit = SubmitField("Submit")
