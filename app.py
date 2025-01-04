from flask import Flask, render_template, request, redirect, url_for, flash, send_file
from flask_login import LoginManager, login_user, logout_user, current_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import create_engine, text
from sqlalchemy.exc import ProgrammingError
from backend.config import Config
from backend.models import db, User 
from backend.form import RegisterForm, LoginForm
from cipher.classic import caesar_encryption, caesar_decryption, vigenere_encryption, vigenere_decryption, transposition_encrypt, transposition_decrypt
from cipher.classic import caesar_encrypt_file, caesar_decrypt_file, vigenere_encrypt_file, vigenere_decrypt_file, transposition_encrypt_file, transposition_decrypt_file
from steganography.steganography import embed_text, embed_and_encrypt, extract_text, extract_and_decrypt
import os

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

def create_database():
    engine = create_engine('mysql://root@localhost')
    db_name = 'pbl_rks_102_sakti'
    
    with engine.connect() as conn:
        existing_database = conn.execute(text("SHOW DATABASES;"))
        databases = [d[0] for d in existing_database]
        if db_name not in databases:
            conn.execute(text(f"CREATE DATABASE {db_name};"))
            print(f"Database '{db_name}' created successfully")
        else:
            print(f"Database '{db_name}' already exists")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data)
        new_user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash("Berhasil Registrasi, Yey!", "success")
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            flash("Berhasil Login, Welcome!", "success")
            return redirect(url_for('dashboard'))
        else:
            flash("Username atau Password salah!!!", "danger")
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

@app.route('/cytix', methods=['GET', 'POST'])
@login_required
def cytix():
    result = ""
    download_path = ""
    if request.method == 'POST':
        text = request.form.get("text", "")
        cipher = request.form.get("cipher", "")
        key = request.form.get("key", "")
        action = request.form.get("action", "")
        file = request.files.get("file")

        try:
            # Validasi input key
            if cipher == 'vigenere' and not key.isalpha():
                flash("Key harus berupa string alfabet untuk Vigenère cipher.", "danger")
                return redirect(url_for('cytix'))
            elif cipher in ['caesar', 'transposition'] and not key.isdigit():
                flash("Key harus berupa angka untuk algoritma ini.", "danger")
                return redirect(url_for('cytix'))

            if cipher in ["caesar", "vigenere", "transposition"]:
                # Handle file encryption/decryption
                if file:
                    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
                    output_path = os.path.join(app.config['RESULT_FOLDER'], f"processed_{file.filename}")
                    file.save(file_path)

                    if cipher == 'caesar':
                        shift = int(key)
                        if action == 'Encrypt':
                            caesar_encrypt_file(file_path, output_path, shift)
                        else:
                            caesar_decrypt_file(file_path, output_path, shift)
                    elif cipher == 'vigenere':
                        if action == 'Encrypt':
                            vigenere_encrypt_file(file_path, output_path, key)
                        else:
                            vigenere_decrypt_file(file_path, output_path, key)
                    elif cipher == 'transposition':
                        if action == 'Encrypt':
                            transposition_encrypt_file(file_path, output_path, key)
                        else:
                            transposition_decrypt_file(file_path, output_path, key)

                    download_path = output_path
                # Handle text encryption/decryption
                else:
                    if cipher == 'caesar':
                        shift = int(key)
                        result = caesar_encryption(text, shift) if action == 'Encrypt' else caesar_decryption(text, shift)
                    elif cipher == 'vigenere':
                        result = vigenere_encryption(text, key) if action == 'Encrypt' else vigenere_decryption(text, key)
                    elif cipher == 'transposition':
                        result = transposition_encrypt(text, int(key)) if action == 'Encrypt' else transposition_decrypt(text, int(key))
        except Exception as e:
            flash(f"Error: {str(e)}", "danger")

        if download_path:
            return send_file(download_path, as_attachment=True)

    return render_template('cytix.html', result=result)

@app.route('/steaky', methods=['GET', 'POST'])
@login_required
def steaky():
    result = ""
    download_path = ""
    if request.method == 'POST':
        action = request.form.get("action", "")
        text = request.form.get("text", "")
        key = request.form.get("key", "")
        aes_type = int(request.form.get("aes_type", 128)) if request.form.get("aes_type") else 128
        file = request.files.get("file")

        try:
            if action in ["embed_text", "extract_text", "embed_encrypt", "extract_decrypt"]:
                if not file:
                    flash("File gambar diperlukan untuk aksi ini.", "danger")
                    return redirect(url_for('steaky'))
                
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
                file.save(file_path)

                if action == "embed_text":
                    output_path = os.path.join(app.config['RESULT_FOLDER'], f"{file.filename}_embedded.png")
                    embed_text(file_path, text, output_path)
                    download_path = output_path
                elif action == "extract_text":
                    result = extract_text(file_path)
                    flash("Berhasil mengekstrak teks dari gambar!", "success")
                elif action == "embed_encrypt":
                    output_path = os.path.join(app.config['RESULT_FOLDER'], f"{file.filename}_encrypted_embedded.png")
                    embed_and_encrypt(file_path, text, key, aes_type, output_path)
                    download_path = output_path
                elif action == "extract_decrypt":
                    result = extract_and_decrypt(file_path, key, aes_type)
                    flash("Berhasil mengekstrak dan mendekripsi teks dari gambar!", "success")
            else:
                flash("Aksi tidak valid!", "danger")

            if download_path:
                return send_file(download_path, as_attachment=True)

        except ValueError as ve:
            flash(f"Kesalahan: {str(ve)}", "danger")
        except Exception as e:
            flash(f"Terjadi kesalahan: {str(e)}", "danger")

    return render_template('steaky.html', result=result)


if __name__ == '__main__':
    create_database()
    with app.app_context():
        db.create_all()
    app.run(debug=True)