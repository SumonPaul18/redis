# tasks.py
from celery import Celery
from flask_mail import Message
from app import mail, app

def make_celery(app):
    celery = Celery(
        app.import_name,
        backend="redis://192.168.0.207:6379/0",
        broker="redis://192.168.0.207:6379/0"
    )
    celery.conf.update(app.config)

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery

# টাস্ক ডিফাইন করা
@celery.task
def send_welcome_email(email, name):
    with app.app_context():
        msg = Message(
            subject="স্বাগতম!",
            recipients=[email],
            body=f"হ্যালো {name}, আপনাকে আমাদের সাইটে স্বাগতম!"
        )
        mail.send(msg)
    return f"ইমেইল পাঠানো হয়েছে: {email}"