# config.py
import os

class Config:
    SECRET_KEY = 'your-secret-key'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'your_email@gmail.com'
    MAIL_PASSWORD = 'your_app_password'  # Gmail-এ App Password ব্যবহার করুন