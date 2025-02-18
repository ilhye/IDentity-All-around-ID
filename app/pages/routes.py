from flask import render_template, redirect, url_for, session
from . import pages_bp
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField, DateTimeField
from wtforms.validators import DataRequired, Email

class PersonalInfo(FlaskForm):
    fullname = StringField('Full name', validators=[
                        DataRequired("Please enter your full name")])
    gender = SelectField('Gender', choices=[
                         (0, "Select Gender"), (1, "Male"), (2, "Female")])
    civilStatus = SelectField('Civil Status', choices=[(
        0, "Select Civil Status"), (1, "Single"), (2, "Married"), (3, "Widowed"), (4, "Separated")])
    nationality = SelectField('Nationality', choices=[(0, "Select Nationality"), (1, "American"), (2, "Australian"), (3, "Brazilian"), (4, "British"), (5, "Canadian"), (6, "Chinese"), (7, "Filipino"), (8, "French"), (9, "German"), (10, "Indian"), (
        11, "Indonesian"), (12, "Italian"), (13, "Japanese"), (14, "Korean"), (15, "Malaysian"), (16, "Mexican"), (17, "Russian"), (18, "Singaporean"), (19, "South African"), (20, "Spanish"), (21, "Swiss"), (22, "Thai"), (23, "Vietnamese")])
    birthday = DateTimeField('Birthday', validators=[DataRequired(
        "Please enter your birthday")], format='%Y-%m-%d')
    birthplace = StringField('Birthplace', validators=[
                             DataRequired("Please enter your birthplace")])
    occupation = StringField('Occupation', validators=[
                             DataRequired("Please enter your occupation")])
    fatherName = StringField('Father Name', validators=[
                             DataRequired("Please enter your father's name")])
    fatherOccupation = StringField('Father Occupation', validators=[
                                   DataRequired("Please enter your father's occupation")])
    motherName = StringField('Mother Name', validators=[
                             DataRequired("Please enter your mother's name")])
    motherOccupation = StringField('Mother Occupation', validators=[
                                   DataRequired("Please enter your mother's occupation")])
    submit = SubmitField('Next')


class HomeID(FlaskForm):
    submit = SubmitField('Submit')

@pages_bp.route('/page-one')
def page_one():
    return "Page One"

@pages_bp.route('/home-id')
def home_id():
    form=HomeID()

    if form.validate_on_submit():
        return redirect(url_for('pages.home_id'))
    return render_template('homeid.html')

@pages_bp.route('/notifications')
def notifications():
    return render_template('Notification.html')

@pages_bp.route('/profile')
def profile():
    form = PersonalInfo()

    if form.validate_on_submit():
        session['personal_info'] = {
            'fname': form.fName.data,
            'lname': form.lName.data,
            'mname': form.mName.data,
            'exName': form.exName.data,
            'gender': form.gender.data,
            'civilStatus': form.civilStatus.data,
            'nationality': form.nationality.data,
            'birthday': form.birthday.data.strftime('%Y-%m-%d'),
            'birthplace': form.birthplace.data,
            'occupation': form.occupation.data,
            'fatherName': form.fatherName.data,
            'fatherOccupation': form.fatherOccupation.data,
            'motherName': form.motherName.data,
            'motherOccupation': form.motherOccupation.data
        }

        # Reset form data
        form.fName.data = ''
        form.lName.data = ''
        form.mName.data = ''
        form.exName.data = ''
        form.gender.data = ''
        form.civilStatus.data = ''
        form.nationality.data = ''
        form.birthday.data = ''
        form.birthplace.data = ''
        form.occupation.data = ''
        form.fatherName.data = ''
        form.fatherOccupation.data = ''
        form.motherName.data = ''
        form.motherOccupation.data = ''
        return redirect(url_for('pages.profile'))
    return render_template('profile.html', form=form, include_sidebar=True)
