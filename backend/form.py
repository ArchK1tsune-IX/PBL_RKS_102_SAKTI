from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError, Regexp, Email
from backend.models import User

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(message="Username tidak boleh kosong"), Length(min=4, message="Username minimal 4 huruf")])
    email = StringField('Email', validators=[DataRequired(message="Email tidak boleh kosong"), Email(message="Email tidak valid")])
    password = PasswordField('Password', validators=[DataRequired(message="Passwword tidak boleh kosong"), Length(min=8, message="Password minimal 8 huruf"), Regexp(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$', message="Password harus mengandung huruf besar, huruf kecil, angka, dan karakter khusus")])
    submit = SubmitField('Register')
    
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("Username sudah digunakan, silahkan gunakan Username yang lain !!!")
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("Email sudah digunakan, silahkan gunakan Email yang lain !!!")
        
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')