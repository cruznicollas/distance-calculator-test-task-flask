from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class GetCoordinates(FlaskForm):
    destiny = StringField('destinations', validators=[DataRequired()])

