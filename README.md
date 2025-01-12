# Cryptography and Steganography Web Application

This project is a web-based application developed using Python with a MySQL database backend. It combines cryptographic and steganographic techniques to provide a secure platform for encrypting and hiding information. The application is designed with cybersecurity principles, including password validation with regex and protection against CSRF attacks.

## Features

### 1. **Homepage**
   - Overview of the application and its features.
   - User-friendly interface for navigation.

### 2. **User Authentication**
   - **Register**: Secure user registration with password validation using regex.
   - **Login**: Secure login system with hashed passwords.

### 3. **Dashboard**
   - Central hub for accessing all features after logging in.
   - Displays user activity and quick links to functionalities.

### 4. **Cytix**
   - Cryptography text encryption and decryption.
   - Supported algorithms:
     - Caesar Cipher (Classic)
     - Vigenère Cipher (Classic)
     - Transposition Cipher (Classic)

### 5. **Steaky**
   - Steganography for images.
   - Modern cryptography implementation using AES for secure embedding.

## Security Features

- **Password Validation**:
  - Passwords are validated using regular expressions to ensure strong password practices.
  - Example rules: Minimum 8 characters, must include uppercase, lowercase, number, and special character.

- **CSRF Protection**:
  - Implemented to secure forms and prevent unauthorized actions on behalf of authenticated users.

- **Data Encryption**:
  - Sensitive data is encrypted using AES (Advanced Encryption Standard).

- **Secure Authentication**:
  - Passwords are stored using hashing algorithms to prevent unauthorized access even if the database is compromised.

## Technologies Used

### Backend
- Python (Flask or Django Framework)
- MySQL Database

### Frontend
- HTML5, CSS3, JavaScript
- Bootstrap for responsive design

### Cryptographic Algorithms
- **Classic Cryptography**:
  - Caesar Cipher
  - Vigenère Cipher
  - Transposition Cipher
- **Modern Cryptography**:
  - AES (Advanced Encryption Standard)

## Installation

### Prerequisites
1. Python 3.8 or higher
2. MySQL Database Server
3. Virtual Environment (optional but recommended)

### Steps
1. Clone the repository:
   ```bash
   git clone [https://github.com/your-username/your-repository.git](https://github.com/ArchK1tsune-IX/PBL_RKS_102_SAKTI)
   ```
2. Navigate to the project directory:
   ```bash
   cd your-repository
   ```
3. Set up a virtual environment (optional):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Set up the database:
   - Run MySQL by XAMPP or MySQL service
6. Start the application:
   ```bash
   python app.py  # Or the relevant start script for the framework
   ```
7. Access the application in your web browser at `http://localhost:5000`.

## Usage
1. Register a new user account.
2. Log in with your credentials.
3. Navigate through the dashboard to use cryptography or steganography features.
4. Experiment with text encryption/decryption and image steganography securely.

## Contributing
1. Muhammad Reza Pahlevi as Leader Team
  - Create app.py file and setup the databases
  - Create AES encryption and decryption function
  - Create steganography embed, extract function
  - Create Caesar, Vigenere and Transposition encryption and decryption function
  - Prepare Presentation materials
2. Syahneezha Putri Desfranza as Member Team
  - Create and design register, login, dashboard html pages
  - Menyusun laporan
  - Create a Poster that provides a brief view
  - Create and prepare Presentation materials
3. Dimaz Zahid Mahawira as Member Team
  - Create and design home, cytix, steaky html pages
  - Editing video demo and presentation
  - Create a Poster that provides a brief view
  - Prepare Presentation materials

## License
This application was developed by our team as part of the PBL-RKS505 project

## Acknowledgments
- Thanks to the developers of the cryptographic algorithms and libraries used in this project.
- Inspired by the principles of secure software development.
