from flask_wtf import Form
from wtforms import StringField, IntegerField, BooleanField
from wtforms.validators import DataRequired

class FormGeneral(Form):
    distanceLow = IntegerField('Price Lower Bound', render_kw={"value": "5"})
    distanceHigh = IntegerField('Price Upper Bound', render_kw={"value": "10"})
    oneDollar = BooleanField('One Dollar Sign')
    twoDollar = BooleanField('Two Dollar Signs')
    threeDollar = BooleanField('Three Dollar Signs')
    fourDollar = BooleanField('Four Dollar Signs')
    numFriends = IntegerField('Number of Friends', render_kw={"value": "2"})