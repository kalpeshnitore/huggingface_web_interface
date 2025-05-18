from flask import render_template, request, redirect, url_for
from .forms import ModelSelectionForm
from .models import MODELS_INFO
from transformers import pipeline

def init_routes(app):
    @app.route('/', methods=['GET', 'POST'])
    def index():
        form = ModelSelectionForm()
        
        if form.validate_on_submit():
            model_name = form.model_name.data
            input_text = form.input_text.data
            task_type = MODELS_INFO[model_name]['task']
            
            # मॉडेल लोड करा आणि प्रक्रिया करा
            try:
                pipe = pipeline(task_type, model=model_name)
                result = pipe(input_text)
                return render_template('result.html', 
                                     result=result,
                                     model_name=model_name,
                                     input_text=input_text)
            except Exception as e:
                error = f"त्रुटी: {str(e)}"
                return render_template('index.html', form=form, error=error)
        
        return render_template('index.html', form=form)