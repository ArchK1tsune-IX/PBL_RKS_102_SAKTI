import os

class Config:
    SECRET_KEY = 'Masadepan123!'
    SQLALCHEMY_DATABASE_URI = 'mysql://root@localhost/pbl_rks_102_sakti'
    UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')
    RESULT_FOLDER = os.path.join(os.getcwd(), 'results')
    
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    os.makedirs(RESULT_FOLDER, exist_ok=True)