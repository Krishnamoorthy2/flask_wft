from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, PasswordField, widgets
from wtforms.validators import DataRequired, ValidationError, Email
from wtforms.fields import core, html5, simple
import phonenumbers
import email_validator



class SubmitForm(FlaskForm):
    username = StringField('User Name', validators=[DataRequired(),Length(min=2, max=20)])
    mobilenumber =StringField('Phone Number', validators=[DataRequired()])
    email = html5.EmailField(label=' email ',validators=[DataRequired(message=' the mailbox cannot be empty. '),Email(message=' email format error ')],widget=widgets.TextInput(input_type='email'),render_kw={'class': 'form-control'})
    gender = core.RadioField(label=' gender ',choices=((1, ' male '),(2, ' female '),), coerce=int)
    
    subject = core.SelectField(label=' Subject ', choices=(('ta', ' Tamil '),('sc', ' Science '),('ma', ' Maths '),('ss', ' Social Science ')))
    submit = SubmitField('Submit')
    def validate_phone(self, form, field):
        if len(field.data) > 16:
            raise ValidationError('Invalid phone number.')
        try:
            input_number = phonenumbers.parse(field.data)
            if not (phonenumbers.is_valid_number(input_number)):
                raise ValidationError('Invalid phone number.')
        except:
            input_number = phonenumbers.parse("+91"+field.data)
            if not (phonenumbers.is_valid_number(input_number)):
                raise ValidationError('Invalid phone number.')