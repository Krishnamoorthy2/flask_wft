from flask import *
from flask_sqlalchemy import *
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///student.db'

db = SQLAlchemy(app)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(200), nullable=False)
    last_name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(4096))
    gender = db.Column(db.String(10))
    subject = db.Column(db.String(200))
    phone_number = db.Column(db.Integer)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __init__(self, first_name, last_name, email, gender, subject, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.gender = gender
        self.subject = subject
        self.phone_number = phone_number
    

subscribers = []
details = []

@app.route('/form', methods=['GET'])
def delete():
    student_del = Student.query.get_or_404()

    try:
        db.session.delete(student_del)
        db.session.commit()

        return redirect('/form')
    except:
        return " there was problem "

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/subscribe')
def subscribe():

    title = 'Subscribe to the Channel'
    return render_template("subscribe.html", title = title)

@app.route('/form', methods=['POST', 'GET'])
def form():

    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    email = request.form.get('email')
    gender =request.form.get('gender')
    phone_number = request.form.get('phone_number')
    subject = request.form.get('subject')
    
    
    if not first_name or not last_name or not email:
        error_statement = "All the fields are required "
        return render_template('subscribe.html', error_statement=error_statement, first_name=first_name, last_name=last_name, email=email)

    if request.method == 'POST':
        try:
            new_student = Student(first_name, last_name, email, gender, subject, phone_number)
            
            db.session.add(new_student)
            db.session.commit()
            subscribers.append(f"{first_name} {last_name} | {email} | {phone_number} | {gender} | {subject}")
            title = 'Thank you Subscribing....'
            return render_template("forms.html", subscribers=subscribers, title=title)
        except:
            return "There was an error in Student Table"
    else:
        print("Hi")
        subscribers.append(f"{first_name} {last_name} | {email} | {phone_number} | {gender} | {subject}")
        title = 'Thank you Subscribing....'
        return render_template("forms.html", subscribers=subscribers, title=title)



if __name__ == "__main__":
    app.run()