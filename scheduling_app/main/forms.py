from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, DateField, SubmitField
from wtforms.ext.sqlalchemy.fields import QuerySelectField, QuerySelectMultipleField
from wtforms.validators import DataRequired, Length, ValidationError
from scheduling_app.models import Load, User

class LoadForm(FlaskForm):
    """Form to create a console."""
    load_number = IntegerField('Load Number', validators=[DataRequired()])
    date = DateField('Date Scheduled', validators=[DataRequired()])
    shipping_order_number = IntegerField('Shipping Order Number', validators=[DataRequired()])
    customer = StringField('Customer', validators=[DataRequired(), Length(min=3, max=80)])
    trucker = StringField('Trucker', validators=[DataRequired(), Length(min=3, max=80)])
    pallet_amount = IntegerField('Pallet Amount', validators=[DataRequired()])
    pickup = BooleanField('Pickup?')
    submit = SubmitField('Submit')