from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField
from wtforms.validators import DataRequired
from .models import MODELS_INFO

class ModelSelectionForm(FlaskForm):
    # ड्रॉपडाउन मेनूसाठी पर्याय तयार करा
    model_choices = [(key, f"{value['name']} - {value['description']}") 
                     for key, value in MODELS_INFO.items()]
    
    model_name = SelectField('मॉडेल निवडा', 
                           choices=model_choices,
                           validators=[DataRequired()])
    
    input_text = TextAreaField('इनपुट टेक्स्ट', 
                              validators=[DataRequired()],
                              render_kw={"placeholder": "तुमचा टेक्स्ट येथे टाइप करा..."})