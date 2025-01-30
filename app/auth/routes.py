from flask import render_template, redirect, url_for, request, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField, DateTimeField
from wtforms.validators import DataRequired, Email
from . import auth_bp

class Login(FlaskForm):
    username = StringField('Username', validators=[DataRequired("Please enter your username")])
    password = PasswordField('Password', validators=[DataRequired("Please enter your password")])   
    remember_me = BooleanField('Remember Me', default=False)
    submit = SubmitField('Login')

class GenRegister(FlaskForm):
    fName = StringField('First Name', validators=[DataRequired("Please enter your first name")])
    lName = StringField('Last Name', validators=[DataRequired("Please enter your last name")])
    mName = StringField('Middle Name', validators=[DataRequired("Please enter your middle name")])
    exName = StringField('Extension Name')
    gender = SelectField('Gender', choices=[(0, "Selec Gender"),(1, "Male"), (2, "Female")])
    civilStatus = SelectField('Civil Status', choices=[(0,"Select Civil Status"),(1, "Single"), (2, "Married"), (3, "Widowed"), (4, "Separated")])
    nationality = SelectField('Nationality', choices=[(0, "Select Nationality"),(1, "American"), (2, "Australian"), (3, "Brazilian"), (4, "British"), (5, "Canadian"), (6, "Chinese"), (7, "Filipino"), (8, "French"), (9, "German"), (10, "Indian"), (11, "Indonesian"), (12, "Italian"), (13, "Japanese"), (14, "Korean"), (15, "Malaysian"), (16, "Mexican"), (17, "Russian"), (18, "Singaporean"), (19, "South African"), (20, "Spanish"), (21, "Swiss"), (22, "Thai"), (23, "Vietnamese")])
    birthday = DateTimeField('Birthday',validators=[DataRequired("Please enter your birthday")], format='%Y-%m-%d')
    birthplace = StringField('Birthplace', validators=[DataRequired("Please enter your birthplace")])
    occupation = StringField('Occupation', validators=[DataRequired("Please enter your occupation")])
    fatherName = StringField('Father Name', validators=[DataRequired("Please enter your father's name")])
    fatherOccupation = StringField('Father Occupation', validators=[DataRequired("Please enter your father's occupation")])
    motherName = StringField('Mother Name', validators=[DataRequired("Please enter your mother's name")])
    motherOccupation = StringField('Mother Occupation', validators=[DataRequired("Please enter your mother's occupation")])
    submit = SubmitField('Next')

class ContactRegister(FlaskForm):
    email = StringField('Email', validators=[DataRequired("Please enter your email address"), Email("Please enter a valid email address")])
    mobile = StringField('Mobile Number', validators=[DataRequired("Please enter your mobile number")])
    phone = StringField('Phone Number', validators=[DataRequired("Please enter your phone number")])
    city = StringField('City', validators=[DataRequired("Please enter your city")])
    region = StringField('Region', validators=[DataRequired("Please enter your region")])
    province = StringField('Province', validators=[DataRequired("Please enter your province")])
    barangay = StringField('Barangay', validators=[DataRequired("Please enter your barangay")])
    zipCode = StringField('Zip Code', validators=[DataRequired("Please enter your zip code")])
    blkLotStrt = StringField('Blk/Lot/Street', validators=[DataRequired("Please enter your block/lot/street")])
    country = StringField('Country', validators=[DataRequired("Please enter your country")])
    addInfo = StringField('Additional Information')
    submit = SubmitField('Next')

class AccountRegister(FlaskForm):
    username = StringField('Username', validators=[DataRequired("Please enter your username")])
    password = PasswordField('Password', validators=[DataRequired("Please enter your password")])
    confirmPassword = PasswordField('Confirm Password', validators=[DataRequired("Please confirm your password")])
    submit = SubmitField('Register')

class ForgotPassword(FlaskForm):
    username = StringField('Email', validators=[DataRequired("Please enter your email address"), Email("Please enter a valid email address")])
    new_password = PasswordField('New Password', validators=[DataRequired("Please enter your new password")])
    submit = SubmitField('Submit')

