from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField
from wtforms.validators import DataRequired

class PricingForm(FlaskForm):
    historical_price = FloatField('Historical Price', validators=[DataRequired()])
    demand_factor = FloatField('Demand Factor', validators=[DataRequired()])
    seasonal_factor = FloatField('Seasonal Factor', validators=[DataRequired()])
    competitor_price = FloatField('Competitor Price', validators=[DataRequired()])
    submit = SubmitField('Run Model')
