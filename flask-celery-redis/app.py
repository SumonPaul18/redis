# app.py
from flask import Flask, request, render_template_string
from flask_mail import Mail
from config import Config
from tasks import make_celery, send_welcome_email

app = Flask(__name__)
app.config.from_object(Config)

mail = Mail(app)
celery = make_celery(app)

# সাধারণ HTML ফর্ম
HTML_FORM = '''
<h2>রেজিস্ট্রেশন ফর্ম</h2>
<form method="POST">
    <input type="text" name="name" placeholder="আপনার নাম" required><br><br>
    <input type="email" name="email" placeholder="ইমেইল" required><br><br>
    <button type="submit">সাবমিট</button>
</form>
'''

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]

        # Celery টাস্ক চালু করুন (ব্যাকগ্রাউন্ডে)
        task = send_welcome_email.delay(email, name)

        return f"""
        <h3>ধন্যবাদ, {name}!</h3>
        <p>আপনার রেজিস্ট্রেশন সম্পন্ন হয়েছে।</p>
        <p>ইমেইল আইডি: {email}</p>
        <p>ইমেইল পাঠানো হচ্ছে... (টাস্ক আইডি: {task.id})</p>
        <a href="/">আবার ফর্ম পূরণ করুন</a>
        """
    return render_template_string(HTML_FORM)

if __name__ == "__main__":
    app.run(debug=True)