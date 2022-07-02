from flask_wtf import Form
from wtforms import Form, StringField, TextAreaField, SubmitField, validators

class ParticipantForm(Form):
    fname = StringField('First Name', [validators.DataRequired("Please enter your first name.")])
    lname = StringField('Last Name', [validators.DataRequired("Please enter your last name.")])
    email = StringField('Email', [validators.DataRequired("Please enter your email address."), validators.Email("Please enter a valid email address.")])
    address = TextAreaField('Postal Address', [validators.DataRequired("Please enter your postal address.")])
    phone = StringField('Phone', [validators.DataRequired()])
    submit = SubmitField('Register')