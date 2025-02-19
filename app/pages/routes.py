from flask import render_template, redirect, url_for, session
from . import pages_bp
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField, DateTimeField
from wtforms.validators import DataRequired, Email, Length, Regexp

class PersonalInfo(FlaskForm):
    lastName = StringField('Last name', validators=[DataRequired("Please enter your last name")])
    firstName = StringField('First name', validators=[DataRequired("Please entery your first name")])
    middleName = StringField('Middle name', validators=[DataRequired("Please enter your middle name")])

    birthCountry = StringField("Place of birth (country)", validators=[DataRequired("Please enter your birth country")])
    birthCity = StringField("Place of birth(city/municipality)", validators=[DataRequired("Please enter your birth city/province")])
    birthProvince = StringField("Place of birth(province)", validators=[DataRequired("Please enter your birth province")])

    birthday = DateTimeField('Birthday', validators=[DataRequired("Please enter your birthday")], format='%Y-%m-%d')
    sex = SelectField('Sex', choices=[(0, "Select Sex"), (1, "Male"), (2, "Female")])
    civilStatus = SelectField('Civil Status', choices=[(0, "Select Civil Status"), (1, "Single"), (2, "Married"), (3, "Widowed"), (4, "Separated")])

    nationality = SelectField('Nationality', choices=[(0, "Select Nationality"), (1, "American"), (2, "Australian"), (3, "Brazilian"), (4, "British"), (5, "Canadian"), (6, "Chinese"), (7, "Filipino"), (8, "French"), (9, "German"), (10, "Indian"), (11, "Indonesian"), (12, "Italian"), (13, "Japanese"), (14, "Korean"), (15, "Malaysian"), (16, "Mexican"), (17, "Russian"), (18, "Singaporean"), (19, "South African"), (20, "Spanish"), (21, "Swiss"), (22, "Thai"), (23, "Vietnamese")])
    religion = StringField('Religion', validators=[DataRequired("Please enter your religion")])
    occupation = StringField('Occupation', validators=[DataRequired("Please enter your occupation")])
    
    bloodType = SelectField('Blood type', choices=[(0, "Select blood type"), (1, "O+"), (2, "O-"), (3, "A+"), (4, "A-"), (5, "B+"), (6, "B-"), (7, "AB+"), (8, "AB-"), (9, "Others")])
    height = StringField('Height(cm)', validators=[DataRequired("Please enter your height in cm")])
    weight = StringField('Weight(kg)', validators=[DataRequired("Please enter your weight in kg")])

    email = StringField('Email', validators=[DataRequired("Please enter your email address"), Email("Please enter a valid email address")])
    phoneNum = StringField('Phone Number', validators=[DataRequired("Please enter your phone number"), Length(max=11, message="Phone number must be between 10 and 15 characters")])
    telNum = StringField('Telephone Number', validators=[Regexp(r'\+\d{10}', message="Invalid telephone number")])

    curBarangay = StringField("Barangay", validators=[DataRequired("Please enter your barangay")])
    curProvince = StringField("Province", validators=[DataRequired("Please enter your province")])
    curCity = StringField("City/Municipality", validators=[DataRequired("Please enter your city/municipality")])
    curBlkLot = StringField("Block Lot Unit Floor", validators=[DataRequired("Please enter your Block Lot Unit Floor")])
    
    presBarangay = StringField("Barangay", validators=[DataRequired("Please enter your barangay")])
    presProvince = StringField("Province", validators=[DataRequired("Please enter your province")])
    presCity = StringField("City/Municipality", validators=[DataRequired("Please enter your city/municipality")])
    presBlkLot = StringField("Block Lot Unit Floor", validators=[DataRequired("Please enter your Block Lot Unit Floor")])
    sameAddress = BooleanField('Same as current address', default=False)
    
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
