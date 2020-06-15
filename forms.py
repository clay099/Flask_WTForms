from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, IntegerField, SelectField
from wtforms.validators import InputRequired, Optional, URL, NumberRange


class PetForm(FlaskForm):
    """
    form class for a pet
    """

    name = StringField("Pet Name", validators=[
                       InputRequired(message="pets name can't be blank")])
    species = SelectField("Pet Species", choices=[('Cat', "Cat"), ('Dog', "Dog"), ('Porcupine', "Porcupine")], validators=[
                          InputRequired(message="pets species can't be blank")])
    photo_url = StringField("Pet Photo URL", validators=[Optional(), URL(
        require_tld=True, message="input must be a URL")])
    age = IntegerField("Pet Age", validators=[
                       Optional(), NumberRange(min=0, max=30, message="Pets age must be between 0 & 30")])
    notes = StringField("Pet Notes")
    available = BooleanField("Is Pet Available?")
