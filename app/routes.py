from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import PricingForm
from app.game_theory import run_game_theory_model

@app.route('/', methods=['GET', 'POST'])
def home():
    form = PricingForm()
    if form.validate_on_submit():
        flash('Game theory model is running...')
        results = run_game_theory_model(form.data)
        return render_template('results.html', form=form, results=results)
    return render_template('home.html', form=form)


# from flask import render_template, request
# from app import app

# # Add your pricing optimization logic here

# @app.route('/')
# @app.route('/index')
# def index():
#     return render_template('index.html')

# if __name__ == '__main__':
#     app.run(debug=True)