@auth_bp.route('/get-started')
def get_started():
    return render_template('get-started.html', include_navbar=False)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = Login()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        form.email.data = ''
        form.password.data = ''
        return redirect(url_for('home', username=username, password=password))
    
    if request.method == 'POST':
        for field, errors in form.errors.items():
            for error in errors:
                flash(f"Error in the {getattr(form, field).label.text} field - {error}")

    return render_template('login.html', form=form, include_navbar=True)

@auth_bp.route('/gen-register', methods=['GET', 'POST'])
def gen_register():
    form = GenRegister()

    if form.validate_on_submit():
        fname = form.fName.data
        lname = form.lName.data
        mname = form.mName.data
        exName = form.exName.data
        gender = form.gender.data
        civilStatus = form.civilStatus.data
        nationality = form.nationality.data
        birthday = form.birthday.data
        birthplace = form.birthplace.data
        occupation = form.occupation.data
        fatherName = form.fatherName.data
        fatherOccupation = form.fatherOccupation.data
        motherName = form.motherName.data
        motherOccupation = form.motherOccupation.data
        
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
        
        return redirect(url_for('auth.pass_data', fname=fname, lname=lname, mname=mname, exName=exName, gender=gender, civilStatus=civilStatus, nationality=nationality, birthday=birthday, birthplace=birthplace, occupation=occupation, fatherName=fatherName, fatherOccupation=fatherOccupation, motherName=motherName, motherOccupation=motherOccupation))
    return render_template('gen-register.html', form=form, include_navbar=True)

@auth_bp.route('/contact-register', methods=['GET', 'POST'])
def contact_register():
    form = ContactRegister()

    if form.validate_on_submit():
        email = form.email.data
        mobile = form.mobile.data
        phone = form.phone.data
        city = form.city.data
        zipCode = form.zipCode.data
        region = form.region.data
        province = form.province.data
        barangay = form.barangay.data
        blkLotStrt = form.blkLotStrt.data
        country = form.country.data
        addInfo = form.addInfo.data

        # Reset form data
        form.email.data = ''
        form.mobile.data = ''
        form.phone.data = ''
        form.zipCode.data = ''
        form.region.data = ''
        form.city.data = ''
        form.province.data = ''
        form.barangay.data = ''
        form.blkLotStrt.data = ''
        form.country.data = ''
        form.addInfo.data = ''

        return redirect(url_for('home', email=email, mobile=mobile, phone=phone, city=city, region=region, zipCode=zipCode, province=province, barangay=barangay, blkLotStrt=blkLotStrt, country=country, addInfo=addInfo))
    return render_template('contact-register.html', form=form, include_navbar=True)

@auth_bp.route('/account-register', methods=['GET', 'POST'])
def account_register():
    form = AccountRegister()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        confirmPassword = form.confirmPassword.data

        # Reset form data
        form.username.data = ''
        form.password.data = ''
        form.confirmPassword.data = ''

        return redirect(url_for('home', username=username, password=password, confirmPassword=confirmPassword))
    return render_template('account-register.html', form=form, include_navbar=True)

@auth_bp.route('/forgot-password', methods=['GET', 'POST'])
def forgot_password():
    form = ForgotPassword()

    if form.validate_on_submit():
        username = form.username.data
        new_password = form.new_password.data

        # Reset form data
        form.username.data = ''
        form.new_password.data = ''

        return redirect(url_for('home', username=username, new_password=new_password))
    return render_template('forgot-password.html', form=form, include_navbar=True)

@auth_bp.route('/pass')
def pass_data():
    fName = request.args.get('fname')
    lName = request.args.get('lname')
    mName = request.args.get('mname')
    exName = request.args.get('exName')
    gender = request.args.get('gender')
    civilStatus = request.args.get('civilStatus')
    nationality = request.args.get('nationality')
    birthday = request.args.get('birthday')
    birthplace = request.args.get('birthplace')
    occupation = request.args.get('occupation')
    fatherName = request.args.get('fatherName')
    fatherOccupation = request.args.get('fatherOccupation')
    motherName = request.args.get('motherName')
    motherOccupation = request.args.get('motherOccupation')
    
    return render_template('pass.html', include_navbar=True, fName=fName, lName=lName, mName=mName, exName=exName, gender=gender, civilStatus=civilStatus, nationality=nationality, birthday=birthday, birthplace=birthplace, occupation=occupation, fatherName=fatherName, fatherOccupation=fatherOccupation, motherName=motherName, motherOccupation=motherOccupation)