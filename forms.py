from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired

class MainForm(Form):
    priceLow = StringField('Price Lower Bound', validators=[DataRequired()], render_kw={"value": "5"})
    priceHigh = StringField('Price Upper Bound', validators=[DataRequired()], render_kw={"value": "25"})