from flask import Flask, render_template, session, redirect, url_for
from forms import SubmitForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'any secret string'

@app.route('/')
def home():
    return 'Welcome to the Future'

@app.route('/form', methods=['GET', 'POST', 'DELETE'])
def form():
    form = SubmitForm()
    if form.validate_on_submit():
        session['mobilenumber'] = form.mobilenumber.data
        return redirect(url_for('show_phone'))
    return render_template('form.html', Creator = "Krishna", form=form)


# @app.route('/details')
# def submit():
#     form = SubmitForm()
#     return  render_template('form.html', form=form)


if __name__ == "__main__":
    app.run()